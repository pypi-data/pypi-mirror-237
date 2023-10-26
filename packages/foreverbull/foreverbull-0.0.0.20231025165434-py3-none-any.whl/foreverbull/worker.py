import logging
from datetime import datetime
from functools import partial
from multiprocessing import Event, Process
from threading import Thread
from typing import List

import pynng
from pydantic import BaseModel
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from foreverbull import data, environment, models


class Request(BaseModel):
    execution: str
    timestamp: datetime
    symbol: str


class ConfigurationError(Exception):
    pass


class RunError(Exception):
    pass


class Worker:
    def __init__(self, survey_address: str, state_address: str, stop_event: Event, file_path: str):
        self.logger = logging.getLogger(__name__)
        self.logger.debug("setting up worker")
        self._survey_address = survey_address
        self._state_address = state_address
        self._stop_event = stop_event
        self._database = None
        self._file_path = file_path
        super(Worker, self).__init__()

    @staticmethod
    def _eval_param(type: str, val):
        if type == "int":
            return int(val)
        elif type == "float":
            return float(val)
        elif type == "bool":
            return bool(val)
        elif type == "str":
            return str(val)
        else:
            raise ConfigurationError("Unknown parameter type")

    def _setup_algorithm(self, parameters: List[models.service.Parameter]):
        func = partial(environment.func)
        default_parameters = {param.key: param for param in environment.parameters}
        configured_parameters = {param.key: param for param in parameters}

        for parameter in default_parameters:
            value = None
            if default_parameters[parameter].default:
                value = self._eval_param(default_parameters[parameter].type, default_parameters[parameter].default)
            if parameter in configured_parameters:
                value = self._eval_param(configured_parameters[parameter].type, configured_parameters[parameter].value)
            if value is None:
                raise ConfigurationError(f"Parameter {parameter} has no default value and is not configured")
            func = partial(func, **{parameter: value})
        return func

    def _process(self, request: Request):
        self.logger.debug("Processing: %s", request)
        with self._database_session() as db_session:
            asset = data.Asset.read(request.symbol, request.timestamp, db_session)
            portfolio = data.Portfolio.read(request.execution, request.timestamp, db_session)
        return self._algo(asset=asset, portfolio=portfolio)

    def configure_execution(self, execution: models.backtest.Execution):
        self.logger.info("configuring worker")
        self.socket = pynng.Rep0(dial=f"tcp://{execution.socket.host}:{execution.socket.port}")
        self.socket.recv_timeout = 5000
        self.socket.send_timeout = 5000
        self._algo = self._setup_algorithm(execution.parameters or [])
        engine = create_engine(execution.database.url)
        with engine.connect() as connection:
            connection.execute(text("SELECT 1 from asset;"))
        self._database_session = sessionmaker(bind=engine)
        self.logger.info("worker configured correctly")

    def run(self):
        environment.import_file(self._file_path)
        responder = pynng.Respondent0(dial=self._survey_address)
        responder.send_timeout = 5000
        responder.recv_timeout = 5000
        state = pynng.Pub0(dial=self._state_address)
        state.send(b"ready")
        self.logger.info("starting worker")
        while True:
            try:
                request = models.service.Request.load(responder.recv())
                self.logger.info("Received request")
                if request.task == "configure_execution":
                    execution = models.backtest.Execution(**request.data)
                    self.configure_execution(execution)
                    responder.send(models.service.Response(task=request.task, error=None).dump())
                elif request.task == "run_execution":
                    responder.send(models.service.Response(task=request.task, error=None).dump())
                    self.run_execution()
            except pynng.exceptions.Timeout:
                if self._stop_event.is_set():
                    break
            except Exception as e:
                self.logger.exception(repr(e))
                responder.send(models.service.Response(task=request.task, error=repr(e)).dump())
        responder.close()
        state.close()

    def run_execution(self):
        while True:
            try:
                self.logger.debug("Getting context socket")
                context_socket = self.socket.new_context()
                request = models.service.Request.load(context_socket.recv())
                order = self._process(Request(**request.data))
                self.logger.debug(f"Sending response {order}")
                context_socket.send(models.service.Response(task=request.task, data=order).dump())
                context_socket.close()
            except pynng.exceptions.Timeout:
                context_socket.close()
            except Exception as e:
                self.logger.exception(repr(e))
                context_socket.send(models.service.Response(task=request.task, error=repr(e)).dump())
                context_socket.close()
            if self._stop_event.is_set():
                break
        self.socket.close()


class WorkerThread(Worker, Thread):
    pass


class WorkerProcess(Worker, Process):
    pass

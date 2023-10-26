from datetime import datetime

from pandas import DataFrame, read_sql_query
from sqlalchemy import text
from sqlalchemy.orm.session import Session

from foreverbull import models


class Asset(models.finance.Asset):
    _as_of: datetime
    _db: Session

    @classmethod
    def read(cls, symbol: str, as_of: datetime, db: Session):
        row = db.execute(text(f"Select symbol, name, title, asset_type FROM asset WHERE symbol='{symbol}'")).fetchone()
        if row is None:
            return None
        asset = cls.model_construct()
        asset.symbol = row[0]
        asset.name = row[1]
        asset.title = row[2]
        asset.asset_type = row[3]
        asset._db = db
        asset._as_of = as_of
        return asset

    @property
    def stock_data(self) -> DataFrame:
        return read_sql_query(
            f"""Select symbol, time, high, low, open, close, volume
            FROM ohlc WHERE time <= '{self._as_of}' AND symbol='{self.symbol}'""",
            self._db.bind,
        )


class Portfolio(models.finance.Portfolio):
    _execution: str
    _as_of: datetime
    _db: Session

    @classmethod
    def read(cls, execution: str, as_of: datetime, db: Session):
        row = db.execute(
            text(
                f"""Select id, cash, value
            FROM backtest_portfolio WHERE execution='{execution}' AND date='{as_of}'"""
            )
        ).fetchone()
        if row is None:
            return None
        portfolio = cls.model_construct()
        portfolio_id = row[0]
        portfolio.cash = row[1]
        portfolio.value = row[2]
        portfolio._execution = execution
        portfolio._as_of = as_of
        portfolio._db = db
        rows = db.execute(
            text(
                f"""Select symbol, amount, cost_basis
            FROM backtest_position WHERE portfolio_id='{portfolio_id}'"""
            )
        ).fetchall()
        portfolio.positions = [models.finance.Position(symbol=row[0], amount=row[1], cost_basis=row[2]) for row in rows]
        return portfolio

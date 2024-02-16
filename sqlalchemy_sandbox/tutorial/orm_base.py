from typing import Dict
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Row


def row_to_dict(row: Row) -> Dict:
    return row._asdict()


# pylint: disable=too-few-public-methods
class BaseModel(DeclarativeBase):
    def asdict(self) -> Dict:
        """https://stackoverflow.com/a/11884806/5538793"""
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    @classmethod
    def all_columns(cls):
        return cls.__table__.c

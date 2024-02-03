from typing import Dict
from sqlalchemy.orm import DeclarativeBase


# pylint: disable=too-few-public-methods
class BaseModel(DeclarativeBase):
    def asdict(self) -> Dict:
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

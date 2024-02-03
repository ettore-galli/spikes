from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from tutorial.orm_base import BaseModel


# pylint: disable=too-few-public-methods
class PhoneBookEntry(BaseModel):
    __tablename__ = "phone_book_entry"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    phone: Mapped[str] = mapped_column(String(30), nullable=True)

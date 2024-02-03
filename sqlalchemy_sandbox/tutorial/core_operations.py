"""
Working with data

https://docs.sqlalchemy.org/en/20/tutorial/data.html
"""


from typing import Optional

from sqlalchemy import insert
from sqlalchemy.engine.base import Connection, Engine
from sqlalchemy.engine.cursor import CursorResult

from tutorial.orm_models import BaseModel, PhoneBookEntry


def create_all_tables(engine: Engine):
    BaseModel.metadata.create_all(bind=engine)


def insert_phone_book_entry(
    connection: Connection, name: Optional[str], phone: Optional[str]
) -> CursorResult:
    return connection.execute(
        insert(PhoneBookEntry)
        .values(name=name, phone=phone)
        .returning(PhoneBookEntry.id)
    )

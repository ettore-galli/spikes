from sqlalchemy import insert
from tutorial.connection import create_db_engine
from tutorial.connection_base import Connections
from tutorial.table_objects_core import (
    phonebook,
    phonebook_entry_type,
    database_metadata,
)


def test_phonebook_entry_type_properties():
    assert [
        foreign_key.target_fullname for foreign_key in list(phonebook.foreign_keys)
    ] == ["phonebook_entry_type.entry_type_id"]


def test_phonebook_properties():
    assert [column.name for column in phonebook.primary_key.columns] == ["entry_id"]


def test_creation():
    engine = create_db_engine(Connections.SQLITE_IN_MEMORY.value)
    database_metadata.create_all(bind=engine)
    with engine.connect() as connection:
        connection.execute(
            insert(phonebook_entry_type).values([{"entry_type_id": 1, "type": "casa"}])
        )

from sqlalchemy import select
from sqlalchemy.engine.row import Row
from tutorial.orm_models import PhoneBookEntry
from tutorial.core_operations import create_all_tables, insert_phone_book_entry
from tutorial.connection_base import Connections
from tutorial.connection import create_db_engine


def test_insert_phone_book_entry():
    engine = create_db_engine(Connections.SQLITE_IN_MEMORY.value)
    create_all_tables(engine)

    with engine.connect() as connection:
        result_1 = insert_phone_book_entry(
            connection=connection, name="Ettore", phone="123123123"
        )
        assert result_1.all() == [(1,)]

        result_2 = insert_phone_book_entry(
            connection=connection, name="Ettore 2", phone="987987987"
        )
        assert result_2.all() == [(2,)]

        records = connection.execute(select(PhoneBookEntry)).all()

        assert records == [(1, "Ettore", "123123123"), (2, "Ettore 2", "987987987")]

        for item in connection.execute(select(PhoneBookEntry)):
            assert isinstance(item, Row)

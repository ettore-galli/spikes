from sqlalchemy import text
from tutorial.connection import create_db_engine
from tutorial.connection_base import Connections


def test_create_db_engine():
    engine = create_db_engine(Connections.SQLITE.value)
    assert engine is not None


def test_engine_basic_behaviour():
    """
    https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html
    """

    engine = create_db_engine(Connections.SQLITE_IN_MEMORY.value)
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 'test';"))
        records = result.all()
        assert records == [("test",)]

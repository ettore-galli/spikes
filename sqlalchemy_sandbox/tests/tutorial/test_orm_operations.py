from sqlalchemy import select, insert
from sqlalchemy.orm import Session

from tutorial.orm_models import PhoneBookEntry
from tutorial.core_operations import create_all_tables
from tutorial.connection_base import Connections
from tutorial.connection import create_db_engine


def prepare_dataset(session: Session):
    session.execute(insert(PhoneBookEntry).values(name="Ettore", phone="123123123"))
    session.execute(insert(PhoneBookEntry).values(name="Pippo", phone="111111"))
    session.execute(insert(PhoneBookEntry).values(name="PLuto", phone="222222"))


def test_insert_and_select():
    """
    https://docs.sqlalchemy.org/en/20/tutorial/data_select.html#the-select-sql-expression-construct
    https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Row
    """
    engine = create_db_engine(Connections.SQLITE_IN_MEMORY.value)

    create_all_tables(engine)

    with Session(engine) as session:
        session.execute(insert(PhoneBookEntry).values(name="Ettore", phone="123123123"))

        result = session.execute(select(PhoneBookEntry))
        record = [item.PhoneBookEntry for item in result.all()][0]
        assert record.asdict() == {"id": 1, "name": "Ettore", "phone": "123123123"}


def test_use_scalars_select():
    engine = create_db_engine(Connections.SQLITE_IN_MEMORY.value)

    create_all_tables(engine)

    with Session(engine) as session:
        prepare_dataset(session=session)

        result = session.scalars(select(PhoneBookEntry))
        data = [item.asdict() for item in result.all()]
        assert data == [
            {"id": 1, "name": "Ettore", "phone": "123123123"},
            {"id": 2, "name": "Pippo", "phone": "111111"},
            {"id": 3, "name": "PLuto", "phone": "222222"},
        ]


def test_use_labels():
    engine = create_db_engine(Connections.SQLITE_IN_MEMORY.value)

    create_all_tables(engine)

    with Session(engine) as session:
        prepare_dataset(session=session)

        result = session.execute(
            select(
                PhoneBookEntry.name,
                PhoneBookEntry.phone,
                (PhoneBookEntry.name + "/" + PhoneBookEntry.phone).label("short"),
            )
        )
        records = list(result.all())
        data = [item._asdict() for item in records]

        assert data == [
            {"name": "Ettore", "phone": "123123123", "short": "Ettore/123123123"},
            {"name": "Pippo", "phone": "111111", "short": "Pippo/111111"},
            {"name": "PLuto", "phone": "222222", "short": "PLuto/222222"},
        ]

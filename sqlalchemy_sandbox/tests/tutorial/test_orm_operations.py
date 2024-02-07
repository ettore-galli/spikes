from sqlalchemy import select, insert
from sqlalchemy.orm import Session, aliased
from sqlalchemy import func

from tutorial.orm_models import EntryType, PhoneBookEntry
from tutorial.core_operations import create_all_tables
from tutorial.connection_base import Connections
from tutorial.connection import create_db_engine


def prepare_dataset(session: Session):
    session.execute(insert(EntryType).values(id=100, description="Casa"))
    session.execute(insert(EntryType).values(id=200, description="Cell"))

    session.execute(
        insert(PhoneBookEntry).values(
            name="Ettore", phone="123123123", entry_type_id=200
        )
    )
    session.execute(
        insert(PhoneBookEntry).values(name="Pippo", phone="111111", entry_type_id=200)
    )
    session.execute(
        insert(PhoneBookEntry).values(name="PLuto", phone="222222", entry_type_id=100)
    )


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
        assert record.asdict() == {
            "entry_type_id": None,
            "id": 1,
            "name": "Ettore",
            "phone": "123123123",
        }


def test_use_scalars_select():
    engine = create_db_engine(Connections.SQLITE_IN_MEMORY.value)

    create_all_tables(engine)

    with Session(engine) as session:
        prepare_dataset(session=session)

        result = session.scalars(select(PhoneBookEntry))
        data = [item.asdict() for item in result.all()]
        assert data == [
            {"id": 1, "name": "Ettore", "phone": "123123123", "entry_type_id": 200},
            {"id": 2, "name": "Pippo", "phone": "111111", "entry_type_id": 200},
            {"id": 3, "name": "PLuto", "phone": "222222", "entry_type_id": 100},
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


def test_join():
    engine = create_db_engine(Connections.SQLITE_IN_MEMORY.value)

    create_all_tables(engine)

    with Session(engine) as session:
        prepare_dataset(session=session)

        result = session.execute(
            select(
                PhoneBookEntry.name,
                PhoneBookEntry.phone,
                EntryType.description.label("type"),
            )
            .select_from(PhoneBookEntry)
            .join(EntryType, PhoneBookEntry.entry_type_id == EntryType.id)
        )
        records = list(result.all())
        data = [item._asdict() for item in records]

        assert data == [
            {"name": "Ettore", "phone": "123123123", "type": "Cell"},
            {"name": "Pippo", "phone": "111111", "type": "Cell"},
            {"name": "PLuto", "phone": "222222", "type": "Casa"},
        ]


def test_groupby():
    engine = create_db_engine(Connections.SQLITE_IN_MEMORY.value)

    create_all_tables(engine)

    with Session(engine) as session:
        prepare_dataset(session=session)

        # pylint: disable=not-callable
        result = session.execute(
            select(EntryType.description.label("type"), func.count(PhoneBookEntry.id))
            .select_from(PhoneBookEntry)
            .join(EntryType, PhoneBookEntry.entry_type_id == EntryType.id)
            .group_by(EntryType.description)
            # Please note that .group_by("type") would work as well.
        )
        records = list(result.all())
        data = [item._asdict() for item in records]

        assert data == [{"type": "Casa", "count": 1}, {"type": "Cell", "count": 2}]


def test_subquery_cte():
    engine = create_db_engine(Connections.SQLITE_IN_MEMORY.value)

    create_all_tables(engine)

    with Session(engine) as session:
        prepare_dataset(session=session)

        # pylint: disable=not-callable
        count_subq_base = select(
            PhoneBookEntry.entry_type_id,
            func.count(PhoneBookEntry.id).label("ntypes"),
        ).group_by(PhoneBookEntry.entry_type_id)

        for count_subq in [count_subq_base.subquery(), count_subq_base.cte()]:
            result = session.execute(
                select(PhoneBookEntry.name, PhoneBookEntry.phone, count_subq.c.ntypes)
                .select_from(PhoneBookEntry)
                .join(
                    count_subq,
                    PhoneBookEntry.entry_type_id == count_subq.c.entry_type_id,
                )
            )
            records = list(result.all())
            data = [item._asdict() for item in records]

            assert data == [
                {"name": "Ettore", "phone": "123123123", "ntypes": 2},
                {"name": "Pippo", "phone": "111111", "ntypes": 2},
                {"name": "PLuto", "phone": "222222", "ntypes": 1},
            ]


def test_aliased_orm_subquery_cte():
    engine = create_db_engine(Connections.SQLITE_IN_MEMORY.value)

    create_all_tables(engine)

    with Session(engine) as session:
        prepare_dataset(session=session)

        # pylint: disable=not-callable
        subq = (
            select(
                PhoneBookEntry.entry_type_id,
                func.count(PhoneBookEntry.id).label("id"),
            )
            .group_by(PhoneBookEntry.entry_type_id)
            .subquery()
        )

        pbe_subq = aliased(
            PhoneBookEntry,
            alias=subq,
        )

        result = session.execute(
            select(
                PhoneBookEntry.name, PhoneBookEntry.phone, pbe_subq.id.label("n_per_id")
            )
            .select_from(PhoneBookEntry)
            .join(
                pbe_subq,
                PhoneBookEntry.entry_type_id == pbe_subq.entry_type_id,
            )
        )
        records = list(result.all())
        data = [item._asdict() for item in records]

        assert data == [
            {"name": "Ettore", "phone": "123123123", "n_per_id": 1},
            {"name": "Pippo", "phone": "111111", "n_per_id": 2},
            {"name": "PLuto", "phone": "222222", "n_per_id": 3},
        ]


def test_scalar_borderline_more_than_one_row():
    engine = create_db_engine(Connections.SQLITE_IN_MEMORY.value)

    create_all_tables(engine)

    with Session(engine) as session:
        prepare_dataset(session=session)

        query = (
            select(PhoneBookEntry.id)
            .order_by(PhoneBookEntry.id.desc())
            .scalar_subquery()
        )

        result = session.execute(select(query))
        records = list(result.all())

        assert records == [(3,)]

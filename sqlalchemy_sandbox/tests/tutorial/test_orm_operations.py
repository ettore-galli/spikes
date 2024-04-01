from sqlalchemy import select, insert, union
from sqlalchemy.orm import Session, aliased
from sqlalchemy import func, literal_column

from tutorial.orm_models import EntryType, PhoneBookEntry
from tutorial.core_operations import create_all_tables
from tutorial.connection_base import Connections
from tutorial.connection import create_db_engine


def prepare_simple_dataset(session: Session):
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


def prepare_long_dataset(session: Session, number_of_entries: int):
    session.execute(insert(EntryType).values(id=100, description="Casa"))
    session.execute(insert(EntryType).values(id=200, description="Cellulare"))
    session.execute(insert(EntryType).values(id=300, description="Ufficio"))

    def create_entry_type_id(entry_id: int) -> int:
        entry_type_id_fallback = 200 if entry_id % 5 == 0 else 300
        return 100 if entry_id % 7 == 0 else entry_type_id_fallback

    for entry_id in range(number_of_entries):
        session.execute(
            insert(PhoneBookEntry).values(
                id=entry_id,
                name=f"Name <{entry_id}>",
                phone=str(1000000 + entry_id),
                entry_type_id=create_entry_type_id(entry_id=entry_id),
            )
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
        prepare_simple_dataset(session=session)

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
        prepare_simple_dataset(session=session)

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
        prepare_simple_dataset(session=session)

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
        prepare_simple_dataset(session=session)

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
        prepare_simple_dataset(session=session)

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
        prepare_simple_dataset(session=session)

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
        prepare_simple_dataset(session=session)

        query = (
            select(PhoneBookEntry.id)
            .order_by(PhoneBookEntry.id.desc())
            .scalar_subquery()
        )

        result = session.execute(select(query))
        records = list(result.all())

        assert records == [(3,)]


def test_union():
    engine = create_db_engine(Connections.SQLITE_IN_MEMORY.value)

    create_all_tables(engine)

    with Session(engine) as session:
        prepare_simple_dataset(session=session)

        query_1 = select(PhoneBookEntry).where(PhoneBookEntry.id == 1)
        query_2 = select(PhoneBookEntry).where(PhoneBookEntry.id == 2)

        union_statement = union(query_1, query_2)
        result = session.execute(union_statement)

        records = list(result.all())

        assert records == [(1, "Ettore", "123123123", 200), (2, "Pippo", "111111", 200)]

        orm_result = session.execute(
            select(PhoneBookEntry).from_statement(union_statement)
        )
        orm_records = orm_result.all()
        assert isinstance(orm_records[0].PhoneBookEntry, PhoneBookEntry)


def test_select_single_columns():
    engine = create_db_engine(Connections.SQLITE_IN_MEMORY.value)

    create_all_tables(engine)

    with Session(engine) as session:
        prepare_long_dataset(session=session, number_of_entries=100)

        query = select(
            literal_column("'a-value'").label("'a_field'"),
            PhoneBookEntry.__table__,
            EntryType.__table__,
        ).where(PhoneBookEntry.entry_type_id == EntryType.id)

        result = session.execute(query)

        records = list(result.all())

        assert records[:3] == [
            ("a-value", 0, "Name <0>", "1000000", 100, 100, "Casa"),
            ("a-value", 1, "Name <1>", "1000001", 300, 300, "Ufficio"),
            ("a-value", 2, "Name <2>", "1000002", 300, 300, "Ufficio"),
        ]


def test_select_single_columns():
    engine = create_db_engine(Connections.SQLITE_IN_MEMORY.value)

    create_all_tables(engine)

    with Session(engine) as session:
        prepare_long_dataset(session=session, number_of_entries=100)

        query = select(
            literal_column("'a-value'").label("'a_field'"),
            PhoneBookEntry.__table__,
            EntryType.__table__,
        ).where(PhoneBookEntry.entry_type_id == EntryType.id)

        result = session.execute(query)

        records = list(result.all())

        assert records[:3] == [
            ("a-value", 0, "Name <0>", "1000000", 100, 100, "Casa"),
            ("a-value", 1, "Name <1>", "1000001", 300, 300, "Ufficio"),
            ("a-value", 2, "Name <2>", "1000002", 300, 300, "Ufficio"),
        ]
from connection import create_db_session
from models import Employee


def insert_data(session):
    for name in ["Ettore", "aaa", "bbb", "ccc"]:
        session.add(Employee(name=name))
    session.commit()


def query_data(session):
    for record in session.query(Employee).all():
        print(record.__dict__)


def main():
    with create_db_session() as session:
        insert_data(session=session)
        query_data(session=session)


if __name__ == "__main__":
    main()

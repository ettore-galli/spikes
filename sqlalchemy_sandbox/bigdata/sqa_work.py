from sqlalchemy import delete

from bigdata.connection import create_db_session
from bigdata.models import Employee, Department


def clear_data(session):
    session.execute(delete(Employee))
    session.execute(delete(Department))
    session.commit()


def insert_data(session):
    for dep in ["RD", "Mkt"]:
        session.add(Department(descr=dep))
    session.commit()

    for name in ["Ettore", "aaa", "bbb", "ccc"]:
        session.add(Employee(name=name, department_id=(1 if name == "Ettore" else 2)))
    session.commit()


def query_data(session):
    for dep in session.query(Department).all():
        print(f"========== {dep.id}: {dep.descr} ==========")

        for emp in dep.employees:
            print(f"* {emp.id}: {emp.name} ")


def main():
    with create_db_session() as session:
        clear_data(session=session)
        insert_data(session=session)
        query_data(session=session)


if __name__ == "__main__":
    main()

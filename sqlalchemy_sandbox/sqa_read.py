from sqlalchemy_sandbox.connection import create_db_session
from sqlalchemy_sandbox.models import Department


def query_data(session):
    for dep in session.query(Department).all():
        print(f"========== {dep.id}: {dep.descr} ==========")

        for emp in dep.employees:
            print(f"* {emp.id}: {emp.name} rep: {emp.department.descr} ")


def main():
    with create_db_session() as session:
        query_data(session=session)


if __name__ == "__main__":
    main()

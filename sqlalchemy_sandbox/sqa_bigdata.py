from sqlalchemy_sandbox.connection import create_db_session
from sqlalchemy_sandbox.models import Employee, Department
from sqlalchemy import delete, select
from sqlalchemy.sql.expression import Update, Insert

NUMBER_OF_NAMES = 100000


def clear_data(session):
    session.execute(delete(Employee))
    session.execute(delete(Department))
    session.commit()


def insert_data(session):
    for id, dep in [(1, "RD"), (2, "Mkt")]:
        session.add(Department(id=id, descr=dep))
    session.commit()

    for name in [f"Emp_{NUMBER_OF_NAMES + id }" for id in range(NUMBER_OF_NAMES)]:
        session.add(Employee(name=name, department_id=(1 if name == "Ettore" else 2)))
    session.commit()


def update_data(session):
    newdata = [
        (id, f"EMPLOYEE_OF_ID_{id}")
        for id in range(int(NUMBER_OF_NAMES / 2), int(NUMBER_OF_NAMES * 1.5))
    ]

    for data in newdata:
        name = f"Emp_{data[0] }"

        rows = session.execute(
            select(Employee).select_from(Employee).filter(Employee.name == name)
        )

        department_id = 1 + data[0] % 2

        row = rows.one_or_none()

        if row is not None:
            print("update", row[0].id, "dep=", department_id)
            session.execute(
                Update(
                    Employee,
                    whereclause=Employee.name == name,
                    values=dict(name=data[1], department_id=department_id),
                )
            )
        else:
            print("insert dep=", department_id)
            session.execute(
                Insert(
                    Employee,
                    values=dict(id=data[0], name=data[1], department_id=department_id),
                )
            )
    session.commit()


def main():
    with create_db_session() as session:
        from datetime import datetime

        t0 = datetime.now()
        clear_data(session=session)
        insert_data(session=session)
        update_data(session=session)
        delta = datetime.now() - t0
        print(delta)


if __name__ == "__main__":
    main()

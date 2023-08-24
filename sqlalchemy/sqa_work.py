from connection import create_db_session
from models import Employee


def main():
    with create_db_session() as session:
        print(session)
        for record in session.query(Employee).all():
            print(record)


if __name__ == "__main__":
    main()

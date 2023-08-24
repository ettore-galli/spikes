import sqlalchemy
from sqlalchemy import create_engine, Index
from sqlalchemy.orm import sessionmaker

from sqlalchemy_sandbox.models import Base, Employee


class DBSettings:
    url = "sqlite:///./db-sqlite/database.db"


class DBSettingsMySQL:
    url = "mysql+pymysql://root:password@localhost:3306/sandbox?charset=utf8mb4"


DB_SETTINGS = DBSettingsMySQL()


def create_db_engine(db_settings) -> sqlalchemy.engine.base.Engine:
    return create_engine(db_settings.url)


def create_tables(engine: sqlalchemy.engine.base.Engine):
    Base.metadata.create_all(engine)
    Index("employees_name", Employee.name).create(engine)


def initialize_database():
    create_tables(create_db_engine(DB_SETTINGS))


def build_db_session(engine: sqlalchemy.engine.base.Engine):
    Session = sessionmaker(engine)
    session = Session()

    return session


def create_db_session():
    return build_db_session(create_db_engine(DB_SETTINGS))

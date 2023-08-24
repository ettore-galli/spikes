import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base


class DBSettings:
    url = "sqlite:///./db/database.db"


def create_db_engine(db_settings: DBSettings) -> sqlalchemy.engine.base.Engine:
    return create_engine(db_settings.url)


def create_tables(engine: sqlalchemy.engine.base.Engine):
    Base.metadata.create_all(engine)


def initialize_database():
    create_tables(create_db_engine(DBSettings()))


def build_db_session(engine: sqlalchemy.engine.base.Engine):
    Session = sessionmaker(engine)
    session = Session()
    print(type(session))
    return session


def create_db_session():
    return build_db_session(create_db_engine(DBSettings()))

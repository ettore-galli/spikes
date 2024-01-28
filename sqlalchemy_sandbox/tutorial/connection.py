from sqlalchemy import create_engine


def create_connection(database: str):
    engine = create_engine(database)
    return engine

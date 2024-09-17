from sqlalchemy.orm import scoped_session
from sqlalchemy import insert

from multi_processing.models.data import Data


class DataRepo:
    def __init__(self, session: scoped_session) -> None:
        self.session: scoped_session = session

    def add_data(self, content: str) -> None:
        query = insert(Data).values(content=content)
        self.session.execute(query)
        self.session.commit()

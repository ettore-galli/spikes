# pylint: disable=too-few-public-methods
from enum import Enum


class Connections(Enum):
    SQLITE = "sqlite:///./db-sqlite/database.db"
    MYSQL = "mysql+pymysql://root:password@localhost:3306/sandbox?charset=utf8mb4"

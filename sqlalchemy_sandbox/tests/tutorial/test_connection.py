from tutorial.connection import create_connection
from tutorial.connection_base import Connections


def test_create_connection():
    connection = create_connection(Connections.SQLITE.value)
    assert connection is not None

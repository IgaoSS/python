# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304
#import pytest
from sqlalchemy.engine import Engine
from .connection import db_connection_handler

#@pytest.mark.skip(reason="Integração com o banco de dados")
def test_connect_to_db():
    assert db_connection_handler.get_engine() is None

    db_connection_handler.connect_to_db()
    db_engine = db_connection_handler.get_engine()

    assert db_engine is not None
    assert isinstance(db_engine, Engine)
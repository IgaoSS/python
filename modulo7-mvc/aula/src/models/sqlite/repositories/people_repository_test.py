# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321
from unittest import mock
from alchemy_mock.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.people import PeopleTable
from .people_repository import PeopleRepository

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                [mock.call.query(PeopleTable)],
                [
                    PeopleTable(first_name="test name", last_name="test last", age=50, pet_id=2)
                ]
            ]
        )

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

def test_insert_person():
    mock_connection = MockConnection()
    repo = PeopleRepository(mock_connection)
    repo.insert_person(first_name="Igor", last_name="Sousa", age=23, pet_id=3)

    mock_connection.session.add.assert_called_once()
    mock_connection.session.query.assert_not_called()
    mock_connection.session.filter.assert_not_called()

def test_get_person():
    mock_connection = MockConnection()
    repo = PeopleRepository(mock_connection)
    repo.get_person(1)

    mock_connection.session.query.assert_called_once_with(PeopleTable)

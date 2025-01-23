# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321
from unittest import mock
import pytest
from alchemy_mock.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable

from .pets_repository import PetsRepository


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PetsTable)], #query
                    [
                        PetsTable(name="dog", type="dog"),
                        PetsTable(name="cat", type="cat")
                    ] #resultado
                )
            ]
        )

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

class MockConnectionNoResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

def test_list_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    response = repo.list_pets()

    # Verifica se no list_pets foi chamado o método query() e all()
    # Verifica também se não foi chamado o método filter()
    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].name == "dog"

def test_delete_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    repo.delete_pets("burro")

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.filter.assert_called_once_with(PetsTable.name == "burro")
    mock_connection.session.delete.assert_called_once()

def test_list_pets_no_results():
    mock_connection = MockConnectionNoResult()
    repo = PetsRepository(mock_connection)
    response = repo.list_pets()

    # Como é disparado um side_effect assim que acessa o método query, ele lança a exceção
    # Sem executar o método all do list_pets
    # Portanto, o session.all precisa ser assert not called, pois ele não será chamado
    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    assert response == []

def test_delete_pets_error():
    mock_connection = MockConnectionNoResult()
    repo = PetsRepository(mock_connection)

    with pytest.raises(Exception):
        repo.delete_pets("petName")

    mock_connection.session.rollback.assert_called_once()
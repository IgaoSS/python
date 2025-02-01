# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321,E0401,E0611,W0104,C0301
from unittest import mock
from alchemy_mock.mocking import UnifiedAlchemyMagicMock
from ..entities.juridic_person import JuridicPersonTable
from .juridic_person_repository import JuridicPersonRepository

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(JuridicPersonTable)],
                    [
                        JuridicPersonTable(
                            nome_fantasia = "Empresa Teste LTDA",
                            idade = 23,
                            faturamento = 50000.00,
                            celular = "1111-2222",
                            categoria = "Categoria A",
                            saldo = 100000.00
                        )
                    ]
                )
            ]
        )

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

def test_list_juridic_persons():
    mock_connection = MockConnection()
    repo = JuridicPersonRepository(mock_connection)
    response = repo.list_juridic_persons()

    mock_connection.session.query.assert_called_once_with(JuridicPersonTable)
    mock_connection.session.query.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].nome_fantasia == "Empresa Teste LTDA"

def test_withdraw_money():
    mock_connection = MockConnection()
    repo = JuridicPersonRepository(mock_connection)
    response = repo.withdraw_money(1, 1000.00)

    assert response == 'Saque de R$ 1000.0 realizado com sucesso. Saldo atualizado: R$ 99000.0'

def test_check_balance():
    mock_connection = MockConnection()
    repo = JuridicPersonRepository(mock_connection)
    response = repo.check_balance(1)

    mock_connection.session.query.assert_called_once_with(JuridicPersonTable)
    mock_connection.session.query.assert_called_once()
    mock_connection.session.filter.assert_called_once()

    assert response == 100000.00

def test_view_statement():
    mock_connection = MockConnection()
    repo = JuridicPersonRepository(mock_connection)
    response = repo.view_statement(1)

    mock_connection.session.query.assert_called_once_with(JuridicPersonTable)
    mock_connection.session.query.assert_called_once()
    mock_connection.session.filter.assert_called_once()

    assert response == {'Nome Fantasia': 'Empresa Teste LTDA', 'Saldo': 100000.0, 'Categoria': 'Categoria A'}

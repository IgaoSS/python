# pylint: disable=C0103,C0301
from unittest.mock import Mock
from src.models.repositories.user_repository import UserRepository

class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock()
        self.fetchone = Mock()

class MockConnection:
    def __init__(self) -> None:
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()

def test_registry_user():
    username = "john"
    password = "senha123"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)
    repo.registry_user(username, password)
    cursor = mock_connection.cursor.return_value

    assert "INSERT INTO users (username, password, balance) VALUES (?, ?, ?)" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username, password, 0)

def test_edit_balance():
    user_id = 1
    balance = 5000.00

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)
    repo.edit_balance(user_id, balance)
    cursor = mock_connection.cursor.return_value

    assert "UPDATE users SET balance = ? WHERE id = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (balance, user_id)
    mock_connection.commit.assert_called_once()

def test_get_user_by_username():
    username = "meuUser"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)
    repo.get_user_by_username(username)
    cursor = mock_connection.cursor.return_value

    assert "SELECT id, username, password FROM users WHERE username = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username,)
    cursor.fetchone.assert_called_once()
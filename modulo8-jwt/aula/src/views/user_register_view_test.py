# pylint: disable=W0613,W0612
import pytest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.user_register_view import UserRegisterView

class MockController:
    def registry(self, username, password):
        return { "message": "anything" }

def test_handle_user_register():
    body = {
        "username": "MyUsername",
        "password": "MyPassword"
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    response = user_register_view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.body == {'data': {'message': 'anything'}}
    assert response.status_code == 201

def test_handle_user_register_with_validation_error():
    body = {
        "password": "MyPassword"
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    with pytest.raises(Exception):
        response = user_register_view.handle(request)

def test_handle_user_register_with_username_int():
    body = {
        "username": 1,
        "password": "MyPassword"
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    with pytest.raises(Exception):
        response = user_register_view.handle(request)

def test_handle_user_register_with_password_int():
    body = {
        "username": "MyUsername",
        "password": 1
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    with pytest.raises(Exception):
        response = user_register_view.handle(request)
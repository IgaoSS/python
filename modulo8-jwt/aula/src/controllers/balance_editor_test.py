# pylint: disable=C0103,W0621,C0121
from src.controllers.balance_editor import BalanceEditor

class MockUserRepository:
    def __init__(self) -> None:
        self.user_balance = {}

    def edit_balance(self, user_id: int, new_balance: float) -> None:
        self.user_balance["user_id"] = user_id
        self.user_balance["new_balance"] = new_balance

def test_edit():
    repository = MockUserRepository()
    controller = BalanceEditor(repository)

    user_id = 1
    new_balance = 1250.00

    response = controller.edit(user_id, new_balance)

    assert response["type"] == "User"
    assert response["count"] == 1
    assert response["new_balance"] == new_balance
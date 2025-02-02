# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321,W0719,W0613
#from src.models.sqlite.entities.natural_person import NaturalPersonTable
#from src.controllers.natural_person_statement_controller import NaturalPersonStatementController
from src.controllers.natural_person_withdraw_controller import NaturalPersonWithdrawController
from src.models.sqlite.repositories.natural_person_repository import NaturalPersonRepository
from src.models.sqlite.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

def test_view():
    repo = NaturalPersonRepository(db_connection_handler)
    #controller = NaturalPersonStatementController(repo)
    #response = controller.view_statement(4)
    controller = NaturalPersonWithdrawController(repo)
    data = {
        "person_id": 1,
        "quantify": 10
    }
    response = controller.withdraw_money(data)
    print(response)
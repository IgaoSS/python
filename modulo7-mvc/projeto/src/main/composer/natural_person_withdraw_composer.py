# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.natural_person_repository import NaturalPersonRepository
from src.controllers.natural_person_withdraw_controller import NaturalPersonWithdrawController
from src.views.natural_person_withdraw_view import NaturalPersonWithdrawView

def natural_person_withdraw_composer():
    model = NaturalPersonRepository(db_connection_handler)
    controller = NaturalPersonWithdrawController(model)
    view = NaturalPersonWithdrawView(controller)
    return view
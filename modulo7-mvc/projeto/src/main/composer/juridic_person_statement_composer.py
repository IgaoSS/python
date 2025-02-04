# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.juridic_person_repository import JuridicPersonRepository
from src.controllers.juridic_person_statement_controller import JuridicPersonStatementController
from src.views.juridic_person_statement_view import JuridicPersonStatementView

def juridic_person_statement_composer():
    model = JuridicPersonRepository(db_connection_handler)
    controller = JuridicPersonStatementController(model)
    view = JuridicPersonStatementView(controller)
    return view
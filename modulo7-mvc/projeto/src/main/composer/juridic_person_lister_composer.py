# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.juridic_person_repository import JuridicPersonRepository
from src.controllers.juridic_person_lister_controller import JuridicPersonListerController
from src.views.juridic_person_lister_view import JuridicPersonListerView

def juridic_person_lister_composer():
    model = JuridicPersonRepository(db_connection_handler)
    controller = JuridicPersonListerController(model)
    view = JuridicPersonListerView(controller)
    return view
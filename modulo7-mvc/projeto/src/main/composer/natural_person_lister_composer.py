# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.natural_person_repository import NaturalPersonRepository
from src.controllers.natural_person_lister_controller import NaturalPersonListerController
from src.views.natural_person_lister_view import NaturalPersonListerView

def natural_person_lister_composer():
    model = NaturalPersonRepository(db_connection_handler)
    controller = NaturalPersonListerController(model)
    view = NaturalPersonListerView(controller)
    return view
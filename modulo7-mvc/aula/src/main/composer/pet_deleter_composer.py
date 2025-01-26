# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.controllers.pet_deleter_controller import PetDeleterController
from src.views.pet_deleter_view import PetDeleterView

def pet_deleter_composer():
    model = PetsRepository(db_connection_handler)
    controller = PetDeleterController(model)
    view = PetDeleterView(controller)
    return view
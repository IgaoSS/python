# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321
from src.controllers.interfaces.pet_lister_controller import PetListerControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface

class PetListerView(ViewInterface):
    def __init__(self, controller: PetListerControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.list()
        return HttpResponse(status_code=200, body=body_response)
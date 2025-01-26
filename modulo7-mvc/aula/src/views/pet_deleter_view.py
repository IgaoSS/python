# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321
from src.controllers.interfaces.pet_deleter_controller import PetDeleterControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface

class PetDeleterView(ViewInterface):
    def __init__(self, controller: PetDeleterControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        name = http_request.param["name"]
        self.__controller.delete(name)
        return HttpResponse(status_code=204)
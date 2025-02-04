# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0301,C0304,C0321
from src.controllers.interfaces.juridic_person_lister_controller import JuridicPersonListerControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface

class JuridicPersonListerView(ViewInterface):
    def __init__(self, controller: JuridicPersonListerControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.list_persons()
        return HttpResponse(status_code=200, body=body_response)
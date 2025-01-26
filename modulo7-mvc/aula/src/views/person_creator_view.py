# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321
from src.controllers.interfaces.person_creator_controller import PersonCreatorControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface

class PersonCreatorView(ViewInterface):
    def __init__(self, controller: PersonCreatorControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_info = http_request.body
        body_response = self.__controller.create(person_info)
        return HttpResponse(status_code=201, body=body_response)
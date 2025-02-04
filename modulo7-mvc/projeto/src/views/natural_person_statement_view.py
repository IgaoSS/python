# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0301,C0304,C0321
from src.controllers.interfaces.natural_person_statement_controller import NaturalPersonStatementControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface

class NaturalPersonStatementView(ViewInterface):
    def __init__(self, controller: NaturalPersonStatementControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_id = http_request.param["person_id"]
        body_response = self.__controller.view_statement(person_id)
        return HttpResponse(status_code=200, body=body_response)
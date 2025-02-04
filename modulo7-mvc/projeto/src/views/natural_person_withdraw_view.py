# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0301,C0304,C0321
from src.controllers.interfaces.natural_person_withdraw_controller import NaturalPersonWithdrawControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface

class NaturalPersonWithdrawView(ViewInterface):
    def __init__(self, controller: NaturalPersonWithdrawControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        withdraw_info = http_request.body
        body_response = self.__controller.withdraw_money(withdraw_info)
        return HttpResponse(status_code=200, body=body_response)
# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321,W0719,C0301,R0903
from typing import Dict
from src.models.sqlite.interfaces.juridic_person_repository import JuridicPersonRepositoryInterface
from src.controllers.interfaces.juridic_person_withdraw_controller import JuridicPersonWithdrawControllerInterface

class JuridicPersonWithdrawController(JuridicPersonWithdrawControllerInterface):
    def __init__(self, juridic_person_repository: JuridicPersonRepositoryInterface):
        self.__juridic_person_repository = juridic_person_repository

    def withdraw_money(self, withdraw_info: Dict) -> Dict:
        person_id = withdraw_info["person_id"]
        quantify = withdraw_info["quantify"]

        withdraw = self.__execute_withdraw(person_id, quantify)
        response = self.__format_response(withdraw)
        return response

    def __execute_withdraw(self, person_id: int, quantify: float) -> str:
        response = self.__juridic_person_repository.withdraw_money(person_id, quantify)
        return response

    def __format_response(self, message: str) -> Dict:
        return {
            "data": {
                "type": "Juridic Person",
                "count": 1,
                "attributes": {
                    "message": message
                }
            }
        }
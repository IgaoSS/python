# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321,W0719,C0301,R0913,R0917
from typing import Dict
from src.models.sqlite.interfaces.juridic_person_repository import JuridicPersonRepositoryInterface
from src.controllers.interfaces.juridic_person_creator_controller import JuridicPersonCreatorControllerInterface

class JuridicPersonCreatorController(JuridicPersonCreatorControllerInterface):
    def __init__(self, juridic_person_repository: JuridicPersonRepositoryInterface):
        self.__juridic_person_repository = juridic_person_repository

    def create_user(self, person_info: Dict) -> Dict:
        nome_fantasia = ["nome_fantasia"]
        idade = ["idade"]
        celular = ["celular"]
        email_corporativo = ["email_corporativo"]
        faturamento = ["faturamento"]
        categoria = ["categoria"]
        saldo = ["saldo"]

        self.__insert_person_in_db(nome_fantasia, idade, celular, email_corporativo, faturamento, categoria, saldo)
        formatted_response = self.__format_response(person_info)
        return formatted_response

    def __insert_person_in_db(self, nome_fantasia: str, idade: int, celular: str, email_corporativo: str, faturamento: float, categoria: str, saldo: float) -> None:
        self.__juridic_person_repository.insert_juridic_person(nome_fantasia, idade, celular, email_corporativo, faturamento, categoria, saldo)

    def __format_response(self, person_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Juridic Person",
                "count": 1,
                "attributes": person_info
            }
        }
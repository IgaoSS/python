# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321,W0719,C0301,R0913,R0917
from typing import Dict
import re
from src.models.sqlite.interfaces.natural_person_repository import NaturalPersonRepositoryInterface
from src.controllers.interfaces.natural_person_creator_controller import NaturalPersonCreatorControllerInterface

class NaturalPersonCreatorController(NaturalPersonCreatorControllerInterface):
    def __init__(self, natural_person_repository: NaturalPersonRepositoryInterface):
        self.__natural_person_repository = natural_person_repository

    def create_user(self, person_info: Dict) -> Dict:
        nome_completo = person_info["nome_completo"]
        renda_mensal = person_info["renda_mensal"]
        idade = person_info["idade"]
        celular = person_info["celular"]
        email = person_info["email"]
        categoria = person_info["categoria"]
        saldo = person_info["saldo"]

        self.__validate_name(nome_completo)
        self.__insert_person_in_db(nome_completo, renda_mensal, idade, celular, email, categoria, saldo)
        formatted_response = self.__format_response(person_info)
        return formatted_response

    def __validate_name(self, nome_completo: str) -> None:
        non_valid_characters = re.compile(r'[a-zA-Z\s]')

        if non_valid_characters.search(nome_completo):
            raise ValueError("Nome da pessoa inválido!")

    def __insert_person_in_db(self, nome: str, renda: float, idade: int, celular: str, email: str, categoria: str, saldo: float) -> None:
        self.__natural_person_repository.insert_natural_person(nome, renda, idade, celular, email, categoria, saldo)

    def __format_response(self, person_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Natural Person",
                "count": 1,
                "attributes": person_info
            }
        }
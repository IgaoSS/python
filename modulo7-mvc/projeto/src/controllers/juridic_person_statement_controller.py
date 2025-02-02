# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321,W0719,C0301,R0903
from typing import Dict
from src.models.sqlite.entities.juridic_person import JuridicPersonTable
from src.models.sqlite.interfaces.juridic_person_repository import JuridicPersonRepositoryInterface
from src.controllers.interfaces.juridic_person_statement_controller import JuridicPersonStatementControllerInterface

class JuridicPersonStatementController(JuridicPersonStatementControllerInterface):
    def __init__(self, juridic_person_repository: JuridicPersonRepositoryInterface):
        self.__juridic_person_repository = juridic_person_repository

    def view_statement(self, person_id: int) -> Dict:
        person = self.__find_statement_in_db(person_id)
        response = self.__format_response(person)
        return response

    def __find_statement_in_db(self, person_id: int) -> JuridicPersonTable:
        person = self.__juridic_person_repository.view_statement(person_id)

        if not person:
            raise ValueError("Person not found")

        return person

    def __format_response(self, person: Dict) -> Dict:
        return {
            "data": {
                "type": "Natural Person",
                "count": 1,
                "attributes": person
            }
        }
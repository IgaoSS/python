# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321,W0719,C0301,R0903
from typing import Dict
from src.models.sqlite.entities.natural_person import NaturalPersonTable
from src.models.sqlite.interfaces.natural_person_repository import NaturalPersonRepositoryInterface
from src.controllers.interfaces.natural_person_statement_controller import NaturalPersonStatementControllerInterface

class NaturalPersonStatementController(NaturalPersonStatementControllerInterface):
    def __init__(self, natural_person_repository: NaturalPersonRepositoryInterface):
        self.__natural_person_repository = natural_person_repository

    def view_statement(self, person_id: int) -> Dict:
        person = self.__find_statement_in_db(person_id)
        response = self.__format_response(person)
        return response

    def __find_statement_in_db(self, person_id: int) -> NaturalPersonTable:
        person = self.__natural_person_repository.view_statement(person_id)

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
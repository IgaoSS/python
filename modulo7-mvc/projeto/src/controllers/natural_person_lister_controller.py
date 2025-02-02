# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321,W0719,C0301
from typing import List, Dict
from src.models.sqlite.entities.natural_person import NaturalPersonTable
from src.models.sqlite.interfaces.natural_person_repository import NaturalPersonRepositoryInterface
from src.controllers.interfaces.natural_person_lister_controller import NaturalPersonListerControllerInterface

class NaturalPersonListerController(NaturalPersonListerControllerInterface):
    def __init__(self, natural_person_repository: NaturalPersonRepositoryInterface):
        self.__natural_person_repository = natural_person_repository

    def list_persons(self) -> Dict:
        persons = self.__get_natural_persons_in_db()
        response = self.__format_response(persons)
        return response

    def __get_natural_persons_in_db(self) -> List[NaturalPersonTable]:
        persons = self.__natural_person_repository.list_natural_persons()
        return persons

    def __format_response(self, persons: List[NaturalPersonTable]) -> Dict:
        formatted_persons = []
        for person in persons:
            formatted_persons.append({
                "nome_completo": person.nome_completo,
                "idade": person.idade,
                "celular": person.celular,
                "email": person.email,
                "saldo": person.saldo
            })

        return {
            "data": {
                "type": "Natural Person",
                "count": len(formatted_persons),
                "attributes": formatted_persons
            }
        }
# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0301,E0401,E0611,R0913,R0917,R0801
from typing import List, Dict
from src.models.sqlite.entities.juridic_person import JuridicPersonTable
from src.models.sqlite.interfaces.juridic_person_repository import JuridicPersonRepositoryInterface
from src.controllers.interfaces.juridic_person_lister_controller import JuridicPersonListerControllerInterface

class JuridicPersonListerController(JuridicPersonListerControllerInterface):
    def __init__(self, juridic_person_repository: JuridicPersonRepositoryInterface):
        self.__juridic_person_repository = juridic_person_repository

    def list_persons(self) -> Dict:
        persons = self.__get_juridic_persons_in_db()
        response = self.__format_response(persons)
        return response

    def __get_juridic_persons_in_db(self) -> List[JuridicPersonTable]:
        persons = self.__juridic_person_repository.list_juridic_persons()
        return persons

    def __format_response(self, persons: List[JuridicPersonTable]) -> Dict:
        formatted_persons = []
        for person in persons:
            formatted_persons.append({
                "nome_fantasia": person.nome_fantasia,
                "email_corporativo": person.email_corporativo,
                "celular": person.celular,
                "saldo": person.saldo,
                "teste": person.categoria
            })

        return {
            "data": {
                "type": "Juridic Person",
                "count": len(formatted_persons),
                "attributes": formatted_persons
            }
        }
# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321, W0719
from typing import Dict
import re
from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
from src.controllers.interfaces.person_creator_controller import PersonCreatorControllerInterface

class PersonCreatorController(PersonCreatorControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface):
        self.__people_repository = people_repository

    def create(self, person_info: Dict) -> Dict:
        first_name = person_info["first_name"]
        last_name = person_info["last_name"]
        age = person_info["age"]
        pet_id = person_info["pet_id"]

        self.__validate_first_and_last_name(first_name, last_name)
        self.__insert_person_in_db(first_name, last_name, age, pet_id)
        formatted_response = self.__format_response(person_info)
        return formatted_response

    def __validate_first_and_last_name(self, first_name: str, last_name: str) -> None:
        # Regex para caracteres que não são letras
        non_valid_characters = re.compile(r'[^a-zA-Z]')

        if non_valid_characters.search(first_name) or non_valid_characters.search(last_name):
            raise HttpBadRequestError("Nome da pessoa inválido!")

    def __insert_person_in_db(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        self.__people_repository.insert_person(first_name, last_name, age, pet_id)

    def __format_response(self, person_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": person_info
            }
        }

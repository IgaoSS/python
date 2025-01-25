# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321, W0719
import pytest
from src.controllers.person_creator_controller import PersonCreatorController

class MockPeopleRepository:
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int):
        pass

def test_create():
    person_infos = {
        "first_name": "John",
        "last_name": "Cena",
        "age": 30,
        "pet_id": 1
    }
    controller = PersonCreatorController(MockPeopleRepository())
    response = controller.create(person_infos)

    assert response["data"]["type"] == "Person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_infos

def test_create_error():
    person_infos = {
        "first_name": "John123",
        "last_name": "Cena 15",
        "age": 30,
        "pet_id": 1
    }
    controller = PersonCreatorController(MockPeopleRepository())
    with pytest.raises(Exception):
        controller.create(person_infos)
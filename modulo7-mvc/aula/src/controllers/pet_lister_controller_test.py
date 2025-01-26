# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321
from src.models.sqlite.entities.pets import PetsTable
from src.controllers.pet_lister_controller import PetListerController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="Fido", type="Cat", id=1),
            PetsTable(name="Bolt", type="Dog", id=2),
        ]

def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    expected_response = {
         "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                {"name": "Fido", "type": "Cat", "id": 1},
                {"name": "Bolt", "type": "Dog", "id": 2}
            ]
        }
    }

    assert response == expected_response
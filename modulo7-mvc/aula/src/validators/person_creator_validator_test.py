# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321,W0707
from .person_creator_validator import person_creator_validator

class MockRequest:
    def __init__(self, body) -> None:
        self.body = body

def test_person_creator_validator():
    request = MockRequest({
        "first_name": "John",
        "last_name": "Doe",
        "age": 32,
        "pet_id": 9
    })

    person_creator_validator(request)
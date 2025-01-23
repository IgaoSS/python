# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304
import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository

# db_connection_handler.connect_to_db()

# Esse é um teste de integração do sistema, apenas para verificar o retorno dos dados vindo do banco
# Não é um teste unitário
@pytest.mark.skip(reason="Interação com o banco de dados")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print(response)

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_delete_pet():
    name = 'belinha'
    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(name)

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_insert_person():
    first_name = "test name"
    last_name = "test last"
    age = 50
    pet_id = 2

    repo = PeopleRepository(db_connection_handler)
    repo.insert_person(first_name, last_name, age, pet_id)

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_get_person():
    person_id = 1

    repo = PeopleRepository(db_connection_handler)
    response = repo.get_person(person_id)
    print()
    print(response)
    print(response.pet_name)
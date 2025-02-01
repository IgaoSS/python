# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0301
import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .juridic_person_repository import JuridicPersonRepository
from .natural_person_repository import NaturalPersonRepository

db_connection_handler.connect_to_db()

# TESTES DE INTEGRAÇÃO COM O BANCO DE DADOS

# TESTES DO REPOSITÓRIO DE PESSOA FÍSICA
@pytest.mark.skip(reason="Interação com o banco de dados")
def test_list_natural_persons():
    repo = NaturalPersonRepository(db_connection_handler)
    response = repo.list_natural_persons()
    print(response)

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_check_balance_natural_person():
    repo = NaturalPersonRepository(db_connection_handler)
    response = repo.check_balance(1)
    print(response)

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_insert_natural_person():
    nome_completo = "Igor Sousa"
    idade = 23
    renda_mensal = 5000.00
    celular = "1111-2222"
    email = "igor@teste.com"
    categoria = "Categoria A"
    saldo = 10000.00

    repo = NaturalPersonRepository(db_connection_handler)
    repo.insert_natural_person(nome_completo, renda_mensal, idade, celular, email, categoria, saldo)

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_withdraw_money_natural_person():
    repo = NaturalPersonRepository(db_connection_handler)
    response = repo.withdraw_money(1, 100)
    print(response)

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_view_statement_natural_person():
    repo = NaturalPersonRepository(db_connection_handler)
    response = repo.view_statement(1)
    print(response)

# TESTES DO REPOSITÓRIO DE PESSOA JURÍDICA
@pytest.mark.skip(reason="Interação com o banco de dados")
def test_list_juridic_persons():
    repo = JuridicPersonRepository(db_connection_handler)
    response = repo.list_juridic_persons()
    print()
    print(response)

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_check_balance_juridic_person():
    repo = JuridicPersonRepository(db_connection_handler)
    response = repo.check_balance(1)
    print()
    print(response)

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_insert_juridic_person():
    nome_fantasia = "Teste Jurídica"
    idade = 20
    celular = "4002-8922"
    email_corporativo = "teste@juridica.br"
    faturamento = 200000.00
    categoria = "Categoria D"
    saldo = 534000.00

    repo = JuridicPersonRepository(db_connection_handler)
    repo.insert_juridic_person(nome_fantasia, idade, celular, email_corporativo, faturamento, categoria, saldo)

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_withdraw_money_juridic_person():
    repo = JuridicPersonRepository(db_connection_handler)
    response = repo.withdraw_money(1, 1000)
    print()
    print(response)

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_view_statement_juridic_person():
    repo = JuridicPersonRepository(db_connection_handler)
    response = repo.view_statement(1)
    print(response)
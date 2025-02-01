# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0301,E0401,E0611,R0913,R0917,R0801
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.natural_person import NaturalPersonTable
from src.models.sqlite.interfaces.client_repository import ClientRepositoryInterface

class NaturalPersonRepository(ClientRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_natural_person(self, nome_completo: str, renda_mensal: float, idade: int, celular: str, email: str, categoria: str, saldo: float) -> None:
        with self.__db_connection as database:
            try:
                person_data = NaturalPersonTable(
                    nome_completo=nome_completo,
                    renda_mensal=renda_mensal,
                    idade=idade,
                    celular=celular,
                    email=email,
                    categoria=categoria,
                    saldo=saldo
                )
                database.session.add(person_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def list_natural_persons(self) -> List[NaturalPersonTable]:
        with self.__db_connection as database:
            try:
                natural_persons = database.session.query(NaturalPersonTable).all()
                return natural_persons
            except NoResultFound:
                return []

    def withdraw_money(self, person_id, quantify):
        try:
            daily_limit = 2000.00

            balance = self.check_balance(person_id)

            if quantify > daily_limit:
                return "ERRO: Saque ultrapassa o limite permitido!"

            if quantify > balance:
                return "ERRO: Saldo não disponível para saque!"

            new_balance = balance - quantify
            self.update_balance(person_id, new_balance)
            return f"Saque de R$ {quantify} realizado com sucesso. Saldo atualizado: R$ {new_balance}"

        except Exception as exception:
            raise exception

    def check_balance(self, person_id) -> NaturalPersonTable:
        with self.__db_connection as database:
            try:
                result = (
                    database.session
                        .query(NaturalPersonTable)
                        .filter(NaturalPersonTable.id == person_id)
                        .one()
                )
                return result.saldo
            except NoResultFound:
                return None

    def update_balance(self, person_id, new_balance):
        with self.__db_connection as database:
            try:
                result = (
                    database.session
                    .query(NaturalPersonTable)
                    .filter(NaturalPersonTable.id == person_id)
                    .first()
                )
                result.saldo = new_balance
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def view_statement(self, person_id):
        with self.__db_connection as database:
            try:
                person = (
                    database.session
                    .query(NaturalPersonTable)
                    .filter(NaturalPersonTable.id == person_id)
                    .first()
                )

                return {
                    "Nome": person.nome_completo,
                    "Saldo": person.saldo,
                    "Categoria": person.categoria,
                }
            except NoResultFound:
                return []
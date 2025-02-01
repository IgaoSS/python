# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0301,E0401,E0611,R0913,R0917
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.natural_person import NaturalPersonTable
# Implementar a interface

class NaturalPersonRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_natural_person(self, nome_completo: str, renda_mensal: float, idade: int, celular: str, categoria: str, saldo: float) -> None:
        with self.__db_connection as database:
            try:
                person_data = NaturalPersonTable(
                    nome_completo=nome_completo,
                    renda_mensal=renda_mensal,
                    idade=idade,
                    celular=celular,
                    categoria=categoria,
                    saldo=saldo
                )
                database.session.add(person_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def list_natural_people(self) -> List[NaturalPersonTable]:
        with self.__db_connection as database:
            try:
                natural_people = database.session.query(NaturalPersonTable).all()
                return natural_people
            except NoResultFound:
                return []

    def withdraw_money(self, natural_person_id, quantify):
        try:
            daily_limit = 2000.00

            saldo = self.check_balance(natural_person_id)

            if quantify > daily_limit:
                return "ERRO: Saque ultrapassa o limite permitido!"

            if quantify > saldo:
                return "ERRO: Saldo não disponível para saque!"

            new_balance = saldo - quantify
            self.update_balance(natural_person_id, new_balance)
            return f"Saque de R$ {quantify} realizado com sucesso. Saldo atualizado: R$ {new_balance}"

        except Exception as exception:
            raise exception

    def check_balance(self, natural_person_id) -> NaturalPersonTable:
        with self.__db_connection as database:
            try:
                result = (
                    database.session
                        .query(NaturalPersonTable)
                        .filter(NaturalPersonTable.id == natural_person_id)
                        .one()
                )
                return result.saldo
            except NoResultFound:
                return None

    def update_balance(self, natural_person_id, new_balance):
        with self.__db_connection as database:
            try:
                result = (
                    database.session
                    .query(NaturalPersonTable)
                    .filter(NaturalPersonTable.id == natural_person_id)
                    .first()
                )
                result.saldo = new_balance
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def view_statement(self, natural_person_id):
        with self.__db_connection as database:
            try:
                person = (
                    database.session
                    .query(NaturalPersonTable)
                    .filter(NaturalPersonTable.id == natural_person_id)
                    .first()
                )

                return {
                    "Nome": person.nome_completo,
                    "Saldo": person.saldo,
                    "Categoria": person.categoria,
                }
            except NoResultFound:
                return []
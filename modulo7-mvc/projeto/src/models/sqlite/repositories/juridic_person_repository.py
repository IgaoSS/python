# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0301,E0401,E0611,R0913,R0917,R0801
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.juridic_person import JuridicPersonTable
from src.models.sqlite.interfaces.client_repository import ClientRepositoryInterface

class JuridicPersonRepository(ClientRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_juridic_person(self, nome_fantasia: str, idade: int, celular: str, email_corporativo: str, faturamento: float, categoria: str, saldo: float) -> None:
        with self.__db_connection as database:
            try:
                juridic_data = JuridicPersonTable(
                    nome_fantasia=nome_fantasia,
                    idade=idade,
                    celular=celular,
                    email_corporativo=email_corporativo,
                    faturamento=faturamento,
                    categoria=categoria,
                    saldo=saldo
                )
                database.session.add(juridic_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def list_juridic_persons(self) -> List[JuridicPersonTable]:
        with self.__db_connection as database:
            try:
                juridic_persons = database.session.query(JuridicPersonTable).all()
                return juridic_persons
            except NoResultFound:
                return []

    def withdraw_money(self, person_id: int, quantify: float):
        try:
            daily_limit = 5000.00
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

    def check_balance(self, person_id: int):
        with self.__db_connection as database:
            try:
                result = (
                    database.session
                    .query(JuridicPersonTable)
                    .filter(JuridicPersonTable.id == person_id)
                    .first()
                )
                return result.saldo
            except NoResultFound:
                return None

    def update_balance(self, person_id: int, new_balance: float) -> None:
        with self.__db_connection as database:
            try:
                result = (
                    database.session
                    .query(JuridicPersonTable)
                    .filter(JuridicPersonTable.id == person_id)
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
                result = (
                    database.session
                    .query(JuridicPersonTable)
                    .filter(JuridicPersonTable.id == person_id)
                    .first()
                )

                return {
                    "Nome Fantasia": result.nome_fantasia,
                    "Saldo": result.saldo,
                    "Categoria": result.categoria
                }
            except NoResultFound:
                return []
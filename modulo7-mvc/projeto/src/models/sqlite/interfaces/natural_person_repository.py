# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0301,E0401,E0611,R0913,R0917,R0801
from typing import List
from abc import ABC, abstractmethod
from src.models.sqlite.entities.natural_person import NaturalPersonTable

class NaturalPersonRepositoryInterface(ABC):
    @abstractmethod
    def insert_natural_person(self, nome_completo: str, renda_mensal: float, idade: int, celular: str, email: str, categoria: str, saldo: float) -> None:
        pass

    @abstractmethod
    def list_natural_persons(self) -> List[NaturalPersonTable]:
        pass

    @abstractmethod
    def withdraw_money(self, person_id, quantify):
        pass

    @abstractmethod
    def check_balance(self, person_id):
        pass

    @abstractmethod
    def update_balance(self, person_id, new_balance):
        pass

    @abstractmethod
    def view_statement(self, person_id):
        pass
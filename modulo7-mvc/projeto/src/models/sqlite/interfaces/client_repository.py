# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0301,E0401,E0611,R0913,R0917
from abc import ABC, abstractmethod

class ClientRepositoryInterface(ABC):
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
# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321
from typing import List
from abc import ABC, abstractmethod
from src.models.sqlite.entities.pets import PetsTable

class PetsRepositoryInterface(ABC):
    @abstractmethod
    def list_pets(self) -> List[PetsTable]:
        pass

    @abstractmethod
    def delete_pets(self, name: str) -> None:
        pass
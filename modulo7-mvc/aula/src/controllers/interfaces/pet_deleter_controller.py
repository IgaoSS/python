# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321
from abc import ABC, abstractmethod

class PetDeleterControllerInterface(ABC):
    @abstractmethod
    def delete(self, name: str) -> None:
        pass
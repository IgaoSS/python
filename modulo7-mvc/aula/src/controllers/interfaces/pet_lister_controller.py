# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321
from typing import Dict
from abc import ABC, abstractmethod

class PetListerControllerInterface(ABC):
    @abstractmethod
    def list(self) -> Dict:
        pass
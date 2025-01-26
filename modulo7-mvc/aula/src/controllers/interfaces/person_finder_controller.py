# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321,W0719
from typing import Dict
from abc import ABC, abstractmethod

class PersonFinderControllerInterface(ABC):
    @abstractmethod
    def find(self, person_id: int) -> Dict:
        pass
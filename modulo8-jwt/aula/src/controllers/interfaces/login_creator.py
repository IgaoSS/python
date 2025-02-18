# pylint: disable=W0719,C0321,W0719
from typing import Dict
from abc import ABC, abstractmethod

class LoginCreatorInterface(ABC):
    @abstractmethod
    def create(self, username: str, password: str) -> Dict:
        pass
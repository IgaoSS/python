# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321
from typing import Dict

class HttpRequest:
    def __init__(self, body: Dict = None, param: Dict = None) -> None:
        self.body = body
        self.param = param

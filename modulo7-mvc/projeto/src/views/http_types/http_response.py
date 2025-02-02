# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321
from typing import Dict

class HttpResponse:
    def __init__(self, status_code: int, body: Dict = None) -> None:
        self.status_code = status_code
        self.body = body
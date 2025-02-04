# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321
class HttpBadRequestError(Exception):
    def __init__(self, message: str) -> None:
        self.status_code = 400
        self.name = "BadRequest"
        self.message = message
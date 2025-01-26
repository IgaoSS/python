# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321,W0707
from pydantic import BaseModel, constr, ValidationError
from src.views.http_types.http_request import HttpRequest
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def person_creator_validator(http_request: HttpRequest) -> None:
    class BodyData(BaseModel):
        first_name: constr(min_length=1) # type: ignore
        last_name: constr(min_length=1) # type: ignore
        age: int
        pet_id: int

    try:
        BodyData(**http_request.body)
        # Adicionar o ** na frente do request é para desempacotar o body
        # Seria mesma coisa que:
        # BodyData(first_name="Igor", last_name="Sousa", age="23", pet_id=2)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
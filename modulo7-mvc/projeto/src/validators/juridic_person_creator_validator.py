# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321,W0707
from pydantic import BaseModel, constr, ValidationError
from src.views.http_types.http_request import HttpRequest
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def juridic_person_creator_validator(http_request: HttpRequest) -> None:
    class BodyData(BaseModel):
        nome_fantasia: constr(min_length=1) # type: ignore
        idade: int
        email_corporativo: constr(min_length=1) # type: ignore
        faturamento: float
        celular: constr(min_length=1) # type: ignore
        categoria: constr(min_length=1) # type: ignore
        saldo: float

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0321
from src.views.http_types.http_response import HttpResponse
from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.errors.error_types.http_not_found import HttpNotFoundError
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpBadRequestError, HttpNotFoundError, HttpUnprocessableEntityError)):
        return HttpResponse(
            status_code = error.status_code,
            body = {
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Internal Server Error",
                "detail": str(error)
            }]
        }
    )
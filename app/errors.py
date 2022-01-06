import json
from http import HTTPStatus

from starlette.responses import Response
from app.exceptions import (
    PayloadValidationError,
    PayloadDecodeError,
    RequestError,
)


class Error:
    def __init__(self, status, detail=None):
        self.status = status
        self.detail = detail
        self.reason = HTTPStatus(self.status).phrase

    @property
    def __dict__(self):
        return dict(code=self.status, reason=self.reason, message=self.detail)

    @property
    def response(self):
        return Response(
            content=json.dumps(self.__dict__, indent=4), status_code=self.status
        )


async def on_error(_, exc):
    status = 500
    detail = None

    if issubclass(exc.__class__, RequestError):
        detail = exc.detail
        if isinstance(exc, PayloadValidationError):
            status = 422
        elif isinstance(exc, PayloadDecodeError):
            status = 400
            detail = str(detail)

    return Error(status, detail).response

from abc import abstractmethod, ABC
from json.decoder import JSONDecodeError
from typing import Type, Any, Tuple

from starlette.responses import Response
from sqlalchemy.engine import ScalarResult
from marshmallow.schema import Schema, EXCLUDE
from marshmallow.exceptions import ValidationError
from app.exceptions import (
    PayloadValidationError,
    PayloadDecodeError,
)


class Controller(ABC):
    @classmethod
    def init(cls, app):
        cls.app = app
        return cls()

    @abstractmethod
    def routes_make(self) -> Tuple[str, list]:
        return "", []

    @staticmethod
    def deserialize(data: Any, schema: Type[Schema]):
        try:
            return schema(unknown=EXCLUDE).loads(data.decode())
        except ValidationError as e:
            raise PayloadValidationError(e.messages)
        except JSONDecodeError as e:
            raise PayloadDecodeError(e)

    @staticmethod
    def serialize(data: Any, schema: Type[Schema], many: bool):
        return schema(many=many).dumps(data, indent=4)

    def json_response(self, data, status, schema=None):
        content = (
            self.serialize(data, schema, many=isinstance(data, ScalarResult))
            if schema
            else data
        )
        return Response(content, status_code=status, media_type="application/json")

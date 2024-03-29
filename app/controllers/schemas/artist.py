from marshmallow import Schema, validate
from marshmallow.fields import Integer, String

from app.database.tables import ArtistRole


class ArtistSchema(Schema):
    id = Integer(required=True)
    version = String(
        validate=validate.OneOf([a.name for a in ArtistRole]), required=True
    )
    name = String(required=True)

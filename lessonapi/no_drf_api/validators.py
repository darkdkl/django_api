from marshmallow import Schema, fields, validates, validate, ValidationError, post_load
from django.utils.text import slugify
from django.core.validators import slug_re
from .models import Presentation


class PresentationSchema(Schema):
    deckId = fields.Int(required = True)
    authorUsername = fields.Str(required = True, validate = validate.Length(min = 1))
    deckSlug = fields.Str(required = True)

    @validates("deckSlug")
    def validate_deckSlug(self, value):
        if value == 'undefined':
            raise ValidationError("Shorter than minimum length 1.")
        if not slug_re.match(value):
            raise ValidationError("Enter a valid 'slug' ")

    @post_load
    def create(self, data, **kwargs):
        return Presentation(**data)

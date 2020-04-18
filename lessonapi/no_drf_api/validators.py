from marshmallow import Schema, fields,validates,validate,ValidationError
from django.utils.text import slugify
from django.core.validators import slug_re

class PresentationSchema(Schema):
    deckId=fields.Int()
    authorUsername=fields.Str(validate=validate.Length(min=1))
    deckSlug=fields.Str()

    @validates("deckSlug")
    def validate_deckSlug(self, value):
        if value == 'undefined':
            raise ValidationError("Shorter than minimum length 1.")  
        if not slug_re.match(value):
            raise ValidationError("Enter a valid 'slug' ")      
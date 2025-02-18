from base.utiles.custom_exception import DataValidationError
from marshmallow import Schema, fields, ValidationError


class CategoryDTO(Schema):
    Category_name = fields.String(
        required=True
    )
    Category_description = fields.String(
        required=True
    )

    class Meta:
        ordered = True
from django.core.exceptions import ValidationError
from pos_project import constants
from jsonschema import validate

def get_validator(body):
    schema = {
        'order': {'choices': ['asc', 'desc', '']},
        'count': {'type': 'integer'},
        'offset': {'type': 'integer'},
        'brand_id': {'type': 'integer', 'required': True},
    }

    try:
        validate_data(body, schema)
    except ValidationError as e:
        raise ValidationError({"error": e.message})

def addon_get_validator(body):
    schema = {
        'order': {'choices': ['asc', 'desc', '']},
        'count': {'type': 'integer'},
        'offset': {'type': 'integer'},
        'addon_categories_id': {'type': 'integer', 'min': 1, 'required': True},
    }

    try:
        validate_data(body, schema)
    except ValidationError as e:
        raise ValidationError({"error": e.message})

def category_post_validator(body):
    schema = {
        'brand_id': {'type': 'integer', 'required': True},
        'name': {'type': 'string', 'minlength': 3, 'required': True},
        'image': {'type': 'string', 'minlength': 3, 'required': True},
    }

    try:
        validate_data(body, schema)
    except ValidationError as e:
        raise ValidationError({"error": e.message})

def category_put_validator(body):
    schema = {
        'id': {'type': 'integer', 'required': True},
        'name': {'type': 'string', 'minlength': 3, 'maxlength': 100},
        'visible': {'type': 'boolean'},
        'image': {'type': 'string', 'minlength': 3},
    }

    try:
        validate_data(body, schema)
    except ValidationError as e:
        raise ValidationError({"error": e.message})

def delete_validator(body):
    schema = {
        'id': {'type': 'integer', 'min': 1, 'required': True},
    }

    try:
        validate_data(body, schema)
    except ValidationError as e:
        raise ValidationError({"error": e.message})

def update_outlet_validator(body):
    schema = {
        'type': 'array',
        'items': {
            'type': 'object',
            'properties': {
                'data': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer', 'required': True},
                        'visible': {'type': 'boolean'},
                    },
                    'required': ['id'],
                },
                'outlets': {
                    'type': 'array',
                    'items': {'type': 'integer', 'required': True},
                },
            },
            'required': ['data', 'outlets'],
        },
    }

    try:
        validate_data(body, schema)
    except ValidationError as e:
        raise ValidationError({"error": e.message})

def addon_post_validator(body):
    schema = {
        'name': {'type': 'string', 'minlength': 3, 'required': True},
        'addon_categories_id': {'type': 'integer', 'min': 1, 'required': True},
        'price': {'type': 'number', 'min': 0, 'required': True},
        'food_tag': {'type': 'string', 'enum': list(constants.FOOD_TAG.keys()), 'required': True},
        'image': {'type': 'string', 'minlength': 3, 'required': True},
    }

    try:
        validate_data(body, schema)
    except ValidationError as e:
        raise ValidationError({"error": e.message})

def addon_put_validator(body):
    schema = {
        'name': {'type': 'string', 'minlength': 3},
        'addon_id': {'type': 'integer', 'min': 1, 'required': True},
        'price': {'type': 'number', 'min': 0},
        'food_tag': {'type': 'string', 'enum': list(constants.FOOD_TAG.keys())},
        'visible': {'type': 'boolean'},
        'image': {'type': 'string', 'minlength': 3},
    }

    try:
        validate_data(body, schema)
    except ValidationError as e:
        raise ValidationError({"error": e.message})

def addon_category_link_validator(data):
    schema = {
        'outlet_id': {'type': 'integer', 'required': True},
        'addon_categories_id': {'type': 'integer', 'required': True},
        'visible': {'type': 'boolean'},
    }

    try:
        validate(data, schema)
    except ValidationError as e:
        raise ValidationError({"error": e.message})

def validate_data(data, schema):
    validate(data, schema)


import jsonschema
from jsonschema import ValidationError


def validate_json(data, schema):
    if not jsonschema.validate(data.components, schema):
        raise ValidationError('Invalid Schema')

# TODO validate JSON for magic components in app

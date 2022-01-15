from django import template
from dndPlayerClassBlueprint.utils import TableForm

register = template.Library()


@register.filter()
def does_editable_form_exist(enum_key):
    return enum_key in TableForm.__members__


@register.filter()
def enum_substring(text):
    return text[:3].upper()

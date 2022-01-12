from django import template
from django.urls import get_resolver
register = template.Library()


@register.filter()
def does_param_url_exists(param):
    url = f'/player\\-class\\-blueprint/add\\-and\\-update/{param}$'
    return url in set(v[1] for k, v in get_resolver(None).reverse_dict.items())

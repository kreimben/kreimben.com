from django import template

register = template.Library()


@register.filter()
def get_last_from_string(value: str):
    return value.split('/')[-1]


@register.filter
def multiply(value, arg):
    return value * arg

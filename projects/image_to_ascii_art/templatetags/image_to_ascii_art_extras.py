from django import template

register = template.Library()


@register.filter()
def get_last_from_string(value: str):
    return value.split('/')[-1]


@register.filter
def multiply(value, arg):
    return value * arg


@register.filter
def get_string_kilo_bytes(value: str):
    # get string's bytes size
    return f"{len(value.encode('utf-8')) / 1024:.2f} KB"


@register.filter
def get_string_char_count(value: str):
    return f'{len(value)} characters'

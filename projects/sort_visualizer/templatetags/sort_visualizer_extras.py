from django import template

register = template.Library()


@register.filter()
def represent(value: str):
    if '**' in value:
        v = value.split('**')
        return f'{v[0]}<sup>{v[1]}</sup>'
    else:
        return value

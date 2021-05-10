from django import template
register = template.Library()

@register.filter(name = 'remove_comma')
def remove_comma(value, arg):
    for ch in arg:
        print(ch)
        value = value.replace(ch, '')
    return value

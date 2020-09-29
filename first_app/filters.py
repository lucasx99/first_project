from django import template

register = template.Library()


@register.filter()
def cuting(value, arg):
    return value.replace(arg, '')




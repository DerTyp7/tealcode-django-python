from django import template

register = template.Library()

@register.filter
def filter_blank(value):
    return value.replace(" ", "%20")
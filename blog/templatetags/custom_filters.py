from django import template

register = template.Library()

@register.filter
def limit_characters(value, char_count):
    if len(value) <= char_count:
        return value
    return value[:char_count] + ' ...'

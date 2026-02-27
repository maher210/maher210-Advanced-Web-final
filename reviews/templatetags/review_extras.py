from django import template

register = template.Library()

@register.filter
def stars(value):
    """
    Convert rating number to stars
    """
    try:
        value = int(value)
    except (TypeError, ValueError):
        return ""

    return "⭐" * value
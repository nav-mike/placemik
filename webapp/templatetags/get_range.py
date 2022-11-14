from django.template import Library

register = Library()


@register.filter
def get_range(value):
    return range(value)


@register.filter
def get_rating_stars_range(value):
    return range(value)


@register.filter
def get_rating_stars_empty_range(value):
    return range(5 - value)

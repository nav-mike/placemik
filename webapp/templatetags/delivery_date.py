from django.template import Library
from datetime import datetime, timedelta

register = Library()


@register.simple_tag
def get_delivery_date():
    return (datetime.now() + timedelta(days=14)).strftime("%-d %B %Y")

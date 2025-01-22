
from django import template
from datetime import date

register = template.Library()

@register.filter
def age(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    return age

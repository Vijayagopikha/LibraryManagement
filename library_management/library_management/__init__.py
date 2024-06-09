from django import template
from django.conf import settings

register = template.Library()

@register.filter
def full_url(image_url):
    return f'http://127.0.0.1:8000{image_url}' if settings.DEBUG else image_url

from django import template
from utils.permissions import has_permission

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={'class': css_class})

@register.filter
def get_field(form, field_name):
    return form[field_name]
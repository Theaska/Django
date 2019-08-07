from django import template

register = template.Library()

@register.filter(name='monthList')
def monthList(value):
    value = ['January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December']
    return value
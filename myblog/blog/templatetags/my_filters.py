from django import template
<<<<<<< HEAD
from blog.models import Blog

register = template.Library()

@register.filter(name='months_list')
def months_list(value):
        value = ['january', 'february', 'march', 'april', 'may', 'june',
                'july', 'august', 'september', 'october', 'november', 'december']
        return value

@register.filter(name='get_blogs_tags')
def get_blogs_tags(value):
        value = Blog.objects.values('tagline')
        return value
=======

register = template.Library()

@register.filter(name='monthList')
def monthList(value):
    value = ['January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December']
    return value
>>>>>>> 0e9f77b6729c82fdbf00e9cc44ebc3e3f0005958

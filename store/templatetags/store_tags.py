from django import template
from store.models import *

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('store/list_categories.html')
def show_categories(selected=0):
    cats = Category.objects.all()
    return {"cats":cats, "selected": selected}
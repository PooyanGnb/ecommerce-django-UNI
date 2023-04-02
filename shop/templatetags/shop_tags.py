from django import template
from shop.models import Category, Product

register = template.Library()

@register.inclusion_tag('shop/base-category.html')
def category():
    category = Category.objects.all()
    return {'category': category}

@register.simple_tag(name='catimage')
def categoryimage(cat):
    product = Product.objects.filter(category=cat)
    return product[0]
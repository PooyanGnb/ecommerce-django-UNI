from django import template
from shop.models import Category, Product, Order

register = template.Library()

@register.inclusion_tag('shop/base-category.html')
def category():
    category = Category.objects.all()
    return {'category': category}

@register.simple_tag(name='catimage')
def categoryimage(cat):
    product = Product.objects.filter(category=cat)
    return product[0]

@register.simple_tag(name='cartnumber')
def cartnumber(user):
    try:
        order = Order.objects.filter(user=user)
        return order[0].get_cart_item
    except TypeError:
        return 0
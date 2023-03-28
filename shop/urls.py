from django.urls import path
from shop.views import *

app_name = 'shop'

urlpatterns = [
    path('', shop_index, name='index'),
    path('shop/', shop_shop, name='shop'),
    path('detail/', shop_detail, name='detail'),
    path('contact/', shop_contact, name='contact'),
    path('cart/', shop_cart, name='cart'),
]
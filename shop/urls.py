from django.urls import path
from shop.views import *
from shop.feeds import LatestEntriesFeed

app_name = 'shop'

urlpatterns = [
    path('', shop_index, name='index'),
    path('shop/', shop_shop, name='shop'),
    path('shop/<str:slug>', shop_detail, name='detail'),
    path('shop/category/<str:catname>', shop_shop, name='category'),
    path('shop/color/<str:colorname>', shop_shop, name='color'),
    path('shop/<str:slug>/', shop_detail, name='size'),
    path('contact/', shop_contact, name='contact'),
    path('cart/', shop_cart, name='cart'),
    path('checkout/', shop_checkout, name='checkout'),
    path('updateitem/', updateitem, name='updateitem'),
    path('search/', shop_search, name='search'),
    path('contact', contact_view, name='contact'),
    path('newsletter', newsletter_view, name='newsletter'),
    path('rss/feed/', LatestEntriesFeed()),
]
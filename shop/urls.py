from django.urls import path
from shop.views import *

app_name = 'shop'

urlpatterns = [
    path('', shop_index, name='index'),
]
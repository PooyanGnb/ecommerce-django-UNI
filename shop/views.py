from django.shortcuts import render

# Create your views here.
def shop_index(request):
    return render(request, 'shop/index.html')

def shop_shop(request):
    return render(request, 'shop/shop.html')

def shop_detail(request):
    return render(request, 'shop/detail.html')

def shop_contact(request):
    return render(request, 'shop/contact.html')

def shop_cart(request):
    return render(request, 'shop/cart.html')
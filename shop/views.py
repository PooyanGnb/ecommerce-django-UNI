from django.shortcuts import render, get_object_or_404
from shop.models import *
from shop.forms import *
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

# Create your views here.
def shop_index(request):
    products = Product.objects.filter(status=True)[:8]
    ordered_products = Product.objects.filter(status=True).order_by('-counted_views')[:8]
    category = Category.objects.all()
    context = {'products': products, 'category': category, 'ordered_products': ordered_products}
    return render(request, 'shop/index.html', context)

def shop_shop(request, **kwargs):
    products = Product.objects.filter(status=True)
    if kwargs.get('catname') != None:
        products = products.filter(category__name=kwargs['catname'])  
    if kwargs.get('colorname') != None:
        products = products.filter(color__name=kwargs['colorname'])
    products = Paginator(products, 9)
    try:
        page_number = request.GET.get('page')
        products = products.get_page(page_number)
    except PageNotAnInteger:
        products = products.get_page(1)
    except EmptyPage:
        products = products.get_page(1)
    context = {'products': products}
    return render(request, 'shop/shop.html', context)

def shop_detail(request, slug):
    products = Product.objects.filter(status=True)
    product = get_object_or_404(products,slug=slug)
    products = products.filter(category=product.category.all()[0]).order_by('-counted_views')[:4]
    images = ProductImage.objects.filter(product_id__slug=slug)
    context = {'product': product, 'images': images, 'products': products}
    product.view_increament()
    return render(request, 'shop/detail.html', context)

def shop_contact(request):
    return render(request, 'shop/contact.html')

def shop_cart(request):
    return render(request, 'shop/cart.html')

def shop_search(request):
    products = Product.objects.filter(status=1)
    if s := request.GET.get('s'):
        products = products.filter(name__contains=s)
    context =  { 'products': products}
    return render(request, 'shop/shop.html', context)

def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST.copy())
        if form.is_valid():
            post = form.save(commit=False)
            post.name = 'unknown'
            post.save()
            messages.add_message(request,messages.SUCCESS,'Your ticket submitted successfully!')
        else:
            messages.add_message(request,messages.ERROR,'Your ticket did not submitted!')
    return render(request, 'shop/contact.html',{'form':form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Your email submitted successfully!')
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
# def add_item(request):
#     product = Product.objects.all()
#     image = Image.objects.all()
#     if request.method == "POST":
#         #images will be in request.FILES
#         form = ImageForm(request.POST or None, request.FILES or None)
#         files = request.FILES.getlist('images')
#         if form.is_valid():
#             # form.name = form.cleaned_data['name']
#             # form.category = form.cleaned_data['category']
#             # form.price = form.cleaned_data['price']
#             # form.description = form.cleaned_data['description']
#             product_obj = form.save() #create will create as well as save too in db.
#             for f in files:
#                 # x = Image()
#                 # x.product_id = product_obj.id
#                 # x.image = f
#                 # x.save()
#                 Image.objects.create(product_id=product_obj, image=f)
#             print("Product created")
#         else:
#             print("faield")
#     return render(request, 'test.html', {'product': product, 'image': image})
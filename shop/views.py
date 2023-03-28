from django.shortcuts import render

# Create your views here.
def shop_index(request):
    return render(request, 'index.html')
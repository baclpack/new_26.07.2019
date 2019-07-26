from django.shortcuts import render
from .models import *

# Create your views here.
def catalog_list(request):
    catalog = Catalog.objects.all()
    context = {
        'catalog': catalog
    }
    return render(request, 'blog/catalog_list.html', context)


def category_list(request):
    category = Category.objects.all()
    context = {
        'category': category
    }
    return render(request, 'blog/category_list.html', context)


def product_phone_list(request):
    product_phone = Product_Phone.objects.all()
    context = {
        'product_phone': product_phone
    }
    return render(request, 'blog/phone/product_phone.html', context)
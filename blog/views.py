from django.shortcuts import render
from .models import *

# Create your views here.
def catalog_list(request):
    catalog = Catalog.objects.all()
    context = {
        'catalog': catalog
    }
    return render(request, 'blog/catalog_list.html', context)

def catalog_detail(request, slug):
    catalog = Catalog.objects.get(slug__iexact=slug)
    context = {
        'catalog': catalog,
    }
    return render(request, 'blog/catalog_detail.html', context)


def category_phone_list(request):
    category_phone = Category_Phone.objects.all()
    context = {
        'category_phone': category_phone
    }
    return render(request, 'blog/category_phone_list.html', context)


# def product_phone_list(request):
#     product_phone = Product_Phone.objects.all()
#     context = {
#         'product_phone': product_phone
#     }
#     return render(request, 'blog/phone/product_phone.html', context)
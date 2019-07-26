from django.urls import path
from .views import *

urlpatterns = [
    path('', catalog_list, name='catalog_list_url'),
    path('category/', category_list, name='category_list_url'),
    path('product_phone/', product_phone_list, name='product_phone_list_url'),
]
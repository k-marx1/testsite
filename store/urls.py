from django.contrib import admin
from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('', show_main_page, name='home'),
    path('product/<slug:product_id>/', show_product, name='product_details'),
    path('category/<slug:category_id>/', show_category, name='category_details'),
    path('shop/', show_shop, name='shop')
]

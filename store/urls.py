from django.contrib import admin
from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('', show_main_page, name='home'),
    path('product/<int:product_id>/', show_product, name='product_details'),
    path('category/<int:category_id>/', show_category, name='category_details')
]

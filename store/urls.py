from django.contrib import admin
from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('product/<slug:product_id>/', show_product, name='product_details'),
    path('category/<slug:category_id>/', Shop.as_view(), name='category_details'),
    path("__debug__/", include("debug_toolbar.urls")),
]

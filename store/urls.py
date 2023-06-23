from django.contrib import admin
from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path(r'', HomePage.as_view(), name='home'),
    path(r'product/<slug:slug>/', ShowProduct.as_view(), name='product_details'),
    path(r'category/<slug:slug>/', Shop.as_view(), name='category_details'),
    path(r'sign_up/', SignUpUser.as_view(), name='sign_up'),
    # path(r'add_product/', add_page, name='add_page'),
    path(r'sign_in/', LoginUser.as_view(), name='sign_in'),
    path("__debug__/", include("debug_toolbar.urls")),
    path('logout/', logout_user, name='logout'),
    path(r'profile/', show_profile, name='profile')
]

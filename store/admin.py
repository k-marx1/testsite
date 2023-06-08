from django.contrib import admin

from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'in_stock', 'available', 'category')
    list_display_links = ('in_stock', 'category')
    search_fields = ('product_name', 'description')

admin.site.register(Product, ProductAdmin)
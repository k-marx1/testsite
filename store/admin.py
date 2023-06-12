from django.contrib import admin

from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'slug', 'in_stock', 'available', 'category', 'discount')
    list_editable = ('product_name', 'slug', 'available', 'discount')
    list_display_links = ('in_stock', 'category')
    search_fields = ('product_name', 'description', 'slug')
    prepopulated_fields = {'slug': ('product_name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'slug')

    prepopulated_fields = {'slug': ('category_name',)}



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
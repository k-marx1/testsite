from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *
from django.urls import reverse

categories = Category.objects.all()


def show_main_page(request):
    context = {
        'product': Product.objects.all(),
        'title': 'Main page',
    }
    return render(request, 'store/index.html', context)



def show_product(request, product_id):
    product = get_object_or_404(Product, slug=product_id)
    context = {
        'product': product,
        'title': product.product_name,
        'selected': product.category_id
    }
    return render(request, 'store/product_details.html', context)


def show_category(request, category_id):
    w = Product.objects.filter(category__slug=category_id)
    if len(w) == 0:
        return error404(request, ValueError)
    context = {
        'products': w,
        'title': Category.objects.filter(slug=category_id)[0],
        'selected': category_id
    }
    return render(request, 'store/category_details.html', context)


def error404(request, exception):
    return redirect('home')

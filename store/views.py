from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *
from django.urls import reverse

categories = Category.objects.all()


def show_main_page(request):
    context = {
        'product': Product.objects.all(),
        'title': 'Main page',
        'categories': categories
    }
    return render(request, 'store/index.html', context)


def about(request):
    context = {
        'menu': menu
    }
    return render(request, 'store/about.html', context)


def addpage(request):
    return HttpResponse('addpage')


def show_product(request, product_id):
    context = {
        'product': Product.objects.filter(id=product_id),
        'title': product_id,
        'categories': categories,
    }
    return render(request, 'store/product_details.html', context)


def show_category(request, category_id):
    w = Product.objects.filter(category_id=category_id)
    if len(w) == 0:
        return error404(request, ValueError)
    context = {
        'products': w,
        'title': Category.objects.filter(id=category_id)[0],
        'categories': categories,
    }
    return render(request, 'store/category_details.html', context)


def error404(request, exception):
    return redirect('home')

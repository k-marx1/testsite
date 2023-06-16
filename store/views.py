from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from .models import *
from django.urls import reverse

categories = Category.objects.all()


class HomePage(ListView):
    model = Product
    template_name = 'store/index.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.all().order_by('-discount')[:3]
        context['title'] = 'Main page'
        context['categories'] = categories
        return context

class Shop(ListView):
    model = Category
    template_name = 'store/shop.html'
    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug']).category_name
        context['categories'] = categories
        context['product_list'] = Product.objects.filter(category__slug=self.kwargs['slug'])
        return context

class ShowProduct(DetailView):
    model = Product
    template_name = 'store/product_page.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = get_object_or_404(Product, slug=self.kwargs['slug'])
        context['categories'] = categories
        context['title'] = context['product'].product_name
        return context






from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse, reverse_lazy

from .forms import AddProduct
from .utils import *
from .models import *


class HomePage(DataMixin, ListView):
    model = Product
    template_name = 'store/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Main Page', product=Product.objects.all().order_by('-discount')[:3])
        return context | c_def


class Shop(DataMixin, ListView):
    model = Category
    template_name = 'store/shop.html'
    paginate_by = 2

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=Category.objects.get(slug=self.kwargs['slug']).category_name,
                                      product_list=Product.objects.filter(category__slug=self.kwargs['slug']))
        return context | c_def


class ShowProduct(DataMixin, DetailView):
    model = Product
    template_name = 'store/product_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['product'].product_name,
                                      product=get_object_or_404(Product, slug=self.kwargs['slug']))
        return context | c_def


class SignUpUser(DataMixin, CreateView):

    form_class = UserCreationForm
    template_name = 'store/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Sign Up')
        return context | c_def



def add_page(request):
    if request.method == 'POST':
        form = AddProduct(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddProduct()
    return render(request, 'store/add_page.html', {'form': form})

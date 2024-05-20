from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse

from . import models


class ProductList(ListView):
    model = models.Product  # QuerySet
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 10
    ordering = ['-id']


class ProductDetail(DetailView):
    model = models.Product  # QuerySet
    template_name = 'products/detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'


class AddToCart(ListView):
    pass


class RemoveFromCart(ListView):
    pass


class Cart(ListView):
    pass


class Finalize(ListView):
    pass

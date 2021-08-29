from django.shortcuts import render

from shop.models import Product

# from django.http import HttpResponse


def index(request):
    context = {'products': Product.objects.all()}
    return render(request, 'index.html', context)

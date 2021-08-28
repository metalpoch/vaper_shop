from django.shortcuts import render

from shop.models import Product


def index(request):
    products = Product.objects.all()
    # message = {
    #     'icon': 'warning',
    #     'title': 'Oops...',
    #     'text': 'To continue you must log in',
    #     'show_confirm_button': True,
    #     'is_login': True,
    #     'timer': 0,
    # }
    context = {
        'products': products,
        # 'message': message
    }

    return render(request, 'index.html', context)

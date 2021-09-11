from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.db.models import Sum

from shop.models import Product, SalesRecord
from shop.forms import PurchaseProductForm
from shop.validations import remaining_products

from clients.models import Client
from clients.validations import no_have_credits


def index(request):
    context = {'products': Product.objects.all()}
    return render(request, 'index.html', context)


def about(request):
    try:
        return FileResponse(
            open('static/documents/KeiberUrbila-CV.pdf', 'rb'),
            content_type='application/pdf'
        )
    except FileNotFoundError:
        raise Http404


def product_detail(request, fake, id):
    context = {
        'product': get_object_or_404(Product, pk=id),
        'form': PurchaseProductForm,
    }

    # if method is post and  user no login
    if request.method == 'POST' and request.user.id is None:
        context['message'] = 'noUserLogin'

    # Buying vape
    elif request.method == 'POST' and request.user.id is not None:
        data_form = PurchaseProductForm(request.POST)

        if data_form.is_valid():
            client = get_object_or_404(Client, pk=request.user.id)
            product = get_object_or_404(Product, pk=id)

            # validate if the client have credits
            not_credits_enough = no_have_credits(
                credits=client.credits,
                product_price=product.price,
                quantity=data_form.cleaned_data['quantity']
            )

            # validate if the stock have product
            empty_stock, can_buy, not_stock_enough = remaining_products(
                product_stock=product.stock,
                quantity=data_form.cleaned_data['quantity']
            )

            if not_credits_enough:
                context['form'] = data_form
                context['message'] = 'notCreditsEnough'

            elif not_stock_enough:
                context['form'] = data_form
                context['message'] = 'productNoEnough'
                context['num'] = product.stock

            elif data_form.cleaned_data['quantity'] == 0:
                context['form'] = data_form
                context['message'] = 'quantityError'

            elif can_buy:
                # Save the purchase into the table 'sales records' and update
                # stock product and the client credits
                data_form = data_form.save(commit=False)
                data_form.client = client
                data_form.product = product
                product.stock -= data_form.quantity
                client.credits -= product.price * data_form.quantity
                product.save()
                client.save()
                data_form.save()
                return redirect('profile')

            else:  # No stock
                context['form'] = data_form
                context['message'] = 'stockEmpty'

            return render(request, 'details.html', context)

    return render(request, 'details.html', context)


def trends(request):
    top5 = SalesRecord.objects.values('product').order_by('product').annotate(
        sell=Sum('quantity')
    ).order_by('sell').reverse()[:5]

    product_list = [x['product'] for x in list(top5)]

    products = Product.objects.filter(pk__in=product_list)

    context = {
        'products': products,
        'top5': top5
    }
    return render(request, 'trends.html', context)

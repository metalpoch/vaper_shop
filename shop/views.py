from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse

from shop.models import Product
from clients.models import Client

from random import randint


def index(request):
    context = {'products': Product.objects.all()}
    return render(request, 'index.html', context)


def credits(request):

    def basic_math_question():
        num1, num2, oper = randint(1, 10), randint(1, 10), randint(1, 3)
        if oper == 1:
            oper = '+'
            result = num1 + num2
        elif oper == 2:
            oper = '-'
            result = num1 - num2
        else:
            oper = '*'
            result = num1 * num2
        return num1, num2, oper, result

    num1, num2, oper, result = basic_math_question()

    values = [basic_math_question()[-1] for x in range(5)]

    values.append(result)
    values.sort()

    context = {
        'num1': num1,
        'num2': num2,
        'oper': oper,
        'result': result,
        'values': values
    }
    return render(request, 'credits.html', context)


def add_credits(request, id, credits):
    client = get_object_or_404(Client, pk=id)
    client.credits += credits
    client.save()
    return redirect('credits')

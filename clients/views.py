from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from clients.models import Client
from clients.forms import ClientRegisterForm
from clients.validations import birth_date_valid, basic_math


def sign_up(request):
    context = {
        'form': ClientRegisterForm(),
    }

    if request.method == 'POST':
        data_form = ClientRegisterForm(request.POST)

        if data_form.is_valid():
            if birth_date_valid(data_form.cleaned_data['birth_date']):
                data_form.save()
                user = authenticate(
                    username=data_form.cleaned_data['username'],
                    password=data_form.cleaned_data['password1']
                )
                login(request, user)

                return redirect(to='home')
            else:
                context['message'] = {
                    'icon': 'error',
                    'title': 'You must be at least 21 years old to register',
                    'show_confirm_button': False,
                    'show_sign_in': False,
                    'timer': 2000
                }

        context['form'] = data_form

    return render(request, 'signup.html', context)


@login_required(login_url='login/')
def credits(request):
    num1, num2, oper, result = basic_math()
    values = [basic_math()[-1] for x in range(5)]

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


@login_required(login_url='login/')
def add_credits(request, id, credits):
    client = get_object_or_404(Client, pk=id)
    client.credits += credits
    client.save()
    return redirect('credits')


@login_required(login_url='login/')
def profile(request):
    return render(request, 'profile.html')

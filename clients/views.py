from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required

from clients.forms import ClientRegisterForm
from clients.validations import birth_date_valid


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

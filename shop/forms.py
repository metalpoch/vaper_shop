from django import forms
from django.contrib.auth.forms import UserCreationForm

from shop.models import Client


class ClientRegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    birth_date = forms.DateField(help_text='YYYY-MM-DD')

    class Meta:
        model = Client
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'gender',
            'birth_date',
            'address',
        )

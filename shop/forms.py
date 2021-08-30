from django import forms
from shop.models import SalesRecord


class PurchaseProductForm(forms.ModelForm):
    amount = forms.NumberInput()

    class Meta:
        model = SalesRecord
        fields = ("amount",)

from django import forms
from shop.models import SalesRecord


class PurchaseProductForm(forms.ModelForm):
    quantity = forms.NumberInput()

    class Meta:
        model = SalesRecord
        fields = ("quantity",)

from email.policy import default
from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(required=True)
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput)

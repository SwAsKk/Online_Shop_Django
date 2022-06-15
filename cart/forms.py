from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(required=False, initial=1, widget=forms.HiddenInput)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


CITY_CHOICES =(
    ("spb", "Санкт-Петербург"),
    ("bal", "Балашиха"),
)

class OrderForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={'placeholder': 'Ваше имя',
            'class':'form-control'}
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'E-mail',
            'class':'form-control'}
        )
    )

    phone = forms.CharField(
        max_length=11,
        widget=forms.TextInput(
            attrs={'placeholder': 'Номер телефона',
            'class':'form-control'}
        )
    )

    city = forms.ChoiceField(
        choices = CITY_CHOICES,

    )

    adress = forms.CharField(
        max_length= 200,
        widget=forms.TextInput(
            attrs={'placeholder': 'Адрес доставки',
            'class':'form-control'}
        )
    )

    change = forms.CharField(
        max_length=12,
        widget=forms.TextInput(
            attrs={'placeholder': 'С какой суммы нужна сдача? (если сдача не нужна, укажите "не нужно")',
            'class':'form-control'}
        )
    )

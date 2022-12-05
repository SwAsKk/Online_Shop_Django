from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from main.models import *

from .cart import Cart
from .forms import CITY_CHOICES, CartAddProductForm, OrderForm

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string




def base_context(request):
    context = dict()
    context['user'] = request.user
    context["site_name"] = "Sushiman"  # Строка перед | в title страницы
    context["page_name"] = "Главная"  # Строка после |
    context["page_header"] = ""  # Название страницы в display-3 стиле
    return context

# Create your views here.


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    print(form.is_valid())
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            override_quantity=cd['override']
        )
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    c = base_context(request)

    c["page_name"] = "Корзина"
    c["page_header"] = "Корзина"
    c["cart"] = Cart(request)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data={
                'name': form.cleaned_data['name'],
                'phone': form.cleaned_data['phone'],
                'city': form.cleaned_data['city'],
                'adress': form.cleaned_data['adress'],
                'change': form.cleaned_data['change'],
                'email': form.cleaned_data['email'],
                'cart': Cart(request),
            }
            if form.cleaned_data['city'] == 'spb':
                html_body = render_to_string("mail.html", data)
                msg = EmailMultiAlternatives (subject="Новый заказ!", from_email='from_mail@gmail.com', to=['to_mail@gmail.com',])
                msg.attach_alternative(html_body, "text/html")
                msg.send()
            elif form.cleaned_data['city'] == 'bal':
                html_body = render_to_string("mail.html", data)
                msg = EmailMultiAlternatives (subject="Новый заказ!", from_email='from_mail@gmail.com', to=['to_mail@gmail.com',])
                msg.attach_alternative(html_body, "text/html")
                msg.send()
            return redirect('/')


    else:
        form = OrderForm()
    c['form'] = form
    return render(request, 'cart/detail.html', c)


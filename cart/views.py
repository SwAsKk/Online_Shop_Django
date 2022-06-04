from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from main.models import *

from .cart import Cart
from .forms import CartAddProductForm


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

    return render(request, 'cart/detail.html', c)

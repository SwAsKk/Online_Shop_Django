import imp
from importlib.metadata import requires
from subprocess import call
from django.shortcuts import render
from django.template import base, context
from cart.forms import CartAddProductForm

from main.models import *
from main.forms import *
from django.views import View
from django.http import HttpResponseRedirect



def base_context(request):
    context = dict()
    context['user'] = request.user
    return context

#начальная страница
def index(request):
    return render(request, 'index.html')



#Вьюхи для просмотра товаров по категориям меню с фильтрацией
def baked(request):
    c = base_context(request)
    ob = Product.objects.filter(type="Запечённые роллы")
    c['baked_list'] = ob
    return render(request, 'baked.html', c)


def sushi(request):
    c = base_context(request)
    ob = Product.objects.filter(type="Суши")
    c['sushi_list'] = ob
    return render(request, 'sushi.html', c)

def rolls(request):
    c = base_context(request)
    ob = Product.objects.filter(type="Роллы")
    c['rolls_list'] = ob
    return render(request, 'rolls.html', c)

def sets(request):
    c = base_context(request)
    ob = Product.objects.filter(type="Наборы")
    c['sets_list'] = ob
    return render(request, 'sets.html', c)

def tempured(request):
    c = base_context(request)
    ob = Product.objects.filter(type="Темпура")
    c['tempured_list'] = ob
    return render(request, 'tempured.html', c)


def wok(request):
    c = base_context(request)
    ob = Product.objects.filter(type="Лапша wok")
    c['wok_list'] = ob
    return render(request, 'wok.html', c)

def soup(request):
    c = base_context(request)
    ob = Product.objects.filter(type="Супы")
    c['soup_list'] = ob
    return render(request, 'soup.html', c)


def hotandsalads(request):
    c = base_context(request)
    ob = Product.objects.filter(type="Горячее и салаты")
    c['hotandsalads_list'] = ob
    return render(request, 'hotandsalads.html', c)

def minirolls(request):
    c = base_context(request)
    ob = Product.objects.filter(type="Мини роллы")
    c['minirolls_list'] = ob
    return render(request, 'minirolls.html', c)

def magrolls(request):
    c = base_context(request)
    ob = Product.objects.filter(type="Маг роллы")
    c['magrolls_list'] = ob
    return render(request, 'magrolls.html', c)

def vegan(request):
    c = base_context(request)
    ob = Product.objects.filter(type="Вегетарианское меню")
    c['vegan_list'] = ob
    return render(request, 'vegan.html', c)

def deserts(request):
    c = base_context(request)
    ob = Product.objects.filter(type="Десерты")
    c['deserts_list'] = ob
    return render(request, 'deserts.html', c)

def drinks(request):
    c = base_context(request)
    ob = Product.objects.filter(type="Напитки")
    c['drinks_list'] = ob
    return render(request, 'drinks.html', c)

def stuff(request):
    c = base_context(request)
    ob = Product.objects.filter(type="Всё для суши")
    c['stuff_list'] = ob
    return render(request, 'stuff.html', c)

def pizza(request):
    c = base_context(request)
    ob = Product.objects.filter(type="Пицца")
    c['pizza_list'] = ob
    return render(request, 'pizza.html', c)

#Вьюхи для просмотра товаров по категориям меню с фильтрацией

class ProductDetails(View):
    def get(self,request,id):
        product = Product.objects.get(id = id)
        cart_product_form = CartAddProductForm()
        return render(request, 'product-details.html', context={'product':product,
            'cart_product_form': cart_product_form})
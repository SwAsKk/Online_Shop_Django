from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from main.models import *
from main.forms import *

from cart.forms import CartAddProductForm


def base_context(request):
    context = dict()
    context['user'] = request.user
    context["site_name"] = "Sushiman"  # Строка перед | в title страницы
    context["page_name"] = "Главная"  # Строка после |
    context["page_header"] = ""  # Название страницы в display-3 стиле
    return context

# Начальная страница
def index(request):
    c = base_context(request)
    c["page_header"] = "Меню"
    c["categories"] = Category.objects.all()
    return render(request, 'pages/index.html', c)

# Вьюха для просмотра товаров по категориям меню с фильтрацией
def view_category(request, category_slug):
    c = base_context(request)
    category = get_object_or_404(Category, slug=category_slug)
    
    c["page_name"] = category.name
    c["page_header"] = category.name
    c['products'] = Product.objects.filter(category=category)
    c['form'] = CartAddProductForm()

    return render(request, 'pages/category.html', c)

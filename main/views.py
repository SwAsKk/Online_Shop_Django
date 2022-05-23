import imp
from importlib.metadata import requires
from subprocess import call
from django.shortcuts import render
from django.template import base, context

from main.models import *
from main.forms import *
from django.views import View
from django.http import HttpResponseRedirect



def base_context(request):
    context = dict()
    context['user'] = request.user
    return context

def index(request):
    return render(request, 'index.html')


def baked(request):
    c = base_context(request)
    ob = BakedSet.objects.all()
    c['baked_list'] = ob
    return render(request, 'baked.html', c)


def sushi(request):
    c = base_context(request)
    ob = Sushi.objects.all()
    c['sushi_list'] = ob
    return render(request, 'sushi.html', c)

def rolls(request):
    c = base_context(request)
    ob = Rolls.objects.all()
    c['rolls_list'] = ob
    return render(request, 'rolls.html', c)

def sets(request):
    c = base_context(request)
    ob = Sets.objects.all()
    c['sets_list'] = ob
    return render(request, 'sets.html', c)

def tempured(request):
    c = base_context(request)
    ob = Tempured.objects.all()
    c['tempured_list'] = ob
    return render(request, 'tempured.html', c)


def wok(request):
    c = base_context(request)
    ob = Wok.objects.all()
    c['wok_list'] = ob
    return render(request, 'wok.html', c)

def soup(request):
    c = base_context(request)
    ob = Soup.objects.all()
    c['soup_list'] = ob
    return render(request, 'soup.html', c)


def hotandsalads(request):
    c = base_context(request)
    ob = HotAndSalads.objects.all()
    c['hotandsalads_list'] = ob
    return render(request, 'hotandsalads.html', c)

def minirolls(request):
    c = base_context(request)
    ob = MiniRolls.objects.all()
    c['minirolls_list'] = ob
    return render(request, 'minirolls.html', c)

def magrolls(request):
    c = base_context(request)
    ob = MagRolls.objects.all()
    c['magrolls_list'] = ob
    return render(request, 'magrolls.html', c)

def vegan(request):
    c = base_context(request)
    ob = Vegan.objects.all()
    c['vegan_list'] = ob
    return render(request, 'vegan.html', c)

def deserts(request):
    c = base_context(request)
    ob = Deserts.objects.all()
    c['deserts_list'] = ob
    return render(request, 'deserts.html', c)

def drinks(request):
    c = base_context(request)
    ob = Drinks.objects.all()
    c['drinks_list'] = ob
    return render(request, 'drinks.html', c)

def stuff(request):
    c = base_context(request)
    ob = SushiStuff.objects.all()
    c['stuff_list'] = ob
    return render(request, 'stuff.html', c)

def pizza(request):
    c = base_context(request)
    ob = Pizza.objects.all()
    c['pizza_list'] = ob
    return render(request, 'pizza.html', c)
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
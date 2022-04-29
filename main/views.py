import imp
from importlib.metadata import requires
from subprocess import call
from django.shortcuts import render
from django.template import base, context

from main.models import *
from main.forms import *
from django.views import View
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'index.html')


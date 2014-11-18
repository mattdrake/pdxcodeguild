__author__ = 'matt'
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, render, RequestContext
from django.http import HttpResponseRedirect

from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/success")
        else:
            return HttpResponseRedirect("/invalid")
    else:
        form = RegistrationForm
    token = {}
    token.update(csrf(request))
    token['form'] = form
    return render_to_response("register.html", token)


def home(request):
    return render_to_response("base.html")


def success(request):
    return render_to_response('success.html')

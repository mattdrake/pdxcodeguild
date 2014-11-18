__author__ = 'matt'
from django.shortcuts import render_to_response, render, RequestContext
from django.http import HttpResponseRedirect


def horror(request):
    return render_to_response("horror.html")


def home(request):
    return render_to_response("base.html")


def sci_fi(request):
    return render_to_response("sci_fi.html")


def romance(request):
    return render_to_response("romance.html")


def action(request):
    return render_to_response("action.html")


def comedy(request):
    return render_to_response("comedy.html")


def fantasy(request):
    return render_to_response("fantasy.html")

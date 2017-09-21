
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from models import *
import random


def index(request):
    if "goldcount" not in request.session :
        request.session['goldcount'] = 0
    if "gold" not in request.session :
        request.session['gold'] = 0
    if "activity" not in request.session :
        request.session['activity'] = ""
    if "earned" not in request.session :
        request.session['earned'] = ""
    if "log" not in request.session :
        request.session['log'] = []

    goldcount= request.session['goldcount']
    log= request.session['log']

    context = {
        "goldcount": goldcount,
        "log": log,
    }

    return render(request, "gold/index.html", context)

def process(request):
    if request.POST['button'] == "farm":
        request.session['gold'] = random.randrange(10,21)
        request.session['activity'] = request.POST['button']
    if request.POST['button'] == "cave":
        request.session['gold'] = random.randrange(5,11)
        request.session['activity'] = request.POST['button']
    if request.POST['button'] == "house":
        request.session['gold'] = random.randrange(2,6)
        request.session['activity'] = request.POST['button']
    if request.POST['button'] == "casino":
        request.session['gold'] = random.randrange(-50,51)
        request.session['activity'] = request.POST['button']
    request.session['goldcount'] += request.session['gold']
    if request.session['gold'] > 0 :
        request.session['earned'] = "earned"
    else :
        request.session['earned'] = "lost"

    earned=request.session['earned']
    gold=request.session['gold']
    location=request.session['activity']

    entry = {
        "gold": gold,
        "location": location,
        "earned": earned,
    }
    request.session['log'].append(entry)

    return redirect ('/')

def reset(request):
    del request.session['goldcount']
    del request.session['gold']
    del request.session['log']

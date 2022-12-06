from django.shortcuts import render
from Accounts.models import *
from .models import *

# Create your views here.


def cart(request):
    context = {}
    return render(request, 'cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)
from django.shortcuts import render
from Accounts.models import *
from .models import *

# Create your views here.


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderproduct_set.all()
    else:
        items = []
    context = {'items': items}
    return render(request, 'cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)
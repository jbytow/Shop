from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from Products.models import Products
from .models import *

# Create your views here.


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderproduct_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_products': 0}
    context = {'items': items}
    return render(request, 'cart.html', context)


def add_to_cart(request, product_id):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    product = get_object_or_404(Products, id=product_id)
    cart_item, item_created = OrderProduct.objects.get_or_create(cart=cart, product=product)
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, f"{product.name} was added to your cart.")
    return redirect("cart")


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderproduct_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_products': 0}
    context = {'items': items}
    return render(request, 'checkout.html', context)


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
    context = {'items': items, 'order': order}
    return render(request, 'cart.html', context)


def add_to_cart(request, product_id):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    product = get_object_or_404(Products, id=product_id)
    order_item, item_created = OrderProduct.objects.get_or_create(order=order, product=product)
    if item_created:
        order_item.quantity = 1
    else:
        order_item.quantity += 1
    order_item.save()
    messages.success(request, f"{product.name} was added to your cart.")
    return redirect("cart")


def remove_from_cart(request, product_id):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    product = get_object_or_404(Products, id=product_id)
    try:
        order_item = OrderProduct.objects.get(order=order, product=product)
        if order_item.quantity > 1:
            order_item.quantity -= 1
            order_item.save()
        else:
            order_item.delete()
        messages.success(request, f"{product.name} was removed from your cart.")
    except OrderProduct.DoesNotExist:
        messages.error(request, "The selected item is not in your cart.")
    return redirect("cart")


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderproduct_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_products': 0}
    context = {'items': items, 'order': order}
    return render(request, 'checkout.html', context)

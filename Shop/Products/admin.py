from django.contrib import admin
from .models import Products, Producer, Category, OrderProduct, Order
# Register your models here.

admin.site.register(Products)
admin.site.register(Producer)
admin.site.register(Category)
admin.site.register(OrderProduct)
admin.site.register(Order)
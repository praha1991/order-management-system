# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User, Item, Order, OrderItem
from django.views import generic


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'shop/index.html'
    context_object_name = 'user_list'
    model = User

    def get_queryset(self):
        return User.objects.all()


class ItemView(generic.ListView):
    model = Item
    template_name = 'shop/item.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        return Item.objects.all()

class CartView(generic.ListView):
    model = Order
    template_name = 'shop/cart.html'
    context_object_name = 'cart_list'
    def get_queryset(self):
        return Order.objects.all()

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import User, Item, OrderItem, Order

admin.site.register(User)
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)

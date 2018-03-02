# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db import models
import datetime

class User(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(
        default=datetime.datetime.now, editable=False,
    )

    def __str__(self):
        return self.name + "-" + self.phone


class Item(models.Model):
    item_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True, help_text='Is getting sold?')
    cost = models.FloatField(help_text='Cost of the item')
    capacity = models.IntegerField(help_text='Total items present in the shop', default=1000)
    created_at = models.DateTimeField(
        default=datetime.datetime.now, editable=False,
    )

    def __str__(self):
        return self.item_name


ORDER_STATUS = ["Order Received", "Prepared", "Dispatched", "Delivered"]
PAYMENT_STATUS = ["Not Paid", "Paid by Cash", "Paid by Paytm"]


class Order(models.Model):
    creation_date = models.DateTimeField()
    checked_out = models.BooleanField(default=False, help_text='is checked out')
    user = models.ForeignKey(User)
    order_status = models.CharField(max_length=200,
                                    choices=[(choice, choice) for choice in ORDER_STATUS],
                                    default="Order Received")
    payment_status = models.CharField(max_length=200,
                                      choices=[(choice, choice) for choice in PAYMENT_STATUS],
                                      default="Not Paid")
    created_at = models.DateTimeField(
        default=datetime.datetime.now, editable=False,
    )

    def __str__(self):
        return self.user.name

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    cart = models.ForeignKey(Order)
    item = models.ForeignKey(Item)
    quantity = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.item.cost * self.quantity

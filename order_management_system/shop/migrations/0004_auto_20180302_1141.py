# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-02 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20180302_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='name',
        ),
        migrations.AddField(
            model_name='item',
            name='item_name',
            field=models.CharField(default='idly', max_length=200),
            preserve_default=False,
        ),
    ]
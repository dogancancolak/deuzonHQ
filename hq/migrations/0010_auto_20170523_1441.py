# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '__first__'),
        ('hq', '0009_auto_20170521_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productorder',
            name='pro_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered', to='product.Product'),
        ),
    ]

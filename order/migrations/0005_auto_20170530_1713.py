# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-30 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20170529_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='trackNo',
            field=models.CharField(default='0', max_length=30, null=True),
        ),
    ]

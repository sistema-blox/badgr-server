# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-23 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0017_accesstokenscope'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesstokenscope',
            name='scope',
            field=models.CharField(max_length=255),
        ),
    ]

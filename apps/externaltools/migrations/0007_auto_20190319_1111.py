# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-19 18:11


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('externaltools', '0006_auto_20181102_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externaltoollaunchpoint',
            name='launch_url',
            field=models.CharField(max_length=1024),
        ),
    ]

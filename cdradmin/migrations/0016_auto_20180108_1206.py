# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-08 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cdradmin', '0015_auto_20180108_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superidtoloanliability',
            name='country_of_utilization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdradmin.Country'),
        ),
    ]

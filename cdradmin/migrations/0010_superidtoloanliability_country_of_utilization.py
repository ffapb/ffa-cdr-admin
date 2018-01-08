# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-08 09:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cdradmin', '0009_remove_superidtoloanliability_country_of_utilization'),
    ]

    operations = [
        migrations.AddField(
            model_name='superidtoloanliability',
            name='country_of_utilization',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cdradmin.Country'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-12 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdradmin', '0026_auto_20180312_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='superidtoloanliability',
            name='comments',
            field=models.CharField(blank=True, max_length=600),
        ),
    ]

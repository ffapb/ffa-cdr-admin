# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-04 13:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cdradmin', '0004_auto_20180104_1331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='country_code',
            new_name='country',
        ),
    ]

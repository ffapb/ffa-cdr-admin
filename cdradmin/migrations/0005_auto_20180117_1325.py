# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-17 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdradmin', '0004_auto_20180117_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superidtoloanliability',
            name='ledger',
            field=models.CharField(max_length=255),
        ),
    ]

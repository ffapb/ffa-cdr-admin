# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-17 13:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cdradmin', '0003_auto_20180117_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superidtoloanliability',
            name='ledger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdradmin.Ledger'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-17 12:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cdradmin', '0002_currency_description'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='superid',
            unique_together=set([('superid', 'name')]),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-19 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cdradmin', '0011_superidtoloanliability_guarantee_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyGuarantee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='superidtoloanliability',
            name='currency_guarantee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cdradmin.CurrencyGuarantee'),
        ),
    ]
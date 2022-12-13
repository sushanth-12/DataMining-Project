# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-13 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=300)),
                ('lastname', models.CharField(max_length=200)),
                ('userid', models.CharField(max_length=200)),
                ('password', models.IntegerField()),
                ('mblenum', models.BigIntegerField()),
                ('email', models.EmailField(max_length=400)),
                ('gender', models.CharField(max_length=200)),
            ],
        ),
    ]

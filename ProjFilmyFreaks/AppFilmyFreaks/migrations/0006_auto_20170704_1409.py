# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFilmyFreaks', '0005_auto_20170704_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languageslist',
            name='lang_id',
            field=models.CharField(default='', max_length=10, primary_key=True, serialize=False),
        ),
    ]

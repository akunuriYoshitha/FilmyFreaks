# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 13:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppFilmyFreaks', '0009_auto_20170705_0317'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserPreferences',
        ),
    ]

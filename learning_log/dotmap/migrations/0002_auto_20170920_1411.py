# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 14:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dotmap', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address_info',
            old_name='longtitude',
            new_name='longitude',
        ),
    ]

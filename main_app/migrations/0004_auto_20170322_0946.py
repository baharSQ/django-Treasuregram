# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-22 09:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20170322_0920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treasure',
            old_name='img_url',
            new_name='image',
        ),
    ]

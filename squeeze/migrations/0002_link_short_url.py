# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squeeze', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='short_url',
            field=models.CharField(default='q10wt1', max_length=10),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wootapp', '0002_auto_20170129_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='category',
            field=models.CharField(default='random', max_length=200),
            preserve_default=False,
        ),
    ]
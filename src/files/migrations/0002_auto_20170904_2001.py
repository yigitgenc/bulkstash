# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-04 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='size',
            field=models.BigIntegerField(default=0),
        ),
    ]
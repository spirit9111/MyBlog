# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-15 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20180815_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=128, verbose_name='名字'),
        ),
    ]

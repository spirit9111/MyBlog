# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-12 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20180812_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, height_field=200, null=True, upload_to='upload/', verbose_name='图(820*200)', width_field=820),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-31 04:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_categorytag'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='categorytag',
            table='tb_category_tag',
        ),
    ]
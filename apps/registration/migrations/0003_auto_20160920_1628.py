# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 23:28
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20160920_1326'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('userManager', django.db.models.manager.Manager()),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='courselinks',
            field=models.ManyToManyField(to='enroll.Course'),
        ),
    ]

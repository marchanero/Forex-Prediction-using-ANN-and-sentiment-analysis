# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-04 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('lowa', models.FloatField(default=0)),
                ('opena', models.FloatField(default=0)),
                ('higha', models.FloatField(default=0)),
                ('closea', models.FloatField(default=0)),
                ('predicatea', models.FloatField(default=0)),
            ],
        ),
    ]

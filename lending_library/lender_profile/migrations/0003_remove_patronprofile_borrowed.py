# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 19:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lender_profile', '0002_patronprofile_borrowed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patronprofile',
            name='borrowed',
        ),
    ]

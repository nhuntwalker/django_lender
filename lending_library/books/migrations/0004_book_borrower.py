# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lender_profile', '0003_remove_patronprofile_borrowed'),
        ('books', '0003_auto_20170118_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='borrowed', to='lender_profile.PatronProfile'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-18 23:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0008_taskworker_auto_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='templateitem',
            name='predecessor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='successors', to='crowdsourcing.TemplateItem'),
        ),
    ]

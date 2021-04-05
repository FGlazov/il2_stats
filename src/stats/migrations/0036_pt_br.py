# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-04-05 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0035_score_ai_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='desc_pt_br',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='award',
            name='title_pt_br',
            field=models.CharField(max_length=256, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='object',
            name='name_pt_br',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='title_pt_br',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]

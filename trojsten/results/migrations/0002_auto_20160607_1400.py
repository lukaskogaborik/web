# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-07 12:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frozenuserresult',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.School', verbose_name='\u0161kola'),
        ),
    ]

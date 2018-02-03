# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 13:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('events', '0001_initial'), ('events', '0002_auto_20160118_1906'), ('events', '0003_auto_20170916_1641'), ('events', '0004_auto_20170916_2053'), ('events', '0005_auto_20170916_2349'), ('events', '0006_auto_20170917_1657'), ('events', '0007_auto_20170917_2343')]

    initial = True

    dependencies = [
        ('people', '0001_initial'),
        ('contests', '0004_auto_20170716_1813'),
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='n\xe1zov')),
                ('start_time', models.DateTimeField(verbose_name='\u010das za\u010diatku')),
                ('end_time', models.DateTimeField(verbose_name='\u010das konca')),
                ('text', models.TextField(blank=True, default='', help_text='Obsah bude prehnan\xfd <a href="http://en.wikipedia.org/wiki/Markdown">Markdownom</a>.')),
            ],
            options={
                'ordering': ['-end_time', '-start_time'],
                'verbose_name': 'akcia',
                'verbose_name_plural': 'akcie',
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='n\xe1zov')),
                ('is_camp', models.BooleanField(verbose_name='s\xfastredko')),
                ('organizers_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='skupina ved\xfacich')),
                ('sites', models.ManyToManyField(blank=True, to='sites.Site')),
            ],
            options={
                'verbose_name': 'typ akcie',
                'verbose_name_plural': 'typy akci\xed',
            },
        ),
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.SmallIntegerField(choices=[(0, '\xfa\u010dastn\xedk'), (1, 'n\xe1hradn\xedk'), (2, 'ved\xfaci')], default=0, verbose_name='typ pozvania')),
                ('going', models.BooleanField(default=True, verbose_name='z\xfa\u010dastnil sa')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event', verbose_name='akcia')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='pou\u017e\xedvate\u013e')),
            ],
            options={'verbose_name': '\xfa\u010dastn\xedk akcie', 'verbose_name_plural': '\xfa\u010dastn\xedci akcie'},
        ),
        migrations.CreateModel(
            name='EventPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='n\xe1zov')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.Address')),
            ],
            options={
                'verbose_name': 'miesto akcie',
                'verbose_name_plural': 'miesta akci\xed',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.EventPlace', verbose_name='miesto'),
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.EventType', verbose_name='typ akcie'),
        ),
        migrations.AlterUniqueTogether(
            name='eventparticipant',
            unique_together=set([('event', 'user')]),
        ),
        migrations.AddField(
            model_name='event',
            name='semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contests.Semester', verbose_name='semester'),
        ),
            migrations.CreateModel(
            name='EventOrganizer',
            fields=[
            ],
            options={
                'verbose_name': 'ved\xfaci akcie',
                'proxy': True,
                'verbose_name_plural': 'ved\xfaci akcie',
            },
            bases=('events.eventparticipant',),
        ),
    ]
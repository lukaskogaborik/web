# Generated by Django 2.1.9 on 2019-10-05 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0018_merge_20191005_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskpeople',
            name='role',
            field=models.IntegerField(choices=[(0, 'opravovateľ'), (1, 'solution writer'), (2, 'recenzovač')], verbose_name='funkcia'),
        ),
        migrations.AlterField(
            model_name='taskpeople',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_people', to='contests.Task', verbose_name='task'),
        ),
    ]

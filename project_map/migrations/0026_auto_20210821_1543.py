# Generated by Django 2.2.18 on 2021-08-21 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_map', '0025_project_rubrics'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='marker1',
            field=models.CharField(max_length=1000, null=True, verbose_name='Координаты долгота'),
        ),
        migrations.AddField(
            model_name='project',
            name='marker2',
            field=models.CharField(max_length=1000, null=True, verbose_name='Координаты широта'),
        ),
    ]

# Generated by Django 2.2.18 on 2021-02-24 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_map', '0002_auto_20210224_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='marker',
            field=models.CharField(blank=True, max_length=10000, null=True, verbose_name='Координаты'),
        ),
        migrations.AlterField(
            model_name='rayon',
            name='coords',
            field=models.CharField(blank=True, max_length=14000, null=True, verbose_name='Coordinates'),
        ),
    ]

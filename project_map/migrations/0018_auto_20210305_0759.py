# Generated by Django 2.2.18 on 2021-03-05 07:59

import any_imagefield.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_map', '0017_auto_20210304_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='marker_im',
            field=any_imagefield.models.fields.AnyImageField(blank=True, null=True, upload_to='', verbose_name='Вид маркера для объекта'),
        ),
    ]

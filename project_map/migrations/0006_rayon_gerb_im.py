# Generated by Django 2.2.18 on 2021-03-02 11:50

import any_imagefield.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_map', '0005_rayoncategory_rayonsubcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='rayon',
            name='gerb_im',
            field=any_imagefield.models.fields.AnyImageField(blank=True, null=True, upload_to='', verbose_name='Gerb Image'),
        ),
    ]

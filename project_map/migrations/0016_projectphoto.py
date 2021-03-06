# Generated by Django 2.2.18 on 2021-03-04 14:07

import any_imagefield.models.fields
from django.db import migrations, models
import django.db.models.deletion
import project_map.utils.media


class Migration(migrations.Migration):

    dependencies = [
        ('project_map', '0015_category_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', any_imagefield.models.fields.AnyImageField(blank=True, null=True, upload_to=project_map.utils.media.get_media_path, verbose_name='Image')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_map.Project', verbose_name='Изображение')),
            ],
        ),
    ]

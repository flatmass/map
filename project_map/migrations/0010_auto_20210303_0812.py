# Generated by Django 2.2.18 on 2021-03-03 08:12

from django.db import migrations, models
import project_map.utils.media


class Migration(migrations.Migration):

    dependencies = [
        ('project_map', '0009_category_category_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_icon',
            field=models.FileField(blank=True, null=True, upload_to=project_map.utils.media.get_media_path, verbose_name='Image'),
        ),
    ]

# Generated by Django 2.2.18 on 2021-07-20 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_map', '0021_auto_20210720_0956'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='completephoto',
            options={'verbose_name': 'Фото готового объекта', 'verbose_name_plural': 'Фотографии готового объекта'},
        ),
        migrations.AlterModelOptions(
            name='projectphoto',
            options={'verbose_name': 'Фото объекта до готовности', 'verbose_name_plural': 'Фотографии объекта до готовности'},
        ),
    ]

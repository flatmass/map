# Generated by Django 2.2.18 on 2021-03-01 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_map', '0003_auto_20210224_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Дополнительная информация'),
        ),
        migrations.AddField(
            model_name='project',
            name='end_project_date',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Срок'),
        ),
        migrations.AddField(
            model_name='project',
            name='financi',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Объем финансирования'),
        ),
        migrations.AddField(
            model_name='project',
            name='vid_rabot',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Вид работ'),
        ),
    ]

# Generated by Django 2.2.18 on 2021-03-02 08:01

import any_urlfield.models.fields
from django.db import migrations, models
import django.db.models.deletion
import project_map.utils.media


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppVariants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favicon', models.ImageField(blank=True, help_text='only *.ico file', null=True, upload_to=project_map.utils.media.get_media_path, verbose_name='favicon')),
                ('logo', models.FileField(blank=True, help_text='the logo of the website', null=True, upload_to=project_map.utils.media.get_media_path, verbose_name='site logo')),
                ('alt_for_logo', models.CharField(blank=True, help_text='the title of the logo', max_length=255, null=True, verbose_name='alt for logo')),
                ('url_for_logo', any_urlfield.models.fields.AnyUrlField(blank=True, max_length=300, null=True, verbose_name='Url for logo')),
                ('title', models.CharField(blank=True, help_text='the title of the site', max_length=255, null=True, verbose_name='site title')),
                ('head_first_title', models.CharField(blank=True, help_text='the title to first block in header', max_length=255, null=True, verbose_name='head first title')),
                ('head_first_description', models.TextField(blank=True, help_text='the description to first block in header', null=True, verbose_name='head first description')),
                ('head_two_title', models.CharField(blank=True, help_text='the title to two block in header', max_length=255, null=True, verbose_name='head two title')),
                ('head_two_description', models.TextField(blank=True, help_text='the description to two block in header', null=True, verbose_name='head two description')),
                ('head_three_title', models.CharField(blank=True, help_text='the title to three block in header', max_length=255, null=True, verbose_name='head three title')),
                ('head_three_description', models.TextField(blank=True, help_text='the description to three block in header', null=True, verbose_name='head three description')),
                ('head_four_title', models.CharField(blank=True, help_text='the title to four block in header', max_length=255, null=True, verbose_name='head four title')),
                ('head_four_description', models.TextField(blank=True, help_text='the description to four block in header', null=True, verbose_name='head four description')),
                ('Image_for_header', models.FileField(blank=True, help_text='the image of the website', null=True, upload_to=project_map.utils.media.get_media_path, verbose_name='Image for header')),
                ('sub_title', models.CharField(blank=True, help_text='the subtitle of the site', max_length=255, null=True, verbose_name='site sub title')),
                ('metrics_code', models.TextField(blank=True, help_text='field metrics, raw html', null=True, verbose_name='Metrics html code')),
                ('socials_code', models.TextField(blank=True, help_text='raw html for socials digging share', null=True, verbose_name='Social share html code')),
                ('extrameta_code', models.TextField(blank=True, help_text='advanced meta tags on raw html', null=True, verbose_name='extra meta html code')),
                ('site', models.OneToOneField(help_text='the name of the site to which the setting applies', on_delete=django.db.models.deletion.CASCADE, to='sites.Site', verbose_name='Site')),
            ],
            options={
                'verbose_name': 'App Variants',
                'verbose_name_plural': 'Apps Variants',
            },
        ),
    ]
# -*- coding: utf-8 -*-
from datetime import datetime
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from fluent_contents.models import PlaceholderField, ContentItemRelation, PlaceholderRelation
from mptt.fields import TreeManyToManyField, TreeForeignKey
from polymorphic.models import PolymorphicModel
from any_imagefield.models import AnyImageField
from polymorphic_tree.models import PolymorphicMPTTModel, PolymorphicTreeForeignKey

from project_map.utils.loader import get_model_string
from project_map.utils.media import get_media_path
import os
from django.template.defaultfilters import filesizeformat
import logging
logger = logging.getLogger('django')


class BaseRubric(PolymorphicMPTTModel):

    parent = PolymorphicTreeForeignKey('self', blank=True, null=True, related_name='children', verbose_name=_('parent'), on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(verbose_name=_('slug'), unique=True, help_text=_("For use into URL"))
    description = models.TextField(verbose_name=_('decription'), null=True, blank=True)
    active = models.BooleanField(default=False, verbose_name=_('active'),
                                 help_text=_("If this flag disable the entity not show on site"))

    def __str__(self):
        return self.title

    def get_slug(self):
        return self.slug

    def get_title(self):
        return self.title

    def get_parent_id(self):
        return self.parent.id if self.parent else None

    class Meta(PolymorphicMPTTModel.Meta):
        app_label = 'project_map'
        #abstract = False
        verbose_name = _("Base Rubric")
        verbose_name_plural = _("Base Rubrics")


class Rubric(BaseRubric):

    class Meta: #(BaseRubric.Meta)
        app_label = 'project_map'
        #abstract = True
        verbose_name = _("Rubric")
        verbose_name_plural = _("Rubrics")


class Rayon(models.Model):
    title = models.CharField(_("Rayon"), max_length=1000)
    adress = models.CharField(_("Adress"), max_length=1000, null=True, blank=True)
    coords = models.CharField(_("Coordinates"), max_length=14000, null=True, blank=True)
    gerb_im = AnyImageField(_('Gerb Image'), blank=True, null=True)
    full_objects_count = models.CharField("Всего объектов", max_length=1000, null=True, blank=True)
    full_investments = models.CharField("Общий объем финансирования", max_length=1000, null=True, blank=True)
    infografika_im = AnyImageField(_('Инфографика'), blank=True, null=True)
    mobile_infografika_im = AnyImageField(_('Инфографика для мобильной версии'), blank=True, null=True)

    class Meta:
        app_label = 'project_map'
        verbose_name = _('Rayon')
        verbose_name_plural = _('Rayones')

    def __str__(self):
        return self.title or u'Rayon'

class RayonCategory(models.Model):
    rayon = models.ForeignKey(Rayon, related_name='rayon', on_delete=models.CASCADE)
    #category_icon = AnyImageField(_('Image'), upload_to=get_media_path, blank=True, null=True)
    category_name = models.CharField("Наименование категории", max_length=1000, null=True, blank=True)
    objects_count = models.CharField("Количество объектов", max_length=1000, null=True, blank=True)
    investments = models.CharField("Объем инвестиций", max_length=1000, null=True, blank=True)

class RayonSubCategory(models.Model):
    rayon_category = models.ForeignKey(RayonCategory, related_name='rayon_category', on_delete=models.CASCADE)
    #category_icon = AnyImageField(_('Image'), upload_to=get_media_path, blank=True, null=True)
    category_name = models.CharField("Наименование подкатегории", max_length=1000, null=True, blank=True)
    objects_count = models.CharField("Количество объектов", max_length=1000, null=True, blank=True)
    investments = models.CharField("Объем инвестиций", max_length=1000, null=True, blank=True)

class Category(models.Model):
    title = models.CharField(_("Category"), max_length=1000)
    color = models.CharField("Цвет", max_length=14, blank=True, null=True)
    marker_im = AnyImageField(_('Image'), blank=True, null=True)
    category_icon = models.FileField(_('Image'), upload_to=get_media_path, blank=True, null=True)
    count = models.IntegerField("Позиция в сортировке", default=1)
    active = models.BooleanField("Активный", default=True)

    class Meta:
        app_label = 'project_map'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title or u'Category'

class Project(models.Model):
    rayon = models.ForeignKey(Rayon, verbose_name=_('Rayon'), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=_('Category'), on_delete=models.CASCADE)
    rubrics = TreeManyToManyField(
        get_model_string('BaseRubric'),
        related_name='related_entities',
        verbose_name=_('rubrics'),
        blank=True)

    title = models.CharField(_("Project title"), max_length=1000)
    adress = models.CharField(_("Adress"), max_length=1000)
    vid_rabot = models.CharField("Вид работ", max_length=1000, null=True, blank=True)
    financi = models.IntegerField("Объем финансирования", null=True, blank=True)
    end_project_date = models.CharField("Срок", max_length=1000, null=True, blank=True)
    description = models.TextField("Дополнительная информация", null=True, blank=True)
    marker_im = AnyImageField("Вид маркера для объекта", blank=True, null=True)
    marker = models.CharField("Координаты", max_length=10000,help_text='Координаты должны быть типа [50.388111,36.880136], обязательно в квадратных скобках и без пробелов')
    marker1 = models.CharField("Координаты долгота", max_length=1000, help_text='', null=True)
    marker2 = models.CharField("Координаты широта", max_length=1000, help_text='', null=True)
    complete = models.BooleanField('Проект выполнен', default=False)
    on_main = models.BooleanField('Отображать на главной', default=False)

    class Meta:
        app_label = 'project_map'
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.title or u'Project'

class ProjectPhoto(models.Model):
    project = models.ForeignKey(Project, verbose_name="Изображение", related_name='images', on_delete=models.CASCADE)
    image = AnyImageField(_('Image'), upload_to=get_media_path, blank=True, null=True)

    class Meta:
        verbose_name = "Фото объекта до готовности"
        verbose_name_plural = 'Фотографии объекта до готовности'


class CompletePhoto(models.Model):
    project = models.ForeignKey(Project, verbose_name="Изображение", related_name='completeimages', on_delete=models.CASCADE)
    image = AnyImageField(_('Image'), upload_to=get_media_path, blank=True, null=True)

    class Meta:
        verbose_name = "Фото выполненного объекта"
        verbose_name_plural = 'Фотографии выполненного объекта'
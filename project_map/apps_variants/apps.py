#-*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class VariantsAppConfig(AppConfig):
    name = 'project_map.apps_variants'
    verbose_name = _('App vars') # А здесь, имя которое необходимо отобразить в админке
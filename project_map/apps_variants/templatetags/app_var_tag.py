# -*- coding: UTF-8 -*-
from django import template
from django.contrib.sites.shortcuts import get_current_site

#from forms.filter_form import filter_form
from project_map.apps_variants.models import AppVariants

_disable_redirection = 'disable_redirection'

register=template.Library()

@register.simple_tag(takes_context=True) # регистрируем тег
def app_var_tag(context):
    if AppVariants.objects.filter(site_id=get_current_site(context).id):
        items = AppVariants.objects.get(site_id=get_current_site(context).id)
        return {
            'items': items,
        }
    return None

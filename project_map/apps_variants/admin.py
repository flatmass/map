# -*- coding: utf-8 -*-

from django.contrib import admin
from project_map.apps_variants.forms import AppVariantsAdminForm
from .models import AppVariants



class AppVariantsAdmin(admin.ModelAdmin):
    form = AppVariantsAdminForm


admin.site.register(AppVariants, AppVariantsAdmin)

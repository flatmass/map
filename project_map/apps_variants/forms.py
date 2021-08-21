# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import AppVariants
from ckeditor.widgets import CKEditorWidget

class AppVariantsAdminForm(forms.ModelForm):

    class Meta:
        #model = AppVariants
        fields = '__all__'
        widgets = {
            'footer_title': CKEditorWidget(),
        }


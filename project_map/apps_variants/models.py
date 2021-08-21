# -*- coding: utf-8 -*-
import datetime
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.sites.models import Site
from any_urlfield.models import AnyUrlField
from project_map.utils.media import get_media_path


class AppVariants(models.Model):
    # ========================================================================================================
    # SITE
    # ========================================================================================================
    site = models.OneToOneField(Site, verbose_name=_('Site'), help_text=_('the name of the site to which the setting applies'), on_delete=models.CASCADE)
    favicon = models.ImageField(_('favicon'), upload_to=get_media_path, blank=True, null=True,
                                help_text=_('only *.ico file'))
    logo = models.FileField(_("site logo"), upload_to=get_media_path, blank=True, null=True, help_text=_('the logo of the website'))
    mobile_logo = models.FileField(_("Mobile site logo"), upload_to=get_media_path, blank=True, null=True,
                            help_text=_('the mobile logo of the website'))
    alt_for_logo = models.CharField(_("alt for logo"), blank=True, max_length=255, null=True,
                             help_text=_('the title of the logo'))
    url_for_logo = AnyUrlField(_('Url for logo'), null=True, blank=True)
    title = models.CharField(_("site title"), blank=True, max_length=255, null=True, help_text=_('the title of the site'))

    head_first_title = models.CharField(_("head first title"), blank=True, null=True, max_length=255,
                                 help_text=_('the title to first block in header'))
    head_first_description = models.TextField(_("head first description"), blank=True, null=True,
                                 help_text=_('the description to first block in header'))

    head_two_title = models.CharField(_("head two title"), blank=True, null=True, max_length=255,
                                        help_text=_('the title to two block in header'))
    head_two_description = models.TextField(_("head two description"), blank=True, null=True,
                                              help_text=_('the description to two block in header'))

    head_three_title = models.CharField(_("head three title"), blank=True, null=True, max_length=255,
                                      help_text=_('the title to three block in header'))
    head_three_description = models.TextField(_("head three description"), blank=True, null=True,
                                            help_text=_('the description to three block in header'))

    head_four_title = models.CharField(_("head four title"), blank=True, null=True, max_length=255,
                                        help_text=_('the title to four block in header'))
    head_four_description = models.TextField(_("head four description"), blank=True, null=True,
                                              help_text=_('the description to four block in header'))

    Image_for_header = models.FileField(_("Image for header"), upload_to=get_media_path, blank=True, null=True,
                              help_text=_('the image of the website'))
    Lead_post = models.CharField(_("Lead post "), blank=True, null=True, max_length=255,
                                 help_text='Должность')

    sub_title = models.CharField(_("site sub title"), blank=True, null=True, max_length=255,
                                 help_text=_('the subtitle of the site'))

    footer_title = models.TextField(_("footer title"), blank=True, null=True,
                                     help_text=_('title info, only char, not html tag!'))
    metrics_code = models.TextField(_('Metrics html code'), blank=True, null=True, help_text=_('field metrics, raw html'))
    socials_code = models.TextField(_('Social share html code'), blank=True, null=True, help_text=_('raw html for socials digging share'))
    extrameta_code = models.TextField(_("extra meta html code"), blank=True, null=True, help_text=_('advanced meta tags on raw html'))

    def __str__(self):
        return self.title or self.site.name


    class Meta:
        # abstract = True
        app_label = 'apps_variants'
        verbose_name = _('App Variants')
        verbose_name_plural = _('Apps Variants')
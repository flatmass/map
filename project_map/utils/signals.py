from django.db.models.signals import post_save
from django.core.cache import cache
from notifications.signals import notify
from mb_base.business_models.service.models import Service
from mb_base.pages.categorypage.models import CategoryPage
from mb_base.pages.entitypage.models import EntityPage
from mb_base.pages.simplepage.models import SimplePage

from mb_base.ticket.models import List_tikets


def invalidate_page_cache(sender, **kwargs):
    # invalidate cache
    cache.delete(sender.get_absolute_url()) # or any other pertinent keys

post_save.connect(invalidate_page_cache, sender=SimplePage)
post_save.connect(invalidate_page_cache, sender=EntityPage)
post_save.connect(invalidate_page_cache, sender=CategoryPage)


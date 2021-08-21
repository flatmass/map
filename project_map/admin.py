from django.utils.translation import ugettext_lazy as _
from polymorphic_tree.admin import PolymorphicMPTTChildModelAdmin, PolymorphicMPTTParentModelAdmin

from project_map import models
from django.contrib import admin
from fluent_contents.admin import PlaceholderFieldAdmin
#from salmonella.admin import SalmonellaMixin
#from salmonella.filters import SalmonellaFilter
from django.contrib.admin.options import IS_POPUP_VAR
from django.utils.html import format_html
#from sorl.thumbnail import get_thumbnail
#from polymorphic_tree.admin import PolymorphicMPTTParentModelAdmin, PolymorphicMPTTChildModelAdmin
import nested_admin
from project_map.models import RayonCategory, RayonSubCategory, ProjectPhoto, CompletePhoto



class RubricAdmin(PolymorphicMPTTChildModelAdmin):
    base_model = models.BaseRubric
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Rubric, RubricAdmin)

class BaseRubricAdmin(PolymorphicMPTTParentModelAdmin):
    base_model = models.BaseRubric
#v    child_models = ((Rubric, RubricAdmin),)
    child_models = (models.Rubric,)   #V
    search_fields = ('title',)
    list_filter = ('active',)
    list_display = ('title', 'active',)
    """
    def get_sort_description(self, obj):
        if obj.parent and obj.parent.title != obj.title:
            if not hasattr(self, '_Page__sort_description'):
                self.__sort_description = (Truncator(self.get_sort_description(obj.parent)).chars(obj.level * 16 ))
            return u'%s/%s' % (self.__sort_description, obj.title)

        return u'%s' % obj.title

    get_sort_description.short_description = _('title')
    get_sort_description.admin_order_field = 'title'
    """

admin.site.register(models.BaseRubric, BaseRubricAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Category, CategoryAdmin)


class RayonSubCategoryAdmin(nested_admin.NestedStackedInline):
    model = RayonSubCategory
    extra = 0

class RayonCategoryAdmin(nested_admin.NestedTabularInline):
    model = RayonCategory
    extra = 0
    inlines = [RayonSubCategoryAdmin]


class RayonAdmin(nested_admin.NestedModelAdmin):
    fieldsets = (
        (_(''), {
            'fields': (
            'title', 'adress', 'coords', 'gerb_im', 'full_objects_count', 'full_investments', 'infografika_im', 'mobile_infografika_im')
        }),
    )

    inlines = [RayonCategoryAdmin,]

admin.site.register(models.Rayon, RayonAdmin)

class ProjectPhotoAdmin(admin.TabularInline):
    model = ProjectPhoto
    extra = 0

class CompletePhotoAdmin(admin.TabularInline):
    model = CompletePhoto
    extra = 0

class ProjectAdmin(PlaceholderFieldAdmin):
    list_display = ('title', 'adress', 'category', 'marker', 'on_main')
    search_fields = ('title', 'adress')
    list_filter = ('rayon', 'category', 'rubrics', 'complete', 'on_main')
    inlines = [ProjectPhotoAdmin, CompletePhotoAdmin]
    #filter_horizontal = ('rayon', 'category')

admin.site.register(models.Project, ProjectAdmin)



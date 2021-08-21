"""project_map URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

from project_map.views import ProjectsView, RayonApiView, Projects_listView, Project_addView, \
    Complete_projects_listView, AddAnswerWizard, FORMS

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rayon/', RayonApiView, name='rayon'),
    url(r'^projects-list/', Projects_listView, name='projects_list'),
    url(r'^complete-projects-list/', Complete_projects_listView, name='complete_projects_list'),
    url(r'^_nested_admin/', include('nested_admin.urls')),
    url(r'^projectview/', Project_addView, name='projectview'),
    url(r'^form', AddAnswerWizard.as_view(FORMS),name='forms'),
    url(r'^', ProjectsView, name='projects'),
]
if settings.DEBUG:
    urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
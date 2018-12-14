"""sandbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home
from file_download.views import bibtex_reference_download
from forms.views import forms_index
from tables.views import people
from template_engine.views import jinja_engine
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bibtex/<item_id>', bibtex_reference_download, name='bibtex'),
    path('forms/', forms_index, name='forms'),
    path('tables/', people, name='tables'),
    path('template_engine/jinja/', jinja_engine, name='template_engine_jinja'),
    path('', home, name='home'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + urlpatterns

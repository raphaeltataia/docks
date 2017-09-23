from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateCompanyView, CreateDockView, DetailDockView

urlpatterns = [
    url(r'^companys/$', CreateCompanyView.as_view(), name="create"),
    url(r'^docks/$', CreateDockView.as_view(), name="create"),
    url(r'^docks/(?P<company_id>[0-9]+)$', DetailDockView.as_view(), name="Dock Informations"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
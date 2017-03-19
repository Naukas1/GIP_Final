"""GIP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import include, url
from HistoriaClinica import views as historiaclinica_view
from django.contrib import admin

from .views import (
    historiaclinica_detalle,
    historiaclinica_crear,
    historiaclinica_lista,
    historiaclinica_update,
    historiaclinica_borrar,
)

urlpatterns = [
    url(r'^$', historiaclinica_lista, name="lista"),
    url(r'^crear/$', historiaclinica_crear, name="crear"),
    url(r'^(?P<id>\d+)/$', historiaclinica_detalle, name='detalle'),
    url(r'^(?P<id>\d+)/update/$', historiaclinica_update, name="update"),
    url(r'^(?P<id>\d+)/borrar/$', historiaclinica_borrar, name="borrar"),
]
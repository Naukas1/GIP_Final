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
from Contactos import views as contactos_view
from django.contrib import admin

from .views import (
    contactos_lista,
    contactos_crear,
    contactos_detalle,
    contactos_update,
    contactos_borrar,
)

urlpatterns = [
    url(r'^$', contactos_lista),
    url(r'^crear/$', contactos_crear),
    url(r'^detalle/(?P<id>\d+)$', contactos_detalle),
    url(r'^update/$', contactos_update),
    url(r'^borrar/$', contactos_borrar),

]
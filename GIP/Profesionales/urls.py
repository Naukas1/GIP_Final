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
# from Profesionales import views as profesionales_views

from .views import (
    profesionales_lista,
    # profesionales_crear,
    profesionales_detalle,
    profesionales_editar,
    # profesionales_borrar,
)

urlpatterns = [
    url(r'^$', profesionales_lista, name="lista"),
    # url(r'^crear/$', contactos_crear),
    url(r'^(?P<id>\d+)/$', profesionales_detalle, name='detalle'),
    url(r'^(?P<id>\d+)/editar/$', profesionales_editar, name="editar"),
    # url(r'^(?P<id>\d+)/borrar/$', contactos_borrar),

]
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$',views.socio_list),
    url(r'^importe',views.importe_list),
    url(r'^pago', views.pago_list),
    url(r'^nuevoSocio', views.nuevoSocio, name='nuevoSocio'),
    url(r'^search/$', views.search),
    #url(r'^socioEditar', views.socioEditar),
    url(r'^socioEditar/(?P<pk>[0-9]+)', views.socioEditar, name='socioEditar'),
    url(r'^socioEliminar/(?P<pk>[0-9]+)', views.socioEliminar, name='socioEliminar'),
    url(r'^nuevoImporte', views.importeNuevo, name='importeNuevo'),
    url(r'^nuevoPago', views.pagoNuevo, name='pagoNuevo'),
    url(r'^editarPago/(?P<pk>[0-9]+)', views.pagoEditar, name='pagoEditar'),
    url(r'^eliminarPago/(?P<pk>[0-9]+)', views.pagoEliminar, name='pagoEliminar'),
    url(r'^editarImporte/(?P<pk>[0-9]+)', views.importeEditar, name='importeEditar'),
    url(r'^eliminarImporte/(?P<pk>[0-9]+)', views.importeEliminar, name='importeEliminar'),

    ]
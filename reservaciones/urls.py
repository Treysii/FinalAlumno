from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^$', views.lista),

    url(r'^store/$', views.store, name='store'),
    url(r'^home/$', views.home, name='home'),



    url(r'^habitacion/$', views.habitacion_nueva, name='habitacion_nueva'),


    url(r'^habitac/$', views.lista_habitacion, name ='lista_habitacion'),
    url(r'^detalles/(?P<pk>[0-9]+)/$', views.habitacion_detalle, name='habitacion_detalle'),
    url(r'^edit/(?P<pk>[0-9]+)/edit/$', views.habitacion_editar, name='habitacion_editar'),
    url(r'^borrar/(?P<pk>\d+)/remove/$', views.habitacion_eliminar, name='habitacion_eliminar'),


    url(r'^hu/$', views.lista_huesped, name ='lista_huesped'),
    url(r'^reservacion/nuevo/$', views.reservacion_nueva, name='reservacion_nueva'),
    url(r'^huesped/(?P<pk>[0-9]+)/edit/$', views.huesped_editar, name='huesped_editar'),
    url(r'^detalles/(?P<pk>[0-9]+)/$', views.huesped_detalle, name='huesped_detalle'),
    url(r'^b/(?P<pk>\d+)/r/$', views.huesped_eliminar, name='huesped_eliminar'),
    ]

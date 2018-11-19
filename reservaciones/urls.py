from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^$', views.lista),

    url(r'^store/$', views.store, name='store'),
    url(r'^home/$', views.home, name='home'),



    url(r'^habitacion/$', views.materia_nueva, name='materia_nueva'),


    url(r'^habitac/$', views.lista_materia, name ='lista_materia'),
    url(r'^detalles/(?P<pk>[0-9]+)/$', views.materia_detalle, name='materia_detalle'),
    url(r'^edit/(?P<pk>[0-9]+)/edit/$', views.materia_editar, name='materia_editar'),
    url(r'^borrar/(?P<pk>\d+)/remove/$', views.materia_eliminar, name='materia_eliminar'),


    url(r'^hu/$', views.lista_grado, name ='lista_grado'),
    url(r'^reservacion/nuevo/$', views.asignacion_nueva, name='asignacion_nueva'),
    url(r'^huesped/(?P<pk>[0-9]+)/edit/$', views.grado_editar, name='grado_editar'),
    #url(r'^detalles/(?P<pk>[0-9]+)/$', views.grado_detalle, name='grado_detalle'),
    #url(r'^b/(?P<pk>\d+)/r/$', views.grado_eliminar, name='grado_eliminar'),
    ]

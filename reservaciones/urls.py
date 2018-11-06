from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^$', views.lista),
    url(r'^reservacion/nuevo/$', views.reservacion_nueva, name='reservacion_nueva'),
    url(r'^store/$', views.store, name='store'),
    url(r'^home/$', views.home, name='home'),
    url(r'^ver/$', views.verlo,name='verlo'),
    url(r'^edit/$', views.editar, name='editar'),
    url(r'^borrador/$', views.borrador, name='borrador'),
    url(r'^habitacion/$', views.habitacion_nueva, name='habitacion_nueva'),
    ]

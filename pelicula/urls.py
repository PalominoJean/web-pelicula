from django.conf.urls import include, url
from pelicula import views


urlpatterns=[
    url(r'^$', views.lista_fechaPublicacion,name='lista_fechaPublicacion'),
    url(r'^(?P<pelicula_pk>[0-9]+)/$',views.lista_pelicula,name='lista_pelicula'),
]
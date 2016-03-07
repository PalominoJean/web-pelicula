from django.conf.urls import include, url
from pelicula import views


urlpatterns=[
    url(r'^$', views.lista_fechaAdicion,name='lista_fechaAdicion'),

]

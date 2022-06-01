from django.urls import path 
from . import views




urlpatterns = [
    
    path("", views.inicio),
    path("novelas", views.novelas),
    path("comics", views.comics),
    path("mangas", views.mangas),
    path("alta_novelas", views.novelas_formulario),
    path("alta_comics", views.comics_formulario),
    path("alta_mangas", views.mangas_formulario),
    path("buscar_novelas", views.buscar_novelas),
    path("buscar_comics", views.buscar_comics),
    path("buscar_mangas", views.buscar_mangas),
    path("busqueda_novelas", views.busqueda_novelas),
    path("busqueda_comics", views.busqueda_comics),
    path("busqueda_mangas", views.busqueda_mangas), 

]

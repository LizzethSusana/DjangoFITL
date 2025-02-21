from django.urls import path
from . views import *

urlpatterns = [
    path('api/get', lista_categorias, name='lista'),
    path('ver/', ver_categorias, name='ver_categoria'),
    path('agregar/', agregar_categoria, name='agregar_categoria'),
    path('api/post/', registrar_categoria, name='post_categoria'),
]

from django.contrib import admin
from django.urls import include, path
from dororo.views import insertarPartesCuerpo, insertarUbicaciones, insertarDemonios, insertarPeleas, insertarArticulosDororo, editarDemonios, listarFaltantesCuerpo, listarArticulosDororo, editarArticulos, delete, deleteParte,  printArticulos

urlpatterns = [
    path('', listarArticulosDororo.as_view(),  name="home"),
    path('listarPartesCuerpo', listarFaltantesCuerpo.as_view(), name="listarPartesCuerpo"),

    path('insertarPartesCuerpo', insertarPartesCuerpo.as_view(), name='PartesCuerpo'),
    path('insertarUbicaciones', insertarUbicaciones.as_view(), name='Ubicaciones'),
    path('insertarDemonios', insertarDemonios.as_view(), name='Demonios'),
    path('insertarPeleas', insertarPeleas.as_view(), name='Peleas'),
    path('insertarArticulosDororo', insertarArticulosDororo.as_view(), name='Articulos'),
    
    path('ver/<int:pk>', editarDemonios.as_view(), name="ver"),
    path('articulos/delete/<int:pk>', delete.as_view(), name="delete"),
    path('demonios/delete/<int:pk>', deleteParte.as_view(), name="partesDelete"),
    path('articulos/ver/<int:pk>', editarArticulos.as_view(), name="verArticulos"),

    path('home/printArticulos', printArticulos, name="printArticulos"),

]
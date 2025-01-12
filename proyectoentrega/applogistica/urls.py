from django.urls import path
from .views import  index, tractores, tractor_formulario, buscar_tractor, semis, semi_formulario, buscar_semi, choferes, chofer_formulario


urlpatterns=[

    path('inicio', index, name="inicio"),
    path('tractores', tractores, name="tractores"),
    path('tractor-nuevo', tractor_formulario, name="tractor_formulario"),
    path('tractor-buscar', buscar_tractor, name="buscar_tractor"),
    path('semis', semis, name="semis"),
    path('semi-nuevo', semi_formulario, name="semi_formulario"),
    path('semi-buscar', buscar_semi, name="buscar_semi"),
    path('choferes', choferes, name="choferes"),
    path('chofer-nuevo', chofer_formulario, name="chofer_formulario"),




]
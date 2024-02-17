""" urls especificas de esta app"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('gestion/', views.gestion ),
    path('registrarCurso/', views.registrarCurso),
    path('eliminar/<codigo>', views.eliminar),
    path('editar/<codigo>', views.formEditar),
    path('guardarEdicion/', views.guardarEdicion),
]
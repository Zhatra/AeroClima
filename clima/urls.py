"""
Archivo de configuración de URL para la aplicación 'clima' en el proyecto 'AeroClima'.

Este archivo contiene las definiciones de las rutas URL para esta aplicación,
permitiendo la asociación de funciones de vista o clases de vista con
las URL específicas. 
"""

from django.urls import path
from . import views  # Importación de las vistas desde el módulo actual

urlpatterns = [
    # Ruta para la vista inicial del proyecto, dirigida a la función 'inicio' en el módulo 'views'.
    path("", views.inicio, name="inicio"),
]
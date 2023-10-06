"""
Configuración de URLs del proyecto AeroClima.

Este archivo define las rutas a nivel de proyecto. Para más información sobre cómo configurar
las rutas en Django, puedes visitar:
https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""

from django.urls import path, include

urlpatterns = [
    # Incluye las rutas definidas en la aplicación 'clima'
    path("", include("clima.urls")),
]
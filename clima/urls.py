from django.urls import path

# Importa todas las funciones y clases del módulo "views" de la misma carpeta (indicado por el punto).
from . import views

# Define una lista llamada "urlpatterns" que contiene todas las rutas para esta aplicación.
urlpatterns = [
    # Define una ruta que se activa cuando se accede a la URL raíz (es decir, "").
    # Cuando se accede a esta URL, se llama a la función "index" del módulo "views".
    # Además, se le da un nombre "index" a esta ruta para poder referenciarla en otras partes del proyecto.
    path("", views.index, name="index"),
]

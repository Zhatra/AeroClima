"""
Configuración WSGI para el proyecto AeroClima.

Este módulo configura el sistema WSGI que hace de interfaz entre el servidor web y la aplicación Django.
Expone el callable WSGI como una variable a nivel de módulo llamada ``application``.

Para más información sobre este archivo, consulte:
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

# Importa el módulo os para interactuar con el sistema operativo
import os

# Importa la función get_wsgi_application de Django
from django.core.wsgi import get_wsgi_application

# Establece el módulo de configuración predeterminado para esta aplicación.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AeroClima.settings')

# Obtiene la aplicación WSGI para este proyecto.
application = get_wsgi_application()

# Alias para la aplicación WSGI, proporcionando otra manera de referenciar la aplicación WSGI.
app = application

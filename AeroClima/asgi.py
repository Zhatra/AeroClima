"""
Configuración ASGI para el proyecto AeroClima.

Este módulo expone la aplicación ASGI a través de una variable a nivel de módulo llamada ``application``.

Para más información sobre este archivo, consulte la documentación oficial de Django:
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Establece el módulo de configuración de Django predeterminado para este proyecto.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AeroClima.settings')

# Obtiene la aplicación ASGI para este proyecto y la asigna a la variable 'application'.
application = get_asgi_application()

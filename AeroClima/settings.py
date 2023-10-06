"""
Configuraciones del Proyecto AeroClima en Django.

Este archivo fue generado mediante el comando 'django-admin startproject' y está basado en Django 4.2.5.
Contiene las configuraciones esenciales para el funcionamiento adecuado del proyecto AeroClima.

Para obtener más información sobre este archivo, puedes consultar:
https://docs.djangoproject.com/en/4.2/topics/settings/

Para una lista completa de configuraciones y sus valores, puedes visitar:
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

# Importaciones necesarias para la configuración del proyecto
from pathlib import Path
import os
from decouple import config

# Definición de la ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración de seguridad
# Es crucial mantener la llave secreta en un lugar seguro en un entorno de producción
SECRET_KEY = 'django-insecure-53&mgw(nv*a9w%@q7_5^f8+7&z!)c)w=k78!6xdj%mpm6(&tix'

# Configuración de la API de OpenWeatherMap
# La llave de API se obtiene desde un archivo .env por defecto, pero se puede reemplazar directamente aquí
OPENWEATHERMAP_API_KEY = config('OPENWEATHERMAP_API_KEY', default='tu_llave_aqui')

# Configuración de desarrollo - no es adecuada para un entorno de producción
DEBUG = True
ALLOWED_HOSTS = ['.vercel.app', '127.0.0.1']

# Definición de las aplicaciones instaladas y configuración de middleware
INSTALLED_APPS = [
    # Aplicaciones predeterminadas de Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Aplicación personalizada 'clima'
    'clima.apps.ClimaConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de la URL raíz y las plantillas
ROOT_URLCONF = 'AeroClima.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'AeroClima.wsgi.application'

# Configuración de internacionalización
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configuración de archivos estáticos y multimedia
STATIC_URL = '/static/'
MEDIA_URL = '/images/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
STATIC_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Configuración de campo de clave primaria predeterminada
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

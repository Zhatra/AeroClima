"""
Módulo de Vistas de la Aplicación Clima en el Proyecto AeroClima.

Este módulo define las vistas que gestionan la lógica de la aplicación,
incluyendo la obtención y presentación de datos del clima.

"""
# Importaciones necesarias
from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.conf import settings
import pandas as pd
from django.core.cache import cache
import Levenshtein
from .constants import CODIGOS_IATA, IMAGENES, CODIGO_IMG

def obtener_desde_cache_o_api(url: str) -> dict:
    """
    Obtiene datos desde caché o, si no están disponibles, desde la API especificada.

    Parámetros:
        url (str): La URL de la API.

    Retorno:
        dict: Los datos obtenidos.
    """
    clave_cache = f"api_cache_{url}"
    respuesta_cache = cache.get(clave_cache)

    if respuesta_cache:
        return respuesta_cache

    respuesta = requests.get(url)
    datos = respuesta.json()
    cache.set(clave_cache, datos, 21600)

    return datos

def obtener_clima(nombre_ciudad: str) -> dict:
    """
    Obtiene los datos del clima para una ciudad específica.

    Parámetros:
        nombre_ciudad (str): El nombre de la ciudad.

    Retorno:
        dict: Los datos del clima.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={nombre_ciudad}&appid={settings.OPENWEATHERMAP_API_KEY}&units=metric&lang=es"
    datos = obtener_desde_cache_o_api(url)

    if 'weather' in datos and datos['weather']:
        icono_clima = datos['weather'][0]['main']
        if icono_clima not in CODIGO_IMG:
            icono_clima = 'Else'
        datos['weather_icon'] = IMAGENES[icono_clima]
        return datos
    return None

def consultar_clima(latitud: str, longitud: str) -> dict:
    """
    Consulta los datos del clima basados en la latitud y longitud proporcionadas.

    Parámetros:
        latitud (str): La latitud de la ubicación.
        longitud (str): La longitud de la ubicación.

    Retorno:
        dict: Los datos del clima.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={settings.OPENWEATHERMAP_API_KEY}&units=metric&lang=es"
    datos = obtener_desde_cache_o_api(url)

    icono_clima = datos['weather'][0]['main']
    if icono_clima not in CODIGO_IMG:
        icono_clima = 'Else'
    datos['weather_icon'] = IMAGENES[icono_clima]
    return datos

def obtener_ciudad_desde_iata(codigo: str) -> str:
    """
    Obtiene el nombre de una ciudad a partir de su código IATA.

    Parámetros:
        codigo (str): El código IATA.

    Retorno:
        str: El nombre de la ciudad.
    """
    ciudad = CODIGOS_IATA.get(codigo.upper())

    if ciudad:
        return ciudad

    distancia_minima = float('inf')
    ciudad_mas_cercana = None

    for nombre_ciudad in CODIGOS_IATA.values():
        distancia = Levenshtein.distance(codigo.lower(), nombre_ciudad.lower())
        if distancia < distancia_minima:
            distancia_minima = distancia
            ciudad_mas_cercana = nombre_ciudad

    if distancia_minima <= 3:
        return ciudad_mas_cercana

    return codigo

def inicio(request):
    """
    Vista principal para obtener y mostrar los datos del clima.

    Parámetros:
        request: Objeto HttpRequest con los datos de la solicitud.

    Retorno:
        HttpResponse: Objeto HttpResponse con los datos de la respuesta.
    """
    nombre_ciudad1 = obtener_ciudad_desde_iata(request.GET.get('ciudad_nombre_1', ''))
    nombre_ciudad2 = obtener_ciudad_desde_iata(request.GET.get('ciudad_nombre_2', ''))
    datos_clima1 = {}
    datos_clima2 = {}
    clima_origen = {}
    clima_destino = {}
    es_busqueda_ticket = False
    mensaje_error = None

    if nombre_ciudad1:
        datos_clima1 = obtener_clima(nombre_ciudad1)
    if nombre_ciudad2:
        datos_clima2 = obtener_clima(nombre_ciudad2)

    if request.method == 'POST':
        numero_ticket = request.POST['numero_ticket']

        if numero_ticket:
            es_busqueda_ticket = True
            df = pd.read_csv('dataset2.csv')
            filas_datos_ticket = df[df['num_ticket'] == numero_ticket]
            if not filas_datos_ticket.empty:
                datos_ticket = filas_datos_ticket.iloc[0]

                clima_origen = consultar_clima(
                    datos_ticket['origin_latitude'], datos_ticket['origin_longitude'])
                clima_destino = consultar_clima(
                    datos_ticket['destination_latitude'], datos_ticket['destination_longitude'])
            else:
                mensaje_error = "Por favor, ingrese un número de ticket válido."
    else:
        if not datos_clima1 and nombre_ciudad1:
            mensaje_error = "Por favor, ingrese una ciudad de origen válida."
        if not datos_clima2 and nombre_ciudad2:
            mensaje_error = "Por favor, ingrese una ciudad de destino válida."

    return render(request, 'clima/clima.html', {
        'datos_clima1': datos_clima1,
        'datos_clima2': datos_clima2,
        'clima_origen': clima_origen,
        'clima_destino': clima_destino,
        'es_busqueda_ticket': es_busqueda_ticket,
        'mensaje_error': mensaje_error
    })
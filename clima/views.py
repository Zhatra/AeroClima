# Importaciones necesarias
from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.conf import settings
import pandas as pd
from django.core.cache import cache
import Levenshtein
from .constants import IATA_CODES, IMAGES, PIC_CODE

# Función para obtener datos de una API, usando caché para mejorar la eficiencia
def fetch_from_cache_or_api(url):
    # Usa la URL como clave para el caché
    cache_key = f"api_cache_{url}"
    cached_response = cache.get(cache_key)

    # Si la respuesta ya está en caché, la retorna
    if cached_response:
        return cached_response

    # Si no está en caché, realiza la llamada a la API
    response = requests.get(url)
    data = response.json()
    print(data)

    # Guarda la respuesta en caché por 6 horas (21600 segundos)
    cache.set(cache_key, data, 21600)

    return data

# Función para obtener el clima de una ciudad específica
def get_weather(city_name):
    # Construye la URL para la API de OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={settings.OPENWEATHERMAP_API_KEY}&units=metric&lang=es"
    data = fetch_from_cache_or_api(url)

    # Si la respuesta contiene información del clima, procesa y retorna los datos
    if 'weather' in data and data['weather']:
        icon_pic = data['weather'][0]['main']
        if icon_pic not in PIC_CODE:
            icon_pic = 'Else'
        data['weather_icon'] = IMAGES[icon_pic]
        return data
    return None

# Función para consultar el clima basado en latitud y longitud
def consultar_clima(latitud, longitud):
    # Construye la URL para la API de OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={settings.OPENWEATHERMAP_API_KEY}&units=metric&lang=es"
    data = fetch_from_cache_or_api(url)

    # Procesa y retorna los datos del clima
    icon_pic = data['weather'][0]['main']
    if icon_pic not in PIC_CODE:
        icon_pic = 'Else'
    data['weather_icon'] = IMAGES[icon_pic]
    return data

# Función para obtener el nombre de una ciudad a partir de su código IATA
def get_city_from_iata(code):
    # Intenta obtener el nombre de la ciudad directamente del diccionario
    city = IATA_CODES.get(code.upper())

    if city:
        return city

    # Si no encuentra el código, busca la ciudad más parecida usando la distancia de Levenshtein
    min_distance = float('inf')
    closest_city = None

    for city_name in IATA_CODES.values():
        distance = Levenshtein.distance(code.lower(), city_name.lower())
        if distance < min_distance:
            min_distance = distance
            closest_city = city_name

    # Si la distancia es pequeña (1 o 2), considera que es una coincidencia cercana
    if min_distance <= 3:
        return closest_city

    # Si no encuentra una coincidencia cercana, retorna el código original
    return code

# Vista principal
def index(request):
    # Intenta obtener los nombres de las ciudades a partir de los códigos IATA proporcionados
    city_name1 = get_city_from_iata(request.GET.get('city_name1', ''))
    city_name2 = get_city_from_iata(request.GET.get('city_name2', ''))
    weather_data1 = {}
    weather_data2 = {}
    clima_origen = {}
    clima_destino = {}
    is_ticket_search = False
    error_message = None

    # Si se proporcionan nombres de ciudades, consulta el clima para esas ciudades
    if city_name1:
        weather_data1 = get_weather(city_name1)
    if city_name2:
        weather_data2 = get_weather(city_name2)

    # Si el método de la solicitud es POST, significa que el usuario está buscando el clima basado en un número de ticket
    if request.method == 'POST':
        ticket_number = request.POST['ticket_number']

        if ticket_number:
            is_ticket_search = True
            # Carga el dataset con Pandas
            df = pd.read_csv('dataset2.csv')

            # Verifica si el ticket proporcionado existe en el dataset
            ticket_data_rows = df[df['num_ticket'] == ticket_number]
            if not ticket_data_rows.empty:
                ticket_data = ticket_data_rows.iloc[0]

                # Consulta el clima para las coordenadas de origen y destino del ticket
                clima_origen = consultar_clima(
                    ticket_data['origin_latitude'], ticket_data['origin_longitude'])
                clima_destino = consultar_clima(
                    ticket_data['destination_latitude'], ticket_data['destination_longitude'])
            else:
                error_message = "Por favor, ingrese un número de ticket válido."
    else:
        # Si no se proporciona un número de ticket, verifica si las ciudades proporcionadas son válidas
        if not weather_data1 and city_name1:
            error_message = "Por favor, ingrese una ciudad de origen válida."
        if not weather_data2 and city_name2:
            error_message = "Por favor, ingrese una ciudad de destino válida."

    # Renderiza la plantilla con los datos obtenidos
    return render(request, 'clima/clima.html', {
        'weather_data1': weather_data1,
        'weather_data2': weather_data2,
        'clima_origen': clima_origen,
        'clima_destino': clima_destino,
        'is_ticket_search': is_ticket_search,
        'error_message': error_message
    })

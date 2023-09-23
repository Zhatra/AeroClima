from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.conf import settings
import pandas as pd
from django.core.cache import cache
import Levenshtein


IATA_CODES = {
    'TLC': 'Toluca',
    'MTY': 'Monterrey',
    'MEX': 'Ciudad de Mexico',
    'TAM': 'Tampico',
    'GDL': 'Guadalajara',
    'CJS': 'Ciudad Juarez',
    'CUN': 'Cancun',
    'TIJ': 'Tijuana',
    'HMO': 'Hermosillo',
    'CME': 'Ciudad del Carmen',
    'MID': 'Merida',
    'CTM': 'Chetumal',
    'VER': 'Veracruz',
    'OAX': 'Oaxaca',
    'HUX': 'Huatulco',
    'PVR': 'Puerto Vallarta',
    'PXM': 'Puerto Escondido',
    'ACA': 'Acapulco',
    'ZIH': 'Zihuatanejo',
    'AGU': 'Aguascalientes',
    'VSA': 'Villahermosa',
    'CZM': 'Cozumel',
    'CUU': 'Chihuahua',
    'TRC': 'Torreon',
    'QRO': 'Queretaro',
    'BJX': 'Leon/Guanajuato',
    'PBC': 'Puebla',
    'SLP': 'San Luis Potosi',
    'ZCL': 'Zacatecas',
    'LIM': 'Lima',
    'HAV': 'La Habana',
    'BOG': 'Bogota',
    'MIA': 'Miami',
    'LAX': 'Los Angeles',
    'JFK': 'Nueva York',
    'MZT': 'Mazatlan',
    'GUA': 'Ciudad de Guatemala',
    'BZE': 'Ciudad de Belice',
    'DFW': 'Dallas',
    'ORD': 'Chicago',
    'PHX': 'Phoenix',
    'PHL': 'Filadelfia',
    'CLT': 'Charlotte',
    'YYZ': 'Toronto',
    'IAH': 'Houston',
    'YVR': 'Vancouver',
    'CDG': 'Paris',
    'AMS': 'Amsterdam',
    'ATL': 'Atlanta',
    'CEN': 'Ciudad Obregon',
    'MAD': 'Madrid',
    'SCL': 'Santiago',
}

IMAGES = {
    'Clear',
    'Clouds',
    'Drizzle',
    'Else',
    'Rain',
    'Snow',
    'Thunderstorms',
}


def fetch_from_cache_or_api(url):
    # Usa la URL como clave para el caché
    cache_key = f"api_cache_{url}"
    cached_response = cache.get(cache_key)

    if cached_response:
        return cached_response

    # Si no está en caché, haz la llamada real
    response = requests.get(url)
    data = response.json()

    # Guarda la respuesta en caché por un tiempo determinado (en este caso, 43200 segundos = 12 horas)
    cache.set(cache_key, data, 43200)

    return data

# Create your views here.


def get_weather(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={settings.OPENWEATHERMAP_API_KEY}&units=metric&lang=es"
    data = fetch_from_cache_or_api(url)
    icon_code = data['weather'][0]['icon']
    data['weather_icon_url'] = f"https://openweathermap.org/img/wn/{icon_code}.png"
    return data


def consultar_clima(latitud, longitud):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={settings.OPENWEATHERMAP_API_KEY}&units=metric&lang=es"
    data = fetch_from_cache_or_api(url)
    icon_code = data['weather'][0]['icon']
    data['weather_icon_url'] = f"https://openweathermap.org/img/wn/{icon_code}.png"
    return data


def get_city_from_iata(code):
    # Retorna el nombre de la ciudad si el código existe en el diccionario.
    city = IATA_CODES.get(code)

    if city:
        return city

    # Si el código no se encuentra en el diccionario, busca la ciudad más parecida.
    min_distance = float('inf')
    closest_city = None

    for city_name in IATA_CODES.values():
        distance = Levenshtein.distance(code.lower(), city_name.lower())
        if distance < min_distance:
            min_distance = distance
            closest_city = city_name

    # Por ejemplo, si la distancia es 1 o 2, consideramos que es una coincidencia cercana.
    # Puedes ajustar este umbral según lo que consideres adecuado.
    if min_distance <= 3:
        return closest_city

    # Si no encuentra una coincidencia cercana, simplemente retorna el código ingresado.
    return code


def index(request):
    city_name1 = get_city_from_iata(request.GET.get('city_name1', ''))
    city_name2 = get_city_from_iata(request.GET.get('city_name2', ''))
    weather_data1 = {}
    weather_data2 = {}
    clima_origen = {}
    clima_destino = {}
    is_ticket_search = False

    if city_name1:
        weather_data1 = get_weather(
            city_name1
        )
    if city_name2:
        weather_data2 = get_weather(
            city_name2
        )
    # Buscar Clima por Ticket
    if request.method == 'POST':
        ticket_number = request.POST['ticket_number']

        if ticket_number is not "":
            is_ticket_search = True
            # Cargar la base de datos con Pandas
            df = pd.read_csv('dataset2.csv')

            # Buscar el ticket en la base de datos
            ticket_data = df[df['num_ticket'] == ticket_number].iloc[0]

            # Consultar clima de origen y destino usando OpenWeatherMap
            clima_origen = consultar_clima(
                ticket_data['origin_latitude'], ticket_data['origin_longitude'])
            clima_destino = consultar_clima(
                ticket_data['destination_latitude'], ticket_data['destination_longitude'])

    return render(request, 'clima/clima.html', {
        'weather_data1': weather_data1,
        'weather_data2': weather_data2,
        'clima_origen': clima_origen,
        'clima_destino': clima_destino,
        'is_ticket_search': is_ticket_search
    })

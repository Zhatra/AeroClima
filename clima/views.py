from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.conf import settings
import  pandas as pd
from django.core.cache import cache

# Create your views here.


def index(request):
    
    return render(request, 'clima/clima.html')

def index(request):
    city_name1 = request.GET.get('city_name1','')
    city_name2 = request.GET.get('city_name2','')
    weather_data1 = {}
    weather_data2 = {}
    clima_origen = {}
    clima_destino = {}

    if city_name1:
        weather_data1 = get_weather(
                city_name1
                )
    if city_name2:
        weather_data2 = get_weather(
                city_name2
                )
    #Buscar Clima por Ticket
    if request.method == 'POST':
        ticket_number = request.POST['ticket_number']

        # Cargar la base de datos con Pandas
        df = pd.read_csv('dataset2.csv')

        # Buscar el ticket en la base de datos
        ticket_data = df[df['num_ticket'] == ticket_number].iloc[0]

        # Consultar clima de origen y destino usando OpenWeatherMap
        clima_origen = consultar_clima(ticket_data['origin_latitude'], ticket_data['origin_longitude'])
        clima_destino = consultar_clima(ticket_data['destination_latitude'], ticket_data['destination_longitude'])

    return render(request, 'clima/clima.html',{
        'weather_data1':weather_data1,
        'weather_data2':weather_data2,
        'clima_origen':clima_origen,
        'clima_destino':clima_destino
    })
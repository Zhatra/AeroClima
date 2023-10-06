"""
Archivo de Constantes para el proyecto AeroClima.

Este módulo define varias constantes utilizadas a lo largo de la aplicación AeroClima para representar
datos estáticos y mejorar la legibilidad y mantenibilidad del código.

Contenidos:
    - CODIGOS_IATA: Un diccionario que mapea los códigos IATA de aeropuertos a sus nombres de ciudad correspondientes.
    - IMAGENES: Un diccionario que mapea diferentes condiciones climáticas a URLs de imágenes representativas.
    - CODIGO_IMG: Un conjunto que enumera todos los códigos de condición climática que tienen imágenes asociadas.

"""

CODIGOS_IATA = {
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


IMAGENES = {
    'Clear': 'https://cdn-icons-png.flaticon.com/128/4015/4015543.png',
    'Clouds': 'https://cdn-icons-png.flaticon.com/128/4015/4015374.png',
    'Drizzle': 'https://cdn-icons-png.flaticon.com/128/4015/4015265.png',
    'Rain': 'https://cdn-icons-png.flaticon.com/128/4015/4015291.png',
    'Snow': 'https://cdn-icons-png.flaticon.com/128/4015/4015402.png',
    'Thunderstorm': 'https://cdn-icons-png.flaticon.com/128/4015/4015508.png',
    'Else': 'https://cdn-icons-png.flaticon.com/128/4015/4015221.png',
}


CODIGO_IMG = {
    'Clear',
    'Clouds',
    'Drizzle',
    'Rain',
    'Snow',
    'Thunderstorm',
    'Else',
}

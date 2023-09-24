# AeroClima

AeroClima es una aplicación web desarrollada con Django que permite a los usuarios consultar el clima actual de un lugar de origen y un lugar de destino, ya sea ingresando el nombre de las ciudades o a través de un número de ticket.

## Índice

1. [Descripción General](#aeroclima)
2. [Configuración](#configuración)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Funcionalidad](#funcionalidad)
5. [Contribuciones](#contribuciones)
6. [Requisitos previos](#requisitos-previos)
7. [Instalación](#instalación)
8. [Desactivar el entorno virtual](#desactivar-el-entorno-virtual)
9. [Desactivar redis-server](#desactivar-redis-server)

## Descripción General

AeroClima es una herramienta intuitiva diseñada para aquellos que desean obtener información climática rápida y precisa para sus viajes. No se requiere experiencia previa en programación para usar o configurar esta aplicación.

## Configuración

### Requisitos

- Python 3.x
- Django 4.2.5
- `requests`: Necesario para realizar llamadas API.
- `pandas`: Utilizado para el manejo de datos.
- `Levenshtein`: Herramienta para la comparación de cadenas.

### Configuración del Proyecto

El archivo `settings.py` es el corazón de la configuración del proyecto. Por razones de seguridad, **nunca** expongas la `SECRET_KEY` en repositorios públicos. Además, para que la aplicación funcione correctamente, debes agregar tu llave personal de la API de OpenWeatherMap en `OPENWEATHERMAP_API_KEY`.

## Estructura del Proyecto

### Aplicaciones

El proyecto tiene una aplicación principal denominada `clima`.

#### Clima

- **Modelos**: Aunque no se definen modelos específicos, se utiliza un diccionario `IATA_CODES` para relacionar códigos IATA con nombres de ciudades.
- **Vistas**: La vista `index` es la principal y se encarga de la lógica para consultar el clima usando nombres de ciudades o números de ticket.
- **URLs**: La ruta principal `path("", views.index, name="index")` dirige a la vista `index`.
- **Templates**: El template `clima.html` muestra formularios para ingresar nombres de ciudades o números de ticket y desplegar el clima correspondiente.

### Estilos

Los estilos del proyecto se encuentran en `style.css` dentro de la carpeta `static`. Estos estilos determinan la apariencia general de la aplicación, incluyendo colores, fuentes y diseño.

## Funcionalidad

1. **Consulta de Clima**: Los usuarios pueden consultar el clima ingresando el nombre de las ciudades en los campos "Origen" y "Destino" o mediante un número de ticket.
2. **Caché**: Para optimizar el rendimiento y minimizar las llamadas a la API, se utiliza un sistema de caché.
3. **Búsqueda de Ciudades por Código IATA**: Si el código IATA no se encuentra en el diccionario `IATA_CODES`, se busca la ciudad más parecida usando la distancia de Levenshtein.

## Contribuciones

Si estás interesado en mejorar AeroClima o agregar nuevas funcionalidades, ¡tu ayuda es bienvenida! Simplemente clona el repositorio desde [GitHub](https://github.com/Zhatra/AeroClima.git) y sigue las instrucciones de instalación y configuración.

## Requisitos previos

- Python 3.x

## Instalación

1. **Instalar Python**: Si no tienes Python, descárgalo desde el [sitio oficial de Python](https://www.python.org/downloads/).
   
   ```bash
   # Dependiendo de tu sistema operativo, el comando puede variar.
   ```

2. **Instalar Redis**: Es necesario para algunas funcionalidades. Descárgalo desde el [sitio oficial de Redis](https://redis.io/docs/getting-started/installation/).

   ```bash
   # El proceso de instalación varía según el sistema operativo.
   ```

3. **Instalar `virtualenv`**: Esta herramienta te permite crear entornos virtuales en Python.

   ```bash
   pip install virtualenv
   ```

4. **Crear y activar un entorno virtual**: Esto asegura que los paquetes necesarios no interfieran con otros proyectos.

   ```bash
   virtualenv nombre_del_entorno
   ```

   - **Activar el entorno virtual**:

     - En Windows:

       ```bash
       .\nombre_del_entorno\Scripts\activate
       ```

     - En macOS y Linux:

       ```bash
       source nombre_del_entorno/bin/activate
       ```

5. **Instalar dependencias**: Estas son las bibliotecas y herramientas necesarias para que AeroClima funcione correctamente.

   ```bash
   pip install -r requirements.txt
   ```

6. **Ejecutar servidor Redis**: Inicia el servidor Redis.

   ```bash
   redis-server
   ```

7. **Ejecutar el proyecto Django**: Con esto, tendrás AeroClima funcionando en tu máquina local.

   ```bash
   python manage.py runserver
   ```

## Desactivar el entorno virtual

Una vez que hayas terminado de usar AeroClima, es una buena práctica desactivar el entorno virtual.

```bash
deactivate
```

## Desactivar redis-server

Si ya no necesitas usar Redis, puedes detener el servidor fácilmente.

```bash
redis-cli shutdown
```

---


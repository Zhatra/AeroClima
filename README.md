# AeroClima

Aplicacion web para checar el clima de la ciudad de origen y destino de tu vuelo.

## Requisitos previos

- Python 3.x

## Instalación

### 1. Instalar Python

Si aún no tienes Python instalado, puedes descargarlo desde el [sitio oficial de Python](https://www.python.org/downloads/).

### 2. Instalar Redis

Puedes descargarlo desde el [sitio oficial de Redis](https://redis.io/docs/getting-started/installation/).



### 3. Instalar `virtualenv`

`virtualenv` es una herramienta para crear entornos virtuales aislados en Python. Para instalarlo, ejecuta:

```bash
pip install virtualenv
```


### 4. Crear un entorno virtual

Para crear un entorno virtual para tu proyecto, navega hasta la carpeta de tu proyecto y ejecuta:

```bash
virtualenv nombre_del_entorno
```

Donde `nombre_del_entorno` es el nombre que quieras darle a tu entorno virtual.

### 5. Activar el entorno virtual

Antes de instalar cualquier paquete, asegúrate de activar tu entorno virtual:

- En Windows:

```bash
.\nombre_del_entorno\Scripts\activate
```

- En macOS y Linux:

```bash
source nombre_del_entorno/bin/activate
```

### 6. Instalar las dependencias

Con tu entorno virtual activado, instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

### 7. Ejecutar servidor redis

Ya con redis instalado, ejecuta el servidor de redis con:
```bash
redis-server
```


### 8. Ejecutar el proyecto Django

Una vez que hayas instalado todas las dependencias, puedes ejecutar el servidor de desarrollo de Django con:

```bash
python manage.py runserver
```

Ahora, deberías poder acceder a tu aplicación en `http://127.0.0.1:8000/`.

## Desactivar el entorno virtual

Cuando hayas terminado de trabajar o ver el proyecto, puedes desactivar el entorno virtual con:

```bash
deactivate
```
## Desactivar redis-server

Para apagar redis-server necesitas ejecutar el comando en la terminal:

```bash
redis-cli shutdown
```
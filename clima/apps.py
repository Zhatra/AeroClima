from django.apps import AppConfig

class ClimaConfig(AppConfig):
    """
    Configuración de la aplicación Clima para el proyecto AeroClima.

    Esta clase hereda de `AppConfig` y configura la aplicación 'clima'.
    El nombre de la aplicación y el campo de autoincremento predeterminado para los modelos se definen aquí.

    Atributos:
        default_auto_field (str): Define el tipo de campo utilizado para la clave primaria autoincrementada en los modelos.
        name (str): Define el nombre de la aplicación, que se utiliza en todo el proyecto para referenciar a esta aplicación.
    """

    # Define el tipo de campo a utilizar para la clave primaria autoincrementada en los modelos de la aplicación.
    default_auto_field = 'django.db.models.BigAutoField'

    # Define el nombre de la aplicación que se utilizará en las configuraciones del proyecto y en los modelos.
    name = 'clima'

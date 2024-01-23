"""
3.- Queremos hacer una aplicación que pida un personaje de Star Wars y nos diga los 
nombres de las películas en las que ha salido y su planeta de nacimiento, para ello 
haz uso de esta API.
"""
import requests

def obtener_nombres_todos_personajes():
    # Inicializar la lista para almacenar todos los nombres
    nombres_personajes = []

    # URL de la primera página de personajes
    url_personajes = "https://swapi.dev/api/people/"
    while url_personajes:
        # Obtener datos de la página actual
        respuesta_personajes = requests.get(url_personajes)
        datos_personajes = respuesta_personajes.json()

        # Agregar nombres de la página actual a la lista
        nombres_personajes.extend([personaje['name'] for personaje in datos_personajes['results']])

        # Obtener la URL de la próxima página (si existe)
        url_personajes = datos_personajes['next']

    return nombres_personajes

def mostrar_nombres_personajes():
    # Obtener todos los nombres de personajes
    nombres_personajes = obtener_nombres_todos_personajes()

    # Mostrar nombres de todos los personajes enumerados
    print("Nombres de personajes disponibles:")
    for i, nombre_personaje in enumerate(nombres_personajes, 1):
        print(f"{i}. {nombre_personaje}")
    print("\n")

def obtener_informacion_personaje(nombre_personaje):
    # Buscar el personaje por nombre
    url_personajes = "https://swapi.dev/api/people/"
    parametros = {'search': nombre_personaje}
    respuesta_personajes = requests.get(url_personajes, params=parametros)
    datos_personajes = respuesta_personajes.json()

    if datos_personajes['count'] == 0:
        return "Personaje no encontrado."

    # Obtener información del primer personaje encontrado
    personaje = datos_personajes['results'][0]
    nombre_personaje = personaje['name']
    peliculas = [requests.get(pelicula).json()['title'] for pelicula in personaje['films']]
    planeta_nacimiento_url = personaje['homeworld']
    planeta_nacimiento = requests.get(planeta_nacimiento_url).json()['name']

    # Imprimir la información del personaje
    print(f"Información de {nombre_personaje}:")
    print(f"Películas: {', '.join(peliculas)}")
    print(f"Planeta de nacimiento: {planeta_nacimiento}")

# Mostrar nombres de personajes antes de solicitar el nombre específico
mostrar_nombres_personajes()

# Ejemplo de uso
nombre_personaje = input("Introduce el nombre de un personaje de Star Wars: ")
obtener_informacion_personaje(nombre_personaje)

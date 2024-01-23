"""
2.- El FBI tiene recorte de personal informático y solicitan nuestra ayuda, quieren saber cuantos 
fugitivos tienes registrados en cada una de sus oficinas, para ello han habilitado una API a la que 
puedes acceder desde aquí.
"""

import requests
import json

def obtener_cantidad_fugitivos_oficinas():
    # Inicializar variables
    fugitivos_por_oficina = {}
    fugitivos_no_registrados = 0
    pagina = 1

    while True:
        # Realizar consulta a la API con el número de página
        response = requests.get('https://api.fbi.gov/wanted/v1/list', params={'page': pagina})
        data = json.loads(response.content)

        # Verificar si hay más páginas
        if 'items' not in data or not data['items']:
            break

        # Procesar los resultados de la página actual
        for fugitivo in data['items']:
            oficinas = fugitivo.get('field_offices', [])
            if not oficinas:
                fugitivos_no_registrados += 1
            else:
                for oficina in oficinas:
                    if oficina in fugitivos_por_oficina:
                        fugitivos_por_oficina[oficina] += 1
                    else:
                        fugitivos_por_oficina[oficina] = 1

        # Pasar a la siguiente página
        pagina += 1

    # Ordenar las oficinas alfabéticamente
    oficinas_ordenadas = sorted(fugitivos_por_oficina.items(), key=lambda x: x[0])

    # Mostrar resultados
    print("Cantidad de fugitivos por oficina:")
    for oficina, cantidad in oficinas_ordenadas:
        print(f"{oficina}: {cantidad}")

    print("\nCantidad de fugitivos no registrados en ninguna oficina:", fugitivos_no_registrados)

# Llamar a la función principal
obtener_cantidad_fugitivos_oficinas()

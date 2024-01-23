"""
1.- Queremos hacer una aplicación que sea capaz de convertir una cantidad de dinero en una moneda a otra moneda, para ello haremos uso de la API descrita aquí.

Al usuario/a le pediremos:

La moneda desde la que queremos la conversión.
La moneda a la que queremos convertir.
La cantidad de dinero que tenemos.
A tener en cuenta:

Si la consulta da un error hay que indicarlo.
Al usuario se le mostrarán las diferentes unidades de moneda antes de pedir los datos, estas se pueden obtener mediante consulta en esta misma API.
"""
import requests

def obtener_unidades_moneda():
    # URL de la API para obtener las unidades de moneda
    url_unidades_moneda = "https://v6.exchangerate-api.com/v6/4cd5f57886583a5fa4f44d5d/codes"
    
    # Realizar una solicitud GET a la API
    response = requests.get(url_unidades_moneda)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtener las unidades de moneda de la respuesta JSON de la API
        unidades_moneda = response.json().get('supported_codes', [])
        return unidades_moneda
    else:
        print(f"Error al obtener las unidades de moneda")
        return []

def obtener_tasa_cambio(desde_moneda, a_moneda):
    # URL de la API para obtener la tasa de cambio entre dos monedas
    url_tasa_cambio = f"https://v6.exchangerate-api.com/v6/4cd5f57886583a5fa4f44d5d/latest/{desde_moneda}"
    
    # Realizar una solicitud GET a la API
    response = requests.get(url_tasa_cambio)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtener las tasas de cambio de la respuesta JSON de la API
        tasas = response.json().get('conversion_rates', {})
        return tasas.get(a_moneda)
    else:
        print(f"Error al obtener la tasa de cambio.")
        return None

def convertir_moneda():
    # Obtener las unidades de moneda disponibles
    unidades_moneda = obtener_unidades_moneda()

    if unidades_moneda:
        # Mostrar las unidades de moneda disponibles al usuario
        print("Unidades de moneda disponibles:")
        for unidad in unidades_moneda:
            print(f"{unidad[0]} - {unidad[1]}")

        # Solicitar al usuario ingresar las monedas y la cantidad
        desde_moneda = input("Ingrese la moneda desde la que quiere convertir: ")
        a_moneda = input("Ingrese la moneda a la que quiere convertir: ")

        # Crear una lista de las siglas de las monedas para la validación
        siglas_moneda = [unidad[0] for unidad in unidades_moneda]

        # Verificar si las monedas ingresadas son válidas
        if desde_moneda not in siglas_moneda or a_moneda not in siglas_moneda:
            print("Moneda no válida.")
            return

        # Solicitar al usuario ingresar la cantidad de dinero
        cantidad = float(input("Ingrese la cantidad de dinero que tiene: "))

        # Obtener la tasa de cambio entre las monedas ingresadas
        tasa_cambio = obtener_tasa_cambio(desde_moneda, a_moneda)

        # Verificar si se pudo obtener la tasa de cambio
        if tasa_cambio is not None:
            # Realizar la conversión y mostrar el resultado
            cantidad_convertida = cantidad * tasa_cambio
            print(f"{cantidad} {desde_moneda} equivale a {cantidad_convertida:.2f} {a_moneda}")
        else:
            print("No se pudo realizar la conversión.")

if __name__ == "__main__":
    # Ejecutar la función principal para convertir moneda
    convertir_moneda()


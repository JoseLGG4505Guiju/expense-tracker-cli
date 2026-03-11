import json
from pathlib import Path

DATA_FILE = Path("data.json")

def load_data():
    """_summary_
    Lo que hace load_data es comprobar que el archivo de datos existe, si es así, lo abre y carga su contenido como un diccionario de Python utilizando json.load(). Si el archivo no existe, devuelve un diccionario con una clave "expenses" que contiene una lista vacía.

    Returns:
        dict: Un diccionario que contiene los datos cargados desde el archivo JSON o una estructura vacía si el archivo no existe.

    """
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f) # Carga los datos desde el archivo JSON y los devuelve como un diccionario de Python
    return {"expenses": []} # Si el archivo no existe, devuelve un diccionario con una lista vacía de gastos

def save_data(data):
    """_summary_
    Comprueba si el archivo de datos existe y, si es así, guarda el objeto de datos proporcionado en el archivo JSON utilizando json.dump(). La función devuelve el mismo objeto de datos que se ha guardado.
    Args:
        data (objeto): El objeto de datos que se desea guardar en el archivo JSON.
    Returns:
        objeto: El mismo objeto de datos que se ha guardado en el archivo JSON.
    """
    with open(DATA_FILE, "w", encoding="utf-8" ) as f:
            json.dump(data, f, indent=4) # Guarda los datos en el archivo JSON con una indentación de 4 espacios para mejorar la legibilidad
    return data



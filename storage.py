
import json
import os
import tempfile
from pathlib import Path

DATA_FILE = Path("data.json")


def load_data(path=None):
    """Carga datos JSON desde `path` o `DATA_FILE` si no se especifica.

    Devuelve un dict con clave "expenses" como lista vacía si el fichero no existe.
    """
    target = Path(path) if path is not None else DATA_FILE
    if target.exists():
        with open(target, "r", encoding="utf-8") as f:
            raw = json.load(f)
            # Normalizar formatos: aceptar lista directa o dict {"expenses": [...]}
            if isinstance(raw, list):
                return {"expenses": raw}
            if isinstance(raw, dict) and isinstance(raw.get("expenses"), list):
                return raw
            if isinstance(raw, dict):
                # Diccionario no estándar: envolver como un único registro
                return {"expenses": [raw]}
            # Fallback
            return {"expenses": []}
    return {"expenses": []}


def save_data(data, path=None):
    """Guarda `data` en `path` (o `DATA_FILE`) de forma atómica.

    Escribe en un fichero temporal en el mismo directorio, forza el volcado a disco
    y luego reemplaza el fichero objetivo con `Path.replace()`.
    """
    target = Path(path) if path is not None else DATA_FILE
    # Asegurar que existe el directorio destino
    if target.parent:
        target.parent.mkdir(parents=True, exist_ok=True)

    # Crear un temporal en el mismo directorio para permitir un replace atómico
    dirpath = str(target.parent) if target.parent else None
    # Normalizar data aceptando lista o dict
    if isinstance(data, list):
        data_to_write = {"expenses": data}
    elif isinstance(data, dict) and isinstance(data.get("expenses"), list):
        data_to_write = data
    else:
        # envolver cualquier otro objeto como un único registro
        data_to_write = {"expenses": [data]}

    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, dir=dirpath) as tf:
        json.dump(data_to_write, tf, indent=4, ensure_ascii=False)
        tf.flush()
        os.fsync(tf.fileno())
        temp_name = tf.name

    # Reemplazo atómico del fichero objetivo
    Path(temp_name).replace(target)
    return data




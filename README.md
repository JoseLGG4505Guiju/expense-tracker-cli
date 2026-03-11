# expense-tracker-cli

Gestor de gastos personales — pequeña CLI para registrar ingresos y gastos, obtener resúmenes y generar gráficos.

Descripción

Proyecto de ejemplo para practicar Python: persistencia sencilla, análisis básico y visualización con matplotlib.

Estado

- Implementación base: `app.py` existe como punto de partida.
- `plots.py` está previsto para las funciones de visualización.
- `data.json` se usa para persistencia local (por defecto contiene una lista vacía).

Instalación rápida

```bash
python -m venv .venv
# Unix/macOS
source .venv/bin/activate
# Windows (PowerShell)
\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Ejemplo de uso

```bash
python app.py add --amount 50 --category "Comida" --date 2024-06-01 --note "Almuerzo"
python app.py list
python app.py summary --month 2024-06
python app.py plot --month 2024-06
```

Archivo de ejemplo `data.sample.json`

```json
[
  {
    "id": 1,
    "date": "2026-03-18",
    "amount": -12.5,
    "category": "comida",
    "note": "Café"
  },
  {
    "id": 2,
    "date": "2026-03-18",
    "amount": 1200,
    "category": "sueldo",
    "note": "Nómina"
  }
]
```

Archivos importantes

- `app.py`: CLI principal (comandos `add`, `list`, `summary`, `plot`).
- `plots.py`: funciones para generar gráficos (barras, pastel, serie temporal).
- `data.json`: persistencia local (no subir datos reales a GitHub).
- `data.sample.json`: ejemplo con datos de prueba.
- `requirements.txt`: dependencias del proyecto.

Buenas prácticas antes de subir a GitHub

- Añadir una licencia (por ejemplo MIT) en `LICENSE`.
- Crear `.gitignore` para evitar subir archivos generados o datos sensibles.
- Incluir `data.sample.json` en lugar de `data.json` real; añadir `data.json` a `.gitignore`.
- Añadir instrucciones claras de instalación y ejemplos en el README (esto ya está aquí).
- Añadir `requirements.txt` con las dependencias necesarias.

Contribuir

Si quieres mejorar el proyecto: crea una rama, haz cambios pequeños y abre un Pull Request. Añade tests si es posible (pytest recomendada).

Licencia

Proyecto con licencia MIT. Ver archivo `LICENSE`.

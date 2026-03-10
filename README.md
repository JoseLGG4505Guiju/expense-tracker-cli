# expense-tracker-cli

Gestor de gastos personales

Descripción

Proyecto de ejemplo para registrar ingresos y gastos por categoría, ver un resumen mensual y generar gráficos con matplotlib.

Estructura propuesta

- `app.py` — CLI principal (añadir, listar, resumen, exportar)
- `plots.py` — funciones para generar gráficos (barras, pastel, series temporales)
- `data.json` — persistencia local (lista de registros)
- `requirements.txt` — dependencias

Notas

- He creado la estructura y los archivos vacíos excepto el código: implementa `app.py` y `plots.py` a tu gusto.
- `data.json` contiene inicialmente una lista vacía para que la uses desde el primer `add`.

Ejemplo de uso

```bash
$ python app.py add --amount 50 --category "Comida" --date 2024-06-01 --note "Almuerzo"
Gasto registrado: 50€ en Comida el 2024-06-01

$ python app.py summary --month 2024-06-01 
Resumen de gastos para 2024-06-01:
- Comida: 50€

$ python app.py plot --month 2024-06-01
Gráfico generado: gastos_2024-06.png
```

Ejemplo de `data.json`

```json
{
    "id": 1,
    "date": "2026-03-18",
    "amount": -12.5,
    "category": "comida",
    "note": "Café"
}
```

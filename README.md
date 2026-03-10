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

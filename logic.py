"""Lógica de negocio para expense-tracker-cli."""
from datetime import datetime
from collections import defaultdict


def next_id(data):
    expenses = data.get("expenses", [])
    if not expenses:
        return 1
    return max((e.get("id", 0) for e in expenses)) + 1


def add_record(data, record):
    """Valida y añade un registro, asignando id.

    record: dict con keys: date (YYYY-MM-DD), amount (float), category, note (opcional)
    """
    expenses = data.setdefault("expenses", [])
    rec = record.copy()
    rec["id"] = next_id(data)
    # Normalizar fecha
    try:
        datetime.strptime(rec["date"], "%Y-%m-%d")
    except Exception:
        raise ValueError("Fecha debe tener formato YYYY-MM-DD")
    # Normalizar categoría
    rec["category"] = str(rec.get("category", "")).lower()
    expenses.append(rec)
    return data


def list_records(data, filters=None):
    filters = filters or {}
    res = data.get("expenses", [])
    # Implementar filtros básicos más tarde
    return sorted(res, key=lambda r: r.get("date"))


def summary_for_month(data, year_month):
    """Devuelve resumen para un mes 'YYYY-MM' con suma por categoría y total."""
    by_cat = defaultdict(float)
    total = 0.0
    for r in data.get("expenses", []):
        d = r.get("date", "")
        if not d.startswith(year_month):
            continue
        amt = float(r.get("amount", 0))
        cat = r.get("category", "uncategorized")
        by_cat[cat] += amt
        total += amt
    return {"by_category": dict(by_cat), "total": total}

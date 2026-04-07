"""Funciones de visualización para expense-tracker-cli."""
import matplotlib.pyplot as plt


def plot_month_bar(by_category, title_month):
    if not by_category:
        print("No hay datos para el mes.")
        return
    cats = list(by_category.keys())
    vals = [by_category[c] for c in cats]
    fig, ax = plt.subplots()
    ax.bar(cats, vals)
    ax.set_title(f"Gastos {title_month}")
    ax.set_ylabel("Importe")
    ax.set_xticklabels(cats, rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

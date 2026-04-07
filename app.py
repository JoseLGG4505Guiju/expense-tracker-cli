"""CLI para expense-tracker-cli.

Comandos soportados: add, list, summary, plot
"""

import argparse
from datetime import datetime
from pathlib import Path

from storage import load_data, save_data
from logic import add_record, list_records, summary_for_month
from plots import plot_month_bar

DATA_FILE = Path("data.json")


def parse_args():
	p = argparse.ArgumentParser(description="Expense tracker CLI")
	sub = p.add_subparsers(dest="cmd")

	a = sub.add_parser("add", help="Añadir gasto/ingreso")
	a.add_argument("--amount", type=float, required=True)
	a.add_argument("--category", required=True)
	a.add_argument("--date", required=False, help="YYYY-MM-DD")
	a.add_argument("--note", required=False, default="")

	sub.add_parser("list", help="Listar registros")

	s = sub.add_parser("summary", help="Resumen por mes")
	s.add_argument("--month", required=True, help="YYYY-MM")

	p_plot = sub.add_parser("plot", help="Generar gráfico del mes")
	p_plot.add_argument("--month", required=True, help="YYYY-MM")

	return p.parse_args()


def main():
	args = parse_args()
	data = load_data()

	if args.cmd == "add":
		date = args.date or datetime.today().strftime("%Y-%m-%d")
		record = {"date": date, "amount": args.amount, "category": args.category, "note": args.note}
		data = add_record(data, record)
		save_data(data)
		print("Registro añadido.")

	elif args.cmd == "list":
		for r in list_records(data, {}):
			print(r)

	elif args.cmd == "summary":
		res = summary_for_month(data, args.month)
		print("Resumen para", args.month)
		for cat, val in res["by_category"].items():
			print(f"{cat}: {val}")
		print("Total:", res["total"])

	elif args.cmd == "plot":
		res = summary_for_month(data, args.month)
		plot_month_bar(res["by_category"], args.month)

	else:
		print("Usa --help para ver comandos")


if __name__ == "__main__":
	main()


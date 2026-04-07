from logic import add_record, next_id, summary_for_month


def test_next_id_and_add():
    data = {"expenses": []}
    record = {"date": "2026-03-10", "amount": 10, "category": "comida"}
    data = add_record(data, record)
    assert data["expenses"][0]["id"] == 1


def test_summary():
    data = {"expenses": [{"id":1, "date":"2026-03-01","amount":10,"category":"comida"},{"id":2,"date":"2026-03-05","amount":-2,"category":"comida"}]}
    res = summary_for_month(data, "2026-03")
    assert res["by_category"]["comida"] == 8

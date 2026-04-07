import os
from storage import save_data, load_data


def test_save_and_load_tmp(tmp_path):
    p = tmp_path / "test.json"
    data = {"expenses": [{"id": 1, "amount": 5, "date": "2026-03-01"}]}
    save_data(data, str(p))
    loaded = load_data(str(p))
    assert "expenses" in loaded
    assert loaded["expenses"][0]["amount"] == 5

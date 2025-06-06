import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from file_validator import validate_data_headers, read_csv, merge_data, convert_to_dict


def test_validate_data_headers():
    headers = ["name", "hours_worked", "hourly_rate", "department"]
    updated = validate_data_headers(headers.copy())
    assert "rate" in updated
    assert "hourly_rate" not in updated


def test_convert_to_dict():
    table = [
        ["name", "hours_worked", "rate"],
        ["Alice", "10", "100"],
        ["Bob", "5", "200"],
    ]
    result = convert_to_dict(table)
    assert result == [
        {"name": "Alice", "hours_worked": "10", "rate": "100"},
        {"name": "Bob", "hours_worked": "5", "rate": "200"},
    ]


def test_merge_data(tmp_path):
    file_path = tmp_path / "test.csv"
    text = "name,hours_worked,rate,department\nAlice,10,100,IT\nBob,5,150,HR"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

    result = merge_data([str(file_path)])

    assert result == [
        {"name": "Alice", "hours_worked": "10", "rate": "100", "department": "IT"},
        {"name": "Bob", "hours_worked": "5", "rate": "150", "department": "HR"},
    ]

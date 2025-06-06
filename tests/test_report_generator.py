import sys
import io
import os
import tempfile
from json import load

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from report_generator import get_departments, sort_data, report_to_json, print_report


def test_get_departments():
    data = [
        {"name": "Alice", "department": "IT"},
        {"name": "Bob", "department": "HR"},
        {"name": "Eve", "department": "IT"},
    ]
    result = get_departments(data)
    assert result == ["HR", "IT"]


def test_sort_data():
    data = [
        {"name": "Anna", "rate": 10, "hours_worked": 5},
        {"rate": 20, "hours_worked": 8, "name": "Bob"},
    ]

    expected = [
        {"hours_worked": 5, "name": "Anna", "rate": 10},
        {"hours_worked": 8, "name": "Bob", "rate": 20},
    ]

    result = sort_data(data)

    assert result == expected


def test_report_to_json():
    data = [
        {"name": "Alice", "hours_worked": "10", "rate": "100", "department": "IT"},
        {"name": "Bob", "hours_worked": "5", "rate": "150", "department": "HR"},
    ]
    name = "payout"

    with tempfile.TemporaryDirectory(delete=False) as tmpdir:
        filename = os.path.join(tmpdir, name)
        report_to_json(data, filename)

    json_file = filename + ".json"
    assert os.path.exists(json_file)

    with open(json_file, encoding="utf-8") as file:
        content = load(file)

    assert any(item["name"] == "Alice" for item in content)
    assert any(item["rate"] == "150" for item in content)


def test_print_report_without_contextlib():
    data = [
        {"name": "Alice", "hours_worked": "10", "rate": "100", "department": "IT"},
        {"name": "Bob", "hours_worked": "5", "rate": "150", "department": "HR"},
        {"name": "Carol", "hours_worked": "8", "rate": "120", "department": "IT"},
    ]
    departments = {"IT", "HR"}
    indent = 5

    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        print_report(data, indent, departments)
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout

    assert "name" in output
    assert "hours" in output
    assert "IT" in output
    assert "Alice" in output
    assert "$1000" in output

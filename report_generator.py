from json import dump


def get_departments(data: list) -> set:
    """Выделяем отделы в отдельную переменную"""
    return sorted({row["department"] for row in data})


def print_report(data: list, indent: int, departments: set) -> None:
    """Вывод отчёта"""
    headers = ["name", "hours", "rate", "payout"]
    row_format = "{:<20}{:<10}{:<10}{:<10}"
    print(f"{indent * ' '} ", end="")
    print(row_format.format(*headers))
    for item in departments:
        print(item)
        sum_payout = 0
        sum_hours = 0
        for row in data:
            if item == row["department"]:
                payout = int(row["hours_worked"]) * int(row["rate"])
                sum_payout += payout
                sum_hours += int(row["hours_worked"])
                print(f"{indent * '-'} ", end="")
                print(
                    row_format.format(
                        row["name"], row["hours_worked"], row["rate"], f"${payout}"
                    )
                )
        print(
            f"{indent * ' '} {row_format.format(' ',sum_hours,' ', '$' + str(sum_payout))}"
        )


def create_report(data: list) -> None:
    """Печать"""
    departments = get_departments(data)
    indent = len(max(departments, key=len)) + 5
    print_report(data, indent, departments)


def sort_data(data: list) -> list:
    return [dict(sorted(row.items())) for row in data]


def report_to_json(data: list, name: str) -> None:
    """Создаем файл отчёта в формате json"""
    with open(f"{name}.json", "w", encoding="utf-8") as file:
        dump(sort_data(data), file, indent=4)

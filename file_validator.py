def validate_data_headers(headers: list) -> list:
    """Изменение названий заголовков"""
    possible_titles = ["hourly_rate", "rate", "salary"]
    for i in range(len(headers)):
        if headers[i] in possible_titles:
            headers[i] = "rate"
    return headers


def read_csv(file_path: str) -> list:
    """Чтение CSV-файла"""
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()
    rows = [row.split(",") for row in data.splitlines()]
    return rows


def merge_data(files: list) -> list:
    """Слияние прочитанных данных в один список со словарями"""
    merged_data = []
    for path in files:
        csv_data = read_csv(path)
        print(csv_data)
        csv_data[0] = validate_data_headers(csv_data[0])
        merged_data.extend(convert_to_dict(csv_data))
    return merged_data


def convert_to_dict(table: list) -> dict:
    """Создание словаря из файла"""
    headers = table[0]
    del table[0]
    converted_file = []
    for row in table:
        converted_file.append(dict(zip(headers, row)))
    return converted_file

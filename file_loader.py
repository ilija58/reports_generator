import argparse
import os


def get_files_from_directory(directory: str) -> list:
    """Получение файлов [из директории(-й)]"""
    try:
        if os.path.isdir(directory) and directory != "/":
            print([os.path.join(directory, f) for f in os.listdir(directory)])
            return [os.path.join(directory, f) for f in os.listdir(directory)]
    except FileNotFoundError:
        print(f'Директории "{directory}" нет')
    return []


def load_files() -> list:
    """Загрузка файлов"""
    parser = argparse.ArgumentParser(
        description="Reading csv files, create a report and output in console / Считывание csv файла и вывод отчёта о зарплате в консоль"
    )
    parser.add_argument(
        "input_files",
        type=str,
        nargs="+",
        help="Input files or path to files / Входные файлы ",
    )
    parser.add_argument(
        "-r",
        "--report",
        type=str,
        default="payout",
        help="Output file name / Имя выходного файла",
    )

    files = []
    args = parser.parse_args()
    for path in args.input_files:
        if os.path.isdir(path):
            files.extend(get_files_from_directory(path))
        elif os.path.isfile(path):
            files.append(path)
        else:
            raise BaseException(f'Предупреждение: путь или файл "{path}" не найден')
    print(files, args.report)
    return files, args

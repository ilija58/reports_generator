from file_loader import load_files
from file_validator import merge_data
from report_generator import create_report, report_to_json


def main():
    data, parsed_args = load_files()
    data = merge_data(data)
    create_report(data)
    report_to_json(data, parsed_args.report)


if __name__ == "__main__":
    main()

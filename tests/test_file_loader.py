import sys
import os
import tempfile

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from file_loader import get_files_from_directory, load_files


def test_get_files():
    assert get_files_from_directory("files/") == [
        "files/data1.csv",
        "files/data2.csv",
        "files/data3.csv",
    ]
    assert get_files_from_directory("/") == []
    assert get_files_from_directory("data1.csv") == []
    assert get_files_from_directory("fake_path/") == []
    assert get_files_from_directory("files2/") == []


def test_load_files_real_file():
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as tmp_file:
        tmp_file_name = tmp_file.name

    try:
        sys.argv = ["program", tmp_file_name]

        files, args = load_files()

        assert files == [tmp_file_name]
        assert args.input_files == [tmp_file_name]
        assert args.report == "payout"

    finally:
        os.remove(tmp_file_name)

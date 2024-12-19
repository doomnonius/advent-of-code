from typing import Tuple

def import_files(day) -> Tuple[str, str]:
    TEST_FILE = day.with_suffix(".testinput").read_text()
    INPUT_FILE = day.with_suffix(".input").read_text()
    return TEST_FILE, INPUT_FILE
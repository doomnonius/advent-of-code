from typing import Tuple

def import_files(day: str) -> Tuple[str, str]:
    TEST_FILE = day + ".testinput".read_text()
    INPUT_FILE = day + ".input".read_text()
    return TEST_FILE, INPUT_FILE
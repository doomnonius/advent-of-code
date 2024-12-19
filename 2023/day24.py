from typing import List

def part1(nums: List[int]) -> int:
    return





def part2(nums: List[int]) -> int:
    return




def process_data(data: str) -> Tuple[List[str]]:
    lines = data.strip().split("\n")
    return

if __name__ == "__main__":
    from datetime import datetime
    from pathlib import Path
    from .helpers import import_files
    TEST_FILE, INPUT_FILE = import_files(Path(__file__))
    TEST_DATA = process_data(TEST_FILE)
    RAW_DATA = process_data(INPUT_FILE)
    DATA = [int(x) for x in RAW_DATA.split()] # example code
    print(f"Part 1: {part1(DATA)}")
    print(f"Part 2: {part2(DATA)}")
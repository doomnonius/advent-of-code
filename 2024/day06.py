from typing import List, Set
from helpers import Coord

def part1(nums: List[int]) -> int:
    return





def part2(nums: List[int]) -> int:
    return

def navigate()

map: Set[Coord] = set()
def process_data(data: str) -> Coord:
    lines = data.strip().split("\n")
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            map.add(Coord(row,col))
            if lines[row][col] ==
    return 

if __name__ == "__main__":
    from datetime import datetime
    from pathlib import Path
    from helpers import import_files
    TEST_FILE, INPUT_FILE = import_files(Path(__file__))
    TEST_DATA = process_data(TEST_FILE)
    DATA = process_data(INPUT_FILE)
    test_1a = 41
    test_2a = 0
    p1 = part1(TEST_DATA)
    p2 = part2(TEST_DATA)
    if test_1a: assert p1 == test_1a, f"Part 1: {p1} is the wrong answer"
    p1 = part1(DATA)
    print(f"Part 1: {p1}")
    if test_2a: assert p2 == test_2a, f"Part 2: {p2} is the wrong answer"
    p2 = part2(DATA)
    print(f"Part 2: {p2}")
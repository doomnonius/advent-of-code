from typing import List

def part1(nums: List[List[int]], damp=False) -> int:
    r = 0
    for row in nums:
        if row not in [sorted(row), sorted(row, reverse=True)]:
            continue
        safe = True
        danger = 0
        for i in range(len(row)-1):
            if not 0 < abs(row[i+1]-row[i]) < 4:
                danger += 1
                if danger > 1: safe = False
        r += safe
    return r


def process_data(data: str) -> List[List[int]]:
    r = []
    for line in data.strip().split("\n"):
        r.append([int(x) for x in line.split()])
    return r

if __name__ == "__main__":
    from datetime import datetime
    from pathlib import Path
    from helpers import import_files
    TEST_FILE, INPUT_FILE = import_files(Path(__file__))
    TEST_DATA = process_data(TEST_FILE)
    DATA = process_data(INPUT_FILE)
    test_1a = 2
    test_2a = 4
    p1 = part1(TEST_DATA)
    p2 = part1(TEST_DATA, True)
    if test_1a: assert p1 == test_1a, f"Part 1: {p1} is the wrong answer"
    p1 = part1(DATA)
    print(f"Part 1: {p1}")
    if test_2a: assert p2 == test_2a, f"Part 2: {p2} is the wrong answer"
    p2 = part1(DATA,True)
    print(f"Part 2: {p2}")
from typing import List, Tuple

def part1(nums: Tuple[List[str]]) -> int:
    l0 = sorted(nums[0])
    l1 = sorted(nums[1])
    r = 0
    for i in range(0,len(l1)):
        r += abs(l0[i] - l1[i])
    return r

def part2(nums: Tuple[List[str]]) -> int:
    r = 0
    l0 = nums[0]
    l1 = sorted(nums[1])
    for n in l0:
        r += (n * l1.count(n))
    return r


def process_data(data: str) -> Tuple[List[str]]:
    l0 = []
    l1 = []
    for line in data.split("\n"):
        d = line.split()
        l0.append(int(d[0]))
        l1.append(int(d[1]))
    return (l0, l1)

if __name__ == "__main__":
    from datetime import datetime
    from pathlib import Path
    from helpers import import_files
    TEST_FILE, INPUT_FILE = import_files(Path(__file__))
    TEST_DATA = process_data(TEST_FILE)
    DATA = process_data(INPUT_FILE)
    test_1a = 11
    test_2a = 31
    p1 = part1(TEST_DATA)
    p2 = part2(TEST_DATA)
    if test_1a: assert p1 == test_1a, f"Part 1: {p1} is the wrong answer"
    p1 = part1(DATA)
    print(f"Part 1: {p1}")
    if test_2a: assert p2 == test_2a, f"Part 2: {p2} is the wrong answer"
    p2 = part2(DATA)
    print(f"Part 2: {p2}")
from typing import List
import re

def part1(nums: List[str]) -> int:
    r = 0
    pat = r'mul\((\d{1,3}),(\d{1,3})\)'
    for s in nums:
        for m in re.findall(pat, s):
            r += (int(m[0]) * int(m[1]))
    return r

def part2(nums: List[str]) -> int:
    r = 0
    pat = r'do\(\)|mul\((\d{1,3}),(\d{1,3})\)|don\'t\(\)'
    on = True
    nums = "".join(nums)
    for m in re.finditer(pat, nums):
        if m.group(0) == "do()":
            on = True
        elif m.group(0) == "don't()":
            on = False
        else:
            if on: r += (int(m.group(1)) * int(m.group(2)))
    return r

def process_data(data: str) -> List[str]:
    lines = data.strip().split("\n")
    return lines

if __name__ == "__main__":
    from datetime import datetime
    from pathlib import Path
    from helpers import import_files
    TEST_FILE, INPUT_FILE = import_files(Path(__file__))
    TEST_DATA = process_data(TEST_FILE)
    DATA = process_data(INPUT_FILE)
    test_1a = 161
    test_2a = 48
    p1 = part1(TEST_DATA)
    p2 = part2(TEST_DATA)
    if test_1a: assert p1 == test_1a, f"Part 1: {p1} is the wrong answer"
    p1 = part1(DATA)
    print(f"Part 1: {p1}")
    if test_2a: assert p2 == test_2a, f"Part 2: {p2} is the wrong answer"
    p2 = part2(DATA)
    print(f"Part 2: {p2}")
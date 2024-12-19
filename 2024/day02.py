from typing import List

def part1(nums: List[List[int]], t=False) -> int:
    r = 0
    for row in nums:
        if row not in [sorted(row), sorted(row, reverse=True)]:
            continue
        safe = True
        for i in range(len(row)-1):
            if not 0 < abs(row[i+1]-row[i]) < 4:
                safe = False
        r += safe
    return r


def part2(nums: List[List[int]], t=False) -> int:
    r = 0
    for row in nums:
        safe = eval_row(row, False, t)
        r += safe
    return r

def eval_row(r: List[int], skipped: bool, t=False) -> bool:
    if (len(r) - len(set(r))) > 1:
        return False
    change = 0
    for i in range(len(r)-1):
        a = r[i]
        b = r[i+1]
        if not change:
            if not i:
                change = b-a
                continue
            elif not skipped:
                return eval_row(r[1:], True, t)
            else:
                return False
        elif (-4 < change < 0 and -4 < b-a < 0) or (4 > change > 0 and 4 > b-a > 0):
            change = b-a
        elif not skipped:
            if eval_row(r[:i] + r[i+1:], True, t) or eval_row(r[:i-1] + r[i:], True, t) or eval_row(r[:i+1] + r[i+2:], True, t):
                return True
            return False
        else:
            return False
    return True

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
    p1 = part1(TEST_DATA, True)
    if test_1a: assert p1 == test_1a, f"Part 1: {p1} is the wrong answer"
    p1 = part1(DATA)
    print(f"Part 1: {p1}")
    p2 = part2(TEST_DATA, True)
    if test_2a: assert p2 == test_2a, f"Part 2: {p2} is the wrong answer"
    p2 = part2(DATA, True) # too low: 660 or 668; too high: 689; not 678
    print(f"Part 2: {p2}")
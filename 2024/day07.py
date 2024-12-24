from typing import List, Tuple, Set

def part1(nums: List[Tuple[int, List[int]]], t = False) -> int:
    r = 0
    for n in nums:
        total = n[0]
        a = iterate(total, n[1][1:], n[1][0], t)
        if a: r += total
    return r

def iterate(total: int, ops: List[int], running: int, t = False) -> bool:
    if running > total:
        return False
    elif running == total and not ops:
        return True
    elif len(ops) == 1:
        return True in [total == running * ops[0], total == running + ops[0]]
    else:
        return True in [iterate(total, ops[1:], running + ops[0], t), iterate(total, ops[1:], running * ops[0], t)]



def part2(nums: List[Tuple[int, List[int]]], t = False) -> int:
    r = 0
    for n in nums:
        total = n[0]
        a = iterate2(total, n[1][1:], n[1][0], t)
        if a: r += total
    return r

def iterate2(total: int, ops: List[int], running: int, t = False) -> bool:
    if running > total:
        return False
    elif running == total and not ops:
        return True
    elif len(ops) == 1:
        return True in [total == running * ops[0], total == running + ops[0], total == running * (10 ** len(str(ops[0]))) + ops[0]]
    else:
        return True in [iterate2(total, ops[1:], running + ops[0], t), iterate2(total, ops[1:], running * ops[0], t), iterate2(total, ops[1:], running * (10 ** len(str(ops[0]))) + ops[0], t)]


def process_data(data: str) -> List[Tuple[int, List[int]]]:
    r = []
    lines = data.strip().split("\n")
    for line in lines:
        k, v = line.split(": ")
        r.append((int(k),[int(x) for x in v.split(" ")]))
    assert len(lines) == len(r), f"Duplicates in dictionary! {len(lines)} vs {len(r)}"
    return r

if __name__ == "__main__":
    from datetime import datetime
    from pathlib import Path
    from helpers import import_files
    TEST_FILE, INPUT_FILE = import_files(Path(__file__))
    TEST_DATA = process_data(TEST_FILE)
    DATA = process_data(INPUT_FILE)
    test_1a = 3749
    test_2a = 11387
    p1 = part1(TEST_DATA)
    if test_1a: assert p1 == test_1a, f"Part 1: {p1} is the wrong answer"
    p1 = part1(DATA)
    print(f"Part 1: {p1}")
    p2 = part2(TEST_DATA)
    if test_2a: assert p2 == test_2a, f"Part 2: {p2} is the wrong answer"
    p2 = part2(DATA)
    print(f"Part 2: {p2}") # low: 5046314343836
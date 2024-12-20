from typing import List
from itertools import product

def part1(nums: List[str], t = False) -> int:
    ret = 0
    for r in range(len(nums)):
        for c in range(len(nums[r])):
            if nums[r][c] == "X":
                ret += searcher(r, c, nums, t)
    return ret

def part2(nums: List[str]) -> int:
    offsets = [(1,1),(1,-1),(-1,1),(-1,-1)]
    ret = 0
    for r in range(1,len(nums)-1):
        for c in range(1,len(nums[r])-1):
            if nums[r][c] == "A":
                x = []
                for o in offsets:
                    x.append(nums[r + o[0]][c + o[1]])
                if x in [["M","M","S","S"],["S","S","M","M"],["S","M","S","M"],["M","S","M","S"]]:
                    ret += 1
    return ret

def searcher(row: int, col: int, inp: List[str], t = False) -> int:
    ret = 0
    offsets = product([0, 1, -1], repeat=2)
    for o in offsets:
        n = "X"
        try: n = inp[row + o[0]][col + o[1]] if (row + o[0] >= 0) and (col + o[1] >= 0) else inp[10000]
        except: continue
        if n == "M":
            try: n = inp[row + o[0]*2][col + o[1]*2] if (row + o[0]*2 >= 0) and (col + o[1]*2 >= 0) else inp[10000]
            except: continue
            if n == "A":
                try: n = inp[row + o[0]*3][col + o[1]*3] if (row + o[0]*3 >= 0) and (col + o[1]*3 >= 0) else inp[10000]
                except: continue
                if n == "S":
                    ret += 1
    return ret

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
    test_1a = 18
    test_2a = 9
    p1 = part1(TEST_DATA)
    if test_1a: assert p1 == test_1a, f"Part 1: {p1} is the wrong answer"
    p1 = part1(DATA)
    print(f"Part 1: {p1}")
    p2 = part2(TEST_DATA)
    if test_2a: assert p2 == test_2a, f"Part 2: {p2} is the wrong answer"
    p2 = part2(DATA)
    print(f"Part 2: {p2}") # too high: 1914, 1869
from typing import List
from statistics import median

def part1(nums: List[int]) -> int:
    mid = int(median(nums))
    total = 0
    for x in nums:
        total += abs(mid - x)
    return total

def part2(nums: List[int]) -> int:
    av = int(sum(nums)/len(nums)) # not sure why, but rounding down by using int() was correct, not rounding properly using round()
    total = 0
    for x in nums:
        total += sum(range(abs(av - x)+1))
    return total

if __name__ == "__main__":
    import os, timeit
    FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    file = os.path.splitext(__file__)[0][-5:]
    with open(os.path.join(FILE_DIR, file + ".input")) as f:
        DATA = f.read().strip()
    DATA = [int(x) for x in DATA.split(",")] # example code
    print(f"Part 1: {part1(DATA)}")
    print(f"Part 2: {part2(DATA)}") # 101571337 too high
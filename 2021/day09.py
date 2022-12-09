from typing import List, Dict, Tuple
    
def neighbors(t: Tuple):
    x, y = t
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

def part1(nums: Dict[Tuple[int,int], int]) -> int:
    retVal = 0
    bad = False
    for pt in nums.keys():
        for n in neighbors(pt):
            try:
                if nums[n] <= nums[pt]:
                    bad = True
                    break
            except KeyError:
                if test: print(f"key error") # nothing
        if not bad:
            if test: print(f"pt: {pt} adding: {nums[pt] + 1}")
            retVal += nums[pt] + 1
        bad = False
    return retVal

def part2(nums: Dict[Tuple[int,int], int]) -> int:
    return




if __name__ == "__main__":
    import os, timeit
    from pathlib import Path
    test = False
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    DATA = INPUT_FILE.read_text().strip().split()
    # print(DATA)
    COORDS = {}
    y = 0
    for row in DATA:
        x = 0
        while x < len(row):
            COORDS[(x, y)] = int(DATA[y][x])
            x += 1
        y += 1
    # print(COORDS)
    print(f"Part 1: {part1(COORDS)}") # 6202 too high
    print(f"Part 2: {part2(DATA)}")
from typing import List, Dict, Tuple
import math
    
def neighbors(t: Tuple):
    x, y = t
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

def part1(nums: Dict[Tuple[int,int], int]) -> int:
    lows = []
    bad = False
    for pt in nums.keys():
        for n in neighbors(pt):
            try:
                if nums[n] <= nums[pt]:
                    bad = True
                    break
            except KeyError:
                if test: print(f"key error")
        if not bad:
            if test: print(f"pt: {pt} adding: {nums[pt] + 1}")
            lows.append(pt)
        bad = False
    return lows

def part2(nums: Dict[Tuple[int,int], int]) -> int:
    lows = part1(nums)
    highs = []
    # find each neighbor that isn't nine, then each neighbor of that that isn't nine, etc using a set
    for pt in lows:
        checked = set()
        new_pts = [pt]
        while new_pts:
            next_pts = []
            for p in new_pts:
                for n in neighbors(p):
                    if n in checked:
                        continue
                    try:
                        if nums[n] < 9:
                            next_pts.append(n)
                    except KeyError:
                        if test: print(f"key error")
            checked = checked.union(set(new_pts))
            new_pts = next_pts.copy()
        highs.append(len(checked))
    highs.sort()
    if test: print(highs)
    return highs[-3:]

if __name__ == "__main__":
    import os, timeit
    from pathlib import Path
    test = False
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    DATA = INPUT_FILE.read_text().strip().split()
    COORDS = {}
    y = 0
    for row in DATA:
        x = 0
        while x < len(row):
            COORDS[(x, y)] = int(DATA[y][x])
            x += 1
        y += 1
    print(f"Part 1: {sum((COORDS[x] + 1) for x in part1(COORDS))}") # 6202 too high sum((nums[x] + 1) for x in lows)
    print(f"Part 2: {math.prod(part2(COORDS))}")
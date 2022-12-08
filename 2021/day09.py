from typing import List, NamedTuple

class Coord(NamedTuple):
    x: int
    y: int
    val: int

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y, self.val)
    
    def neighbors(self):
        return [self + Coord(0, 1, 0), self + Coord(0, -1, 0), self + Coord(1, 0, 0), self + Coord(-1, 0, 0)]

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

def part1(nums: List[Coord]) -> int:
    retVal = 0
    bad = False
    for pt in nums:
        for n in pt.neighbors():
            if n in nums:
                if test: print(f"{nums[nums.index(n)].val}")
                if nums[nums.index(n)].val < pt.val:
                    bad = True
                    break
        if not bad:
            retVal += pt.val + 1
            bad = False
        else:
            bad = False
            continue
    return retVal

def part2(co: List[Coord]) -> int:
    return




if __name__ == "__main__":
    import os, timeit
    from pathlib import Path
    test = False
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    DATA = INPUT_FILE.read_text().strip().split()
    # print(DATA)
    COORDS = []
    y = 0
    for row in DATA:
        x = 0
        while x < len(row):
            COORDS.append(Coord(x, y, int(row[x])))
            x += 1
        y += 1
    # print(COORDS)
    print(f"Part 1: {part1(COORDS)}") # 6202 too high
    print(f"Part 2: {part2(DATA)}")
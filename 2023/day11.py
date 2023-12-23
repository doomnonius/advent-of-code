from typing import List, Set, Tuple, Dict
from day10 import Coord
from itertools import combinations

stack: List[Tuple[int, Coord]] = []
history: Set[Coord] = set()

def process_data(inp: str) -> Tuple[Dict[Coord, str], Set[Coord], Set[Coord]]:
    points = {}
    empty_row = set()
    empty_col = set()
    inp = inp.split("\n")
    for y in range(len(inp)):
        if set(inp[y]) == {'.'}:
            empty_row.add(y)
        for x in range(len(inp[y])):
            points[Coord(x, y)] = inp[y][x]
    for x in range(len(inp[0])):
        curr_set = set()
        for y in range(len(inp)):
            curr_set.add(inp[y][x])
        if curr_set == {'.'}:
            empty_col.add(x)
    print(empty_row)
    print(empty_col)
    return (points, empty_row, empty_col)


def part1(points: Dict[Coord, str], rows: Set[int], cols: Set[int], expa: int, test: bool = False) -> int:
    # thought: record which segments are "expanded" and each time the path goes through one, increment the step counter by one
    
    # def next_moves(point: Coord, count: int) -> None:
    # 	""" doesn't return anything, just adds to stack
    # 	"""
    r = 0
    gals = [k for k,v in points.items() if v == "#"]
    if test: print(gals)
    pairs = combinations(gals, 2)
    for p in pairs:
        if test: print(p)
        d = 0
        x0, x1 = p[0].x, p[1].x
        y0, y1 = p[0].y, p[1].y
        d = abs(x0-x1) + abs(y0-y1)
        for row in rows:
            if min(y0,y1) < row < max(y0,y1):
                d += (expa - 1)
        for col in cols:
            if min(x0,x1) < col < max(x0,x1):
                d += (expa - 1)
        r += d
    return r


    # I think I'll need to make sure to sort the stack?
    return


def part2(nums: List[int]) -> int:
    return


if __name__ == "__main__":
    import os, timeit
    from pathlib import Path
    test = False
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    DATA = INPUT_FILE.read_text().strip()
    DATA, ROWS, COLS = process_data(DATA)
    print(f"Part 1: {part1(DATA, ROWS, COLS, 2, test)}")
    print(f"Part 2: {part1(DATA, ROWS, COLS, 1000000, test)}")
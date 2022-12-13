from typing import List, Dict, Tuple
import string
lower = string.ascii_lowercase

def neighbors(t: Tuple):
    x, y = t
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

def part1(coords: Dict[Tuple, str]) -> int:
    # thoughts: go through and map the spots that have neighbors that they can move to
    # then work from there somehow
    # maybe I can find a quick way to list all possible paths with this info and find the shortest?
    adj = {x:[] for x in coords.keys()}
    start = [k for k,v in coords.items() if v == "S"][0]
    end = [k for k,v in coords.items() if v == "E"][0]
    for c in coords.keys():
        for n in neighbors(c):
            if n not in coords.keys():
                continue
            if lower.index(coords[n]) <= (lower.index(coords[c]) + 1):
                adj[c] += n
    if test: print(adj)
    return





def part2(nums: List[int]) -> int:
    return




if __name__ == "__main__":
    import os, timeit
    from pathlib import Path
    test = True
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    DATA = INPUT_FILE.read_text().strip().split()
    COORDS = {}
    for y in range(len(DATA)):
        for x in range(len(DATA[y])):
            COORDS[(x,y)] = DATA[y][x]
    print(COORDS)
    print(f"Part 1: {part1(COORDS)}")
    print(f"Part 2: {part2(COORDS)}")
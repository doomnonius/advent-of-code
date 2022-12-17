from typing import List, Dict, Tuple, Set
import string

def neighbors(t: Tuple[int, int]) -> List[Tuple[int, int]]:
    x, y = t
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

def part1(coords: Dict[Tuple, str]) -> int:
    # thoughts: go through and map the spots that have neighbors that they can move to
    # then work from there somehow
    # maybe I can find a quick way to list all possible paths with this info and find the shortest?
    adj = {x:[] for x in coords.keys()}
    start = [k for k,v in coords.items() if v == 44][0]
    end = [k for k,v in coords.items() if v == 30][0]
    for k in coords.keys():
        if coords[k] == 44:
            coords[k] = 0
        if coords[k] == 30:
            coords[k] = 25
    for c in coords.keys():
        for n in neighbors(c):
            if n not in coords.keys():
                continue
            if coords[n] <= (coords[c] + 1):
                adj[c].append(n)
    # if test: print([k for k,v in adj.items() if len(v) == 2])
    r = recursion(adj, start, end, set([start]))
    if test: print(f"r: {r}")
    return min([len(x) for x in r])

def recursion(near: Dict[Tuple, List[Tuple]], s: Tuple, e: Tuple, seen: Set[Tuple]): # can I even remember how to write a recursive function?
    # if test: print(f"seen: {seen}")
    returned = []
    for n in near[s]:
        if test and s == (0,0): print(n)
        if n in seen:
            continue
        if n == e:
            print("found the end!")
            if test: print(f"seen after found: {seen}")
            returned.append(seen)
        seen.add(n)
        returning = recursion(near, n, e, seen.copy())
        if returning and returning not in returned:
            # if test: print(returning)
            returned.extend(returning)
    # if test: print(returned)
    return returned



def part2(nums: List[int]) -> int:
    return




if __name__ == "__main__":
    import os, timeit
    from pathlib import Path
    test = False
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    DATA = INPUT_FILE.read_text().strip().split()
    COORDS = {}
    for y in range(len(DATA)):
        for x in range(len(DATA[y])):
            COORDS[(x,y)] = string.ascii_letters.index(DATA[y][x])
    # if test: print(COORDS)
    print(f"Part 1: {part1(COORDS)}")
    print(f"Part 2: {part2(COORDS)}")
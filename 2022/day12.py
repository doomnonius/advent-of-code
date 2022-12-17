from typing import List, Tuple, Dict
import string

def neighbors(t: Tuple[int, int]) -> List[Tuple[int, int]]:
    x, y = t
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

def part1(coords: Dict[Tuple, str], end: Tuple, adj: Dict[Tuple, List[Tuple]]) -> int:
    # now we'll try a point map
    dist = {x:1000 for x in coords.keys()}
    dist[end] = 0
    if test: print(f"end: {end}")
    # find the neighbors of each spot
    # now find the distant from the start for each spot - will this get computationally out of hand?
    to_do = [(adj[end], 1)]
    while to_do:
        now = to_do.pop()
        for n in now[0]:
            if dist[n] > now[1]:
                dist[n] = now[1]
                next = adj[n].copy()
                if n in next: next.remove(n)
                to_do.append((next, now[1] + 1))
    if test: print(f"distances: {dist}")
    return dist

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
    # if test: print(f"coords: {COORDS}")
    start = [k for k,v in COORDS.items() if v == 44][0]
    end = [k for k,v in COORDS.items() if v == 30][0]
    for k in COORDS.keys():
        if COORDS[k] == 44: COORDS[k] = 0
        if COORDS[k] == 30: COORDS[k] = 25
    adj = {x:[] for x in COORDS.keys()}
    for c in COORDS.keys():
        for n in neighbors(c):
            if n not in COORDS.keys():
                continue
            if COORDS[n] >= (COORDS[c] - 1):
                adj[c].append(n)
    point_map = part1(COORDS, end, adj)
    print(f"Part 1: {point_map[start]}") # not 337
    print(f"Part 2: {min([v for k,v in point_map.items() if COORDS[k] == 0])}")
    print(f"Time: {timeit.timeit('part1(COORDS, end, adj)', setup='from __main__ import part1, COORDS,end, adj', number = 10)/10}")
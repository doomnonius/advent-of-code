from typing import List, Tuple, Dict
import string

class Nav:
    def __init__(self, pos: Tuple, turn: Tuple):
        self.pos = pos
        self.face = turn
        self.turn_right = {
            (1, 0): (0, 1),
            (0, 1): (-1, 0),
            (-1, 0): (0, -1),
            (0, -1): (1, 0)
        }
        self.turn_left = {
            (1, 0): (0, -1),
            (0, 1): (1, 0),
            (-1, 0): (0, 1),
            (0, -1): (-1, 0)
        }
        self.path = [pos]

def neighbors(t: Tuple[int, int]) -> List[Tuple[int, int]]:
    x, y = t
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

def part1(coords: Dict[Tuple, str], start: Tuple, end: Tuple) -> int:
    # now we'll try a point map
    adj = {x:[] for x in coords.keys()}
    dist = {x:1000 for x in coords.keys()}
    dist[start] = 0
    if test: print(f"start: {start}")
    # find the neighbors of each spot
    for c in coords.keys():
        for n in neighbors(c):
            if n not in coords.keys():
                continue
            if coords[n] <= (coords[c] + 1):
                adj[c].append(n)
    # now find the distant from the start for each spot - will this get computationally out of hand?
    to_do = [(adj[start], 1)]
    while to_do:
        now = to_do.pop()
        for n in now[0]:
            if dist[n] > now[1]:
                dist[n] = now[1]
                next = adj[n].copy()
                if n in next: next.remove(n)
                to_do.append((next, now[1] + 1))
    if test: print(f"distances: {dist}")
    return(dist[end])


def part2(coords: Dict[Tuple, str], end: Tuple) -> int:
    adj = {x:[] for x in coords.keys()}
    dist = {x:1000 for x in coords.keys()}
    starts = [k for k,v in coords.items() if v == 0]
    # find the neighbors of each spot
    for c in coords.keys():
        for n in neighbors(c):
            if n not in coords.keys():
                continue
            if coords[n] <= (coords[c] + 1):
                adj[c].append(n)
    # now find the distant from the start for each spot - will this get computationally out of hand?
    retVal = 1000
    for start in starts:
        if test: print(f"start: {start}")
        dist[start] = 0
        to_do = [(adj[start], 1)]
        while to_do:
            now = to_do.pop()
            for n in now[0]:
                if dist[n] > now[1]:
                    dist[n] = now[1]
                    next = adj[n].copy()
                    if n in next: next.remove(n)
                    to_do.append((next, now[1] + 1))
        if test: print(f"distances: {dist}")
        if dist[end] < retVal:
            retVal = dist[end]
    return retVal

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
    print(f"Part 1: {part1(COORDS, start, end)}") # not 337
    print(f"Part 2: {part2(COORDS, end)}")
import hashlib, itertools
from typing import List, Tuple
from day01 import Coord

stack: List[Tuple[Coord, str]] = [] # stack prioritized based on string length
all_rooms = {Coord(x,y) for x in range(4) for y in range(4)}

def hash_key(key:str, c:Coord):
    pass

def next_moves(key:str, loc:Coord):
    """ doesn't return anything, just adds to the stack
    """
    hsh = list(hashlib.md5(key.encode('utf-8')).hexdigest()[0:4]) # order: UDLR
    dirs = [1 if x in "bcdef" else 0 for x in hsh] # order: UDLR
    # coord.neighbors() returns in order SNEW
    neighbors = loc.neighbors()
    if dirs[0] and neighbors[1] in all_rooms: # north
        stack.append((neighbors[1], key + "U"))
    if dirs[1] and neighbors[0] in all_rooms: # south
        stack.append((neighbors[0], key + "D"))
    if dirs[2] and neighbors[3] in all_rooms: # west
        stack.append((neighbors[3], key + "L"))
    if dirs[3] and neighbors[2] in all_rooms: # east
        stack.append((neighbors[2], key + "R"))

def part1(key: str, loc: Coord, target: Coord) -> str:
    next_moves(key, loc)
    while True:
        c, new_key = stack.pop(0)
        if c == target:
            return new_key
        next_moves(new_key, c)

def part2(key: str, loc: Coord, target: Coord):
    hist = set()
    next_moves(key,loc)
    while stack:
        c, new_key = stack.pop(0)
        if c == target:
            hist.add(new_key)
            continue
        next_moves(new_key, c)
    return max(len(x) for x in hist)-8

if __name__ == "__main__":
    import timeit
    DATA = "pslxynzg"
    TEST_DATA = "ulqzkmiv"
    print(f"Part one: {part1(DATA, Coord(0,0), Coord(3,3))}")
    stack: List[Tuple[Coord, str]] = []
    print(f"Part two: {part2(DATA, Coord(0,0), Coord(3,3))}")
    # print(f"Time: {timeit.timeit('part1(DATA, LENGTH2)', setup='from __main__ import DATA, LENGTH2, part1', number = 1)}")
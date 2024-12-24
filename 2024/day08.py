from typing import List, Dict
from helpers import Coord
from itertools import combinations

def part1(data: Dict[str, List[Coord]], t = False) -> int:
    r = set()
    max_x = max(z.x for z in data["."])
    max_y = max(z.y for z in data["."])
    for k in data.keys():
        if k == ".": continue
        if t:
            print(f"{k}:{data[k]}")
        for c in combinations(data[k], 2):
            if t: print(f"{c[0], c[1]}")
            offset = c[0] - c[1]
            up = c[0] + offset
            down = c[1] - offset
            if 0 <= up.x <= max_x and 0 <= up.y <= max_y:
                r.add(up)
            if 0 <= down.x <= max_x and 0 <= down.y <= max_y:
                r.add(down)
    return len(r)





def part2(data: Dict[str, List[Coord]], t = False) -> int:
    r = set()
    max_x = max(z.x for z in data["."])
    max_y = max(z.y for z in data["."])
    for k in data.keys():
        if k == ".": continue
        if t:
            print(f"{k}:{data[k]}")
        for c in combinations(data[k], 2):
            if t: print(f"{c[0], c[1]}")
            offset = c[0] - c[1]
            up = c[1] + offset
            down = c[0] - offset
            while 0 <= up.x <= max_x and 0 <= up.y <= max_y:
                r.add(up)
                up = up + offset
            while 0 <= down.x <= max_x and 0 <= down.y <= max_y:
                r.add(down)
                down = down - offset
    return len(r)




def process_data(data: str) -> Dict[str, List[Coord]]:
    r = dict()
    lines = data.strip().split("\n")
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            c = lines[row][col]
            if c not in r.keys():
                r[c] = [Coord(col, row)]
            else:
                r[c].append(Coord(col, row))
    return r

if __name__ == "__main__":
    from datetime import datetime
    from pathlib import Path
    from helpers import import_files
    TEST_FILE, INPUT_FILE = import_files(Path(__file__))
    TEST_DATA = process_data(TEST_FILE)
    DATA = process_data(INPUT_FILE)
    test_1a = 14
    test_2a = 34
    p1 = part1(TEST_DATA, True)
    if test_1a: assert p1 == test_1a, f"Part 1: {p1} is the wrong answer"
    p1 = part1(DATA)
    print(f"Part 1: {p1}")
    p2 = part2(TEST_DATA)
    if test_2a: assert p2 == test_2a, f"Part 2: {p2} is the wrong answer"
    p2 = part2(DATA)
    print(f"Part 2: {p2}")
from typing import List, Set, Tuple, Dict
from helpers import Coord

def part1(pos: Coord, map: Dict[Coord, str]) -> int:
    visited = set()
    d = start_dict[pos.char]
    loop = dict()
    while pos in map.keys():
        if pos in visited:
            if (pos, d) in loop.keys():
                loop[(pos, d)] += 1
                if loop[(pos, d)] > 1:
                    return 0
            else:
                loop[(pos, d)] = 1
        visited.add(pos)
        next_pos = pos + move_dict[d]
        try:
            if map[next_pos] == "#":
                d = turn_dict[d]
            else:
                pos = next_pos
        except:
            break
    return len(visited)

start_dict = {
    "^":0,
    ">":1,
    "v":2,
    "<":3
}
move_dict = {
    0:Coord(-1,0,"k"),
    1:Coord(0, 1,"k"),
    2:Coord(1,0,"k"),
    3:Coord(0, -1,"k")
}
turn_dict = {
    0:1,
    1:2,
    2:3,
    3:0
}

def part2(pos: Coord, map: Dict[Coord, str], t = False) -> int:
    r = 0
    for k,v in map.items():
        if v == ".":
            map[k] = "#"
            if not part1(pos, map):
                r += 1
            map[k] = "."
    return r

def process_data(data: str) -> Tuple[Coord, Dict[Coord, str]]:
    map: Dict[Coord, str] = dict()
    lines = data.strip().split("\n")
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            char = lines[row][col]
            map[Coord(row,col,"k")] = char
            if lines[row][col] not in "#.":
                start = Coord(row, col, char)
    return start, map

if __name__ == "__main__":
    from datetime import datetime
    from pathlib import Path
    from helpers import import_files
    TEST_FILE, INPUT_FILE = import_files(Path(__file__))
    TEST_DATA, TEST_MAP = process_data(TEST_FILE)
    DATA, MAP = process_data(INPUT_FILE)
    test_1a = 41
    test_2a = 6
    p1 = part1(TEST_DATA, TEST_MAP)
    if test_1a: assert p1 == test_1a, f"Part 1: {p1} is the wrong answer"
    p1 = part1(DATA, MAP)
    print(f"Part 1: {p1}")
    p2 = part2(TEST_DATA, TEST_MAP)
    if test_2a: assert p2 == test_2a, f"Part 2: {p2} is the wrong answer"
    p2 = part2(DATA, MAP, True)
    print(f"Part 2: {p2}") # works, but inefficient (1793)
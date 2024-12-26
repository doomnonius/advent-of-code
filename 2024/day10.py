from typing import List, Set, Dict
from helpers import Coord

def part1(map: Dict[Coord, int], t=False) -> int:
    r = 0
    starts: List[Coord] = [k for k,v in map.items() if v == 0]
    next_paths: Set[Coord] = set()
    for s in starts:
        end = False
        paths: Set[Coord] = {s}
        while paths:
            for k in paths:
                for n in k.neighbors():
                    if n not in map:
                        continue
                    if map[n] == map[k] + 1 and map[n] < 9:
                        n.char = map[k] + 1
                        next_paths.add(n)
                    elif map[n] == map[k] + 1 and map[n] == 9:
                        end = True
                        next_paths.add(n)
            if end:
                r += len(next_paths)
                next_paths = set()
            paths = next_paths.copy()
            next_paths = set()
    return r





def part2(map: Dict[Coord, int], t=False) -> int:
    r = 0
    starts: List[Coord] = [k for k,v in map.items() if v == 0]
    next_paths: List[Coord] = []
    for s in starts:
        end = False
        paths: List[Coord] = [s]
        while paths:
            for k in paths:
                for n in k.neighbors():
                    if n not in map:
                        continue
                    if map[n] == map[k] + 1 and map[n] < 9:
                        n.char = map[k] + 1
                        next_paths.append(n)
                    elif map[n] == map[k] + 1 and map[n] == 9:
                        end = True
                        next_paths.append(n)
            if end:
                r += len(next_paths)
                next_paths = []
            paths = next_paths.copy()
            next_paths = []
    return r


def process_data(data: str) -> Dict[Coord, int]:
    map = dict()
    lines = data.strip().split("\n")
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            map[Coord(col, row, int(lines[row][col]))] = int(lines[row][col])
    return map

if __name__ == "__main__":
    from datetime import datetime
    from pathlib import Path
    from helpers import import_files
    TEST_FILE, INPUT_FILE = import_files(Path(__file__))
    TEST_DATA = process_data(TEST_FILE)
    DATA = process_data(INPUT_FILE)
    test_1a = 36
    test_2a = 81
    p1 = part1(TEST_DATA, True)
    if test_1a: assert p1 == test_1a, f"Part 1: {p1} is the wrong answer"
    p1 = part1(DATA)
    print(f"Part 1: {p1}")
    p2 = part2(TEST_DATA, True)
    if test_2a: assert p2 == test_2a, f"Part 2: {p2} is the wrong answer"
    p2 = part2(DATA)
    print(f"Part 2: {p2}")
from typing import List, Set, Tuple, Dict
from helpers import Coord

def part1(pos: Coord, map: Dict[Coord, str]) -> int:
    visited = set()
    d = start_dict[pos.char]
    while pos in map.keys():
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
# inv_dict = {v:k for k,v in turn_dict.items()}

def part2(pos: Coord, map: Dict[Coord, str], t = False) -> int:
    start = pos
    visited = set()
    blocks = set()
    d = start_dict[pos.char]
    while pos in map.keys():
        # if t: print(f"Location: {pos}")
        next_pos = pos + move_dict[d]
        try:
            if map[next_pos] == "#":
                d = turn_dict[d]
            else:
                visited.add((pos, d))
                turn_pos = pos
                block = pos + move_dict[d]
                turn_d = turn_dict[d]
                countdown = 300
                while turn_pos in map.keys() and block in map.keys() and countdown > 0 and block != start:
                    next_turn_pos = turn_pos + move_dict[turn_d]
                    try:
                        countdown -= 1
                        if map[next_turn_pos] == "#":
                            turn_d = turn_dict[turn_d]
                        else:
                            turn_pos = next_turn_pos
                            if (turn_pos, turn_d) in visited:
                                # if t: print(f"block: {block}")
                                blocks.add(block)
                                break
                    except:
                        break
                # if t: print(f"added ({pos}, {d})")
                pos = next_pos
        except Exception as e:
            # if t: print(f"error: {e}")
            break
    # print(blocks)
    return len(blocks)

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
    p2 = part2(TEST_DATA, TEST_MAP, True)
    if test_2a: assert p2 == test_2a, f"Part 2: {p2} is the wrong answer"
    p2 = part2(DATA, MAP)
    print(f"Part 2: {p2}") # works, but inefficient (1793)
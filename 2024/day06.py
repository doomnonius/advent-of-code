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
rev_dict = {
    1:3,
    3:1,
    0:2,
    2:0
}
inv_dict = {
    0:3,
    3:2,
    2:1,
    1:0
}

def part2(pos: Coord, map: Dict[Coord, str], t = False) -> int:
    start = pos
    visited = set()
    loops = set()
    crossovers = dict()
    d = start_dict[pos.char]
    while pos in map.keys():
        # if t: print(f"Location: {pos}")
        visited.add(pos)
        if pos in crossovers.keys() and d in crossovers[pos]:
            loops.add(pos + move_dict[d])
            if t: print(f"Added {pos + move_dict[d]} to loops")
        next_pos = pos + move_dict[d]
        try:
            if map[next_pos] == "#":
                rev_d = rev_dict[d]
                inv_d = inv_dict[d]
                d = turn_dict[d]
                rev_pos = pos
                while rev_pos in map.keys():
                    if rev_pos in crossovers.keys():
                        crossovers[rev_pos].append(inv_d)
                    else:
                        crossovers[rev_pos] = [inv_d]
                    # if t: print(f"added {rev_pos}: {inv_d} to crossovers!")
                    next_rev_pos = rev_pos + move_dict[rev_d]
                    try:
                        if map[next_rev_pos] == "#":
                            break
                        else:
                            rev_pos =  next_rev_pos
                    except:
                        break
            else:
                pos = next_pos
        except Exception as e:
            # if t: print(f"error: {e}")
            break
    # pos = start
    # d = start_dict[pos.char]
    # # if t: print(crossovers)
    # while pos in map.keys():
    #     # if t: print(f"Location: {pos}")
    #     visited.add(pos)
    #     if pos in crossovers.keys() and d in crossovers[pos]:
    #         if pos + move_dict[d] in map.keys() and pos + move_dict[d] != start and map[pos + move_dict[d]] != "#":
    #             loops.add(pos + move_dict[d])
    #         if t: print(f"Added {pos + move_dict[d]} to loops, at {pos} moving {d}")
    #         if t: print(f"Crossovers: {crossovers[pos]}")
    #     next_pos = pos + move_dict[d]
    #     try:
    #         if map[next_pos] == "#":
    #             d = turn_dict[d]
    #         else:
    #             pos = next_pos
    #     except Exception as e:
    #         # if t: print(f"error: {e}")
    #         break
    return len(loops)

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
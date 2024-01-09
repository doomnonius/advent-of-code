from typing import List, Set
from day10 import Coord

def part1(data: Set[Coord], steps: int, start: Coord) -> int:
    count = 0
    stack = [start]
    seen_odd = set()
    seen_even = set()
    while count < steps:
        count += 1
        new_stack = []
        while stack:
            curr_loc = stack.pop()
            if count % 2:
                for x in curr_loc.neighbors():
                    if x in data and x not in seen_odd:
                        seen_odd.add(x)
                        new_stack.append(x)
            else:
                for x in curr_loc.neighbors():
                    if x in data and x not in seen_even:
                        seen_even.add(x)
                        new_stack.append(x)
        stack = new_stack[0:]
        # if count % 2: print(f"odd count: {len(seen_odd)}; round: {count}")
    return len(seen_even)


def part2(rocks: Set[Coord], steps: int, start: Coord, height: int, width: int) -> int:
    stack = [start]
    increase = [0]
    increase_diff = []
    totals = [0]
    seen_odd = set()
    seen_even = set()
    count = 0
    target = 0
    while count < steps:
        count += 1
        new_stack = []
        while stack:
            curr_loc = stack.pop()
            if (curr_loc.x > width or curr_loc.y > height) and not target:
                target = count + 1000
            if count % 2:
                for z in curr_loc.neighbors():
                    if Coord(z.x % width, z.y % height) not in rocks and z not in seen_odd:
                        seen_odd.add(z)
                        new_stack.append(z)
                # print(f"odd count: {len(seen_odd)}; round: {count}")
            else:
                for z in curr_loc.neighbors():
                    if Coord(z.x % width, z.y % height) not in rocks and z not in seen_even:
                        seen_even.add(z)
                        new_stack.append(z)
        stack = new_stack[0:]
        if count % 2:
            increase.append(len(seen_odd) - totals[-1])
            totals.append(len(seen_odd))
            increase_diff.append(increase[-1] - increase[-2])
            # print(f"odd count: {len(seen_odd)}; round: {count}")
        if count == target:
            print(increase)
            print(totals)
            print(increase_diff)
            break
    return




if __name__ == "__main__":
    from datetime import datetime
    from pathlib import Path
    test = False
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    RAW_DATA = INPUT_FILE.read_text().strip().split("\n")
    DATA = set()
    ROCKS = set()
    for row in range(len(RAW_DATA)):
        for col in range(len(RAW_DATA[row])):
            if RAW_DATA[row][col] != "#":
                DATA.add(Coord(col,row))
                if RAW_DATA[row][col] == "S":
                    START = Coord(col,row)
            else:
                ROCKS.add(Coord(col,row))
    print(f"Part 1: {part1(DATA, 64, START)}") # not 7145, too high
    print(f"Part 2: {part2(ROCKS, 26501365, START, row, col)}")
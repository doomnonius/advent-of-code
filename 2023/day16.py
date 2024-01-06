from typing import List, Dict, Tuple, Set
from day10 import Coord

def part1(data: Dict[Coord,str], current: Coord, dir: int, visited: Set[Tuple[Coord, int]] = set()) -> int:
    
    def find_next(loc: Coord, dir):
        move_d = {
            1 : {
                "|" : [(loc.up(), 0), (loc.down(), 2)],
                "\\" : [(loc.down(), 2)],
                "/" : [(loc.up(), 0)],
                "." : [(loc.right(), 1)],
                "-" : [(loc.right(), 1)]
            },
            2 : {
                "|" : [(loc.down(), 2)],
                "\\" : [(loc.right(), 1)],
                "/" : [(loc.left(), 3)],
                "." : [(loc.down(), 2)],
                "-" : [(loc.right(), 1), (loc.left(), 3)]
            },
            3 : {
                "|" : [(loc.up(), 0), (loc.down(), 2)],
                "\\" : [(loc.up(), 0)],
                "/" : [(loc.down(), 2)],
                "." : [(loc.left(), 3)],
                "-" : [(loc.left(), 3)]
            },
            0 : {
                "|" : [(loc.up(), 0)],
                "\\" : [(loc.left(), 3)],
                "/" : [(loc.right(), 1)],
                "." : [(loc.up(), 0)],
                "-" : [(loc.right(), 1), (loc.left(), 3)]
            }
        }
        for x in move_d[dir][data[loc]]:
            stack.append(x)
    
    visited.add((current, dir))
    stack: List[Tuple[Coord,int]] = []
    find_next(current, dir)
    while stack:
        current, dir = stack.pop()
        if (current, dir) in visited:
            continue
        if current in data:
            visited.add((current, dir))
            find_next(current, dir)
    # print(visited)
    return len({x[0] for x in visited}), visited

def part2(data: Dict[Coord,str], visited: Set[Tuple[Coord, int]]) -> int:
    max_x = len({x for x in data if x.y == 0})-1
    max_y = len({y for y in data if y.x == 0})-1
    edges = {(z, 1) for z in data if z.x == 0} | {(z, 2) for z in data if z.y == 0} | {(z,3) for z in data if z.x == max_x} | {(z,0) for z in data if z.y == max_y}
    assert len(edges) == 440 or len(edges) == 40, "ERROR, wrong number of edges!"
    answers = {x:part1(data, x[0], x[1], visited.copy())[0] for x in edges}
    print(answers)
    return max(answers.values())




if __name__ == "__main__":
    from datetime import datetime
    from pathlib import Path
    test = False
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    RAW_DATA = INPUT_FILE.read_text().strip().split("\n")
    DATA = {}
    for row in range(len(RAW_DATA)):
        for col in range(len(RAW_DATA[row])):
            DATA[Coord(col,row)] = RAW_DATA[row][col]
    p1, visited = part1(DATA, Coord(0,0), 1)
    print(f"Part 1: {p1}") # 11442 too high
    start = datetime.now()
    print(f"Part 2: {part2(DATA, visited)} after {datetime.now()-start}") # 8330 too low

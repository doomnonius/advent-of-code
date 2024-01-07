from typing import List, Dict, Tuple
from day10 import Coord

def map_to_mid(data: Dict[Coord, int], min_move: int, max_move: int, cut: int) -> Dict:
    
    def find_next(loc: Coord, dir: int, streak: int, total: int):
        r = []
        turn_d: Dict[int,List[Tuple[Coord, int]]] = {
            1 : [(loc.up(), 0), (loc.right(), 1), (loc.down(), 2)],
            2 : [(loc.right(), 1), (loc.down(), 2), (loc.left(), 3)],
            3 : [(loc.down(), 2), (loc.left(), 3), (loc.up(), 0)],
            0 : [(loc.left(), 3), (loc.up(), 0), (loc.right(), 1)]
        }
        for x in turn_d[dir]:
            n, d = x
            if d == dir:
                if streak == max_move:
                    continue
                else:
                    new_streak = streak + 1
            else:
                if streak < min_move:
                    continue
                new_streak = 1
            if n not in min_d:
                min_d[n] = dict()
            if (new_streak, d) not in min_d[n]:
                min_d[n].update({(new_streak, d):10000})
            if n in data:
                new_total = total + data[n]
                if new_total < min_d[n][(new_streak, d)]:
                    min_d[n][(new_streak, d)] = new_total
                    r.append((n, d, new_streak, new_total))
        return r

    min_d: Dict[Coord, Dict[Tuple[int, int], int]] = {}
    target = list(data.keys())[-1]
    # print(f"target: {target}")
    stack: List[Tuple[Coord, int, int, int]] = find_next(Coord(0,0), 1, 1, 0)
    solutions = []
    test = 0
    new_stack: List[Tuple[Coord, int, int, int]] = []
    while True:
        if not stack:
            break
        while stack:
            loc, d, streak, total = stack.pop(0)
            if loc == target and streak >= min_move:
                solutions.append(total)
            for x in find_next(loc, d, streak, total):
                new_stack.append(x)
        new_stack.sort(key=lambda x: x[3])
        stack = new_stack[0:cut]
        new_stack = []
    return min(v for k,v in min_d[target].items() if k[0] >= min_move)



def part1(data: Dict[Coord, int], min_move: int, max_move: int, cut: int) -> int:
    mid = len(data) // 2




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
            DATA[Coord(col,row)] = int(RAW_DATA[row][col])
    # print(DATA)
    print(f"Part 1: {part1(DATA, 1, 3, 1000)}")
    print(f"Part 2: {part1(DATA, 4, 10, 1000000000)}") # not 1398, too high; 1320 also; 1310 also; 1286 is wrong
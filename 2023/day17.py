from typing import List, Dict, Tuple
import heapq
from day10 import Coord

def part1(data: Dict[Coord, int], min_move: int, max_move: int) -> Dict:
    
    def find_next(loc: Coord, dir: int, total: int):
        r = []
        turn_d: Dict[int,List[Tuple[Coord, int]]] = {
            1 : [(loc.up(), 0), (loc.down(), 2)],
            2 : [(loc.right(), 1), (loc.left(), 3)],
            3 : [(loc.down(), 2), (loc.up(), 0)],
            0 : [(loc.left(), 3), (loc.right(), 1)]
        }
        str_d: Dict[int,Coord] = {
            1 : Coord(1,0),
            2 : Coord(0,1),
            3 : Coord(-1,0),
            0 : Coord(0,-1),
        }
        for x in turn_d[dir]:
            # give all possible moves turning from this spot
            next_loc, next_dir = x
            next_heat = 0
            for i in range(1, max_move + 1):
                if next_loc not in data:
                    continue
                next_heat += data[next_loc]
                if i >= min_move:
                    r.append((total + next_heat, next_loc, next_dir))
                next_loc += str_d[next_dir]

        return r

    target = list(data.keys())[-1]
    heap = find_next(Coord(0,0), 1, 0)
    for x in find_next(Coord(0,0), 2, 0):
        heapq.heappush(heap, x)
    seen = set()
    while heap:
        total, loc, d = heapq.heappop(heap)
        if (loc, d) in seen:
            continue
        seen.add((loc, d))
        if loc == target: #and streak >= min_move:
            return total
        for x in find_next(loc, d, total):
            heapq.heappush(heap, x)


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
    print(f"Part 1: {part1(DATA, 1, 3)}")
    print(f"Part 2: {part1(DATA, 4, 10)}") # not 1398, too high; 1320 also; 1310 also; 1286 is wrong
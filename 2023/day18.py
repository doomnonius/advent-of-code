from typing import List, Tuple, Set
from day10 import Coord

def part1(inst: List[Tuple[str,int,str]]) -> int:
    curr = Coord(10000,10000)
    edges: Set[Coord] = {curr}
    corners: Set[Coord] = {curr}
    move_d = {"U": Coord(0, -1), "D": Coord(0, 1), "R": Coord(1, 0), "L": Coord(-1, 0)}
    for i in inst:
        dir, dist = i[0], i[1]
        for j in range(dist):
            curr += move_d[dir]
            edges.add(curr)
        corners.add(curr)
    center = Coord(sum(z.x for z in corners)//len(corners), sum(z.y for z in corners)//len(corners))
    if center not in edges:
        edges.add(center)
    stack = [center]
    while stack:
        curr = stack.pop(0)
        for x in curr.neighbors():
            if x not in edges:
                edges.add(x)
                stack.append(x)
    return len(edges)

def part2(inst: List[Tuple[str,int,str]]) -> int:
    curr = Coord(0,0)
    dug = 0
    corners: Set[Coord] = {curr}
    # corners: List[Coord] = []
    # move_d = {"3": Coord(0, -1), "1": Coord(0, 1), "0": Coord(1, 0), "2": Coord(-1, 0)}
    # for i in inst:
    #     dir = i[2][-1]
    #     dist = int(i[2][1:-1], 16)
    #     curr += (move_d[dir] * dist)
    #     corners.add(curr)
    move_d = {"U": Coord(0, -1), "D": Coord(0, 1), "R": Coord(1, 0), "L": Coord(-1, 0)}
    for i in inst:
        dir, dist = i[0], i[1]
        curr += (move_d[dir] * dist)
        corners.add(curr)
    x_lines = {z.x:[a for a in corners if a.x == z.x] for z in corners}
    y_lines = {z.y:[a for a in corners if a.y == z.y] for z in corners}
    start = Coord(min(z.x for z in corners), min(z.y for z in corners))
    curr = start.x
    end = max(z.x for z in corners)+1
    # print(f"height: {max(z.y for z in corners) - min(z.y for z in corners)}")
    # print(corners)
    s = []
    while curr != end:
        if curr in x_lines.keys():
            s = sorted(x_lines[curr], key=lambda z: z.y)
        for i in range(0, len(s), 2):
            dug += abs(s[i+1].y - s[i].y) + 1
        print(f"after {curr}, total is {dug}")
        curr += 1
    return dug




if __name__ == "__main__":
    from datetime import datetime
    from pathlib import Path
    test = True
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    RAW_DATA = INPUT_FILE.read_text().strip().split("\n")
    DATA = []
    for line in RAW_DATA:
        dir, dist, color =  line.split()
        dist = int(dist)
        color = color[1:-1]
        DATA.append((dir, dist, color))
    print(f"Part 1: {part1(DATA)}")
    print(f"Part 2: {part2(DATA)}")
    # start = datetime.now()
    # x = 0
    # while x < 19559501:
    #     x += 1
    # print(f"that took {datetime.now()-start}")
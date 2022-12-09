from typing import List, Tuple, Set

def pull(lead: Tuple[int,int], follow: Tuple[int,int]) -> Tuple[int,int]: # just returns one tuple, new location of second knot
    # note: just need to check diff b/t x and y to find if too far away
    x_diff = lead[0] - follow[0]
    y_diff = lead[1] - follow[1]
    new_x = follow[0]
    new_y = follow[1]
    if abs(x_diff) > 1 and abs(y_diff) > 1:
        new_x = follow[0] + (x_diff//2)
        new_y = follow[1] + (y_diff//2)
        return (new_x, new_y)
    if abs(x_diff) > 1:
        new_x = follow[0] + (x_diff//2) # if two away on x then tail will always move one spot in x direction
        if lead[1] != follow[1]: new_y = lead[1] # if y not same will become same
    if abs(y_diff) > 1:
        new_y = follow[1] + (y_diff//2)
        if lead[0] != follow[0]: new_x = lead[0]
    return (new_x, new_y)

def part1(comms: List[Tuple[str, int]]) -> int:
    visited = set()
    h = t = (0,0)
    for c in comms:
        d, count = c
        while count:
            if d == "U":
                h = (h[0], h[1] + 1)
            if d == "D":
                h = (h[0], h[1] - 1)
            if d == "R":
                h = (h[0] + 1, h[1])
            if d == "L":
                h = (h[0] - 1, h[1])
            t = pull(h, t)
            visited.add(t)
            count -= 1
    return len(visited)

def part2(comms: List[Tuple[str, int]]) -> int:
    visited = set()
    knots = [(0,0)] * 10
    for c in comms:
        d, count = c
        while count:
            if d == "U":
                knots[0] = (knots[0][0], knots[0][1] + 1)
            if d == "D":
                knots[0] = (knots[0][0], knots[0][1] - 1)
            if d == "R":
                knots[0] = (knots[0][0] + 1, knots[0][1])
            if d == "L":
                knots[0] = (knots[0][0] - 1, knots[0][1])
            for k in range(len(knots)-1):
                new = pull(knots[k], knots[k+1])
                if new == knots[k+1]: break # presumably, if a knot doesn't move, the knots behind it won't move
                knots[k+1] = new
            visited.add(knots[-1])
            count -= 1
    if test:
        print(visited)
    return len(visited)




if __name__ == "__main__":
    import os, timeit
    from pathlib import Path
    test = False
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    DATA = INPUT_FILE.read_text().strip().split('\n')
    DATA = [x.split() for x in DATA]
    DATA = [(str(a), int(b)) for a,b in DATA]
    # print(DATA)
    print(f"Part 1: {part1(DATA)}")
    print(f"Part 2: {part2(DATA)}") # not 2553 or 2577, too low
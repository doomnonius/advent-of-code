from typing import Dict, List, Tuple
import itertools
from datetime import datetime

def hash_floors(floors: Dict) -> Tuple[str]:
    t = []
    for i in range(1,5):
        if floors["E"] == i:
            p = [1 for x in floors[i] if x[1] == "G"] + [2 for x in floors[i] if x[1] == "M"] + [3]
        else:
            p = [1 for x in floors[i] if x[1] == "G"] + [2 for x in floors[i] if x[1] == "M"]
        # I definitely need to know which floor the elevator is on
        t.append(tuple(sorted(p)))
    return tuple(t)

def check_valid(floors: Dict) -> bool:
    for i in range(1,5):
        p = floors[i] # present
        generators = {g for g in p if g[1] == "G"}
        if generators:
            for chip in (m for m in p if m[1] == "M"):
                if f"{chip[0]}G" not in generators:
                    return False
    return True

def check_ele(pair: List[str]) -> bool:
    if pair[0][1] != pair[1][1]:
        if pair[0][0] != pair[1][0]:
            return False
    return True

# establishing these outside of the functions so both functions can access them
heap = []
hist = set()


def move_elevator(floors:Dict,count:int,test:bool = False):
    """ This function doesn't return anything, it just adds to the heap that part1 is processing
    """
    f = floors["E"]
    ones = [[x] for x in floors[f]]
    pairs = [list(x) for x in itertools.combinations([x for x in floors[f]], 2)]
    for i in pairs:
        if check_ele(i):
            ones.append(i)
    for l in ones:
        new_floors = {k:frozenset(v) for k,v in floors.items() if type(k) != str}
        for i in l:
            new_floors[f] = new_floors[f] - {i}
        up = f+1
        down = f-1
        up_floor= {k:frozenset(v) for k,v in new_floors.items()}
        down_floor= {k:frozenset(v) for k,v in new_floors.items()}
        if up < 5 and len(l) > 1: # I'm pretty sure you always want to be moving up with two items, so let's try that
            up_floor["E"] = up
            for i in l:
                up_floor[up] = up_floor[up] | {i}
            if check_valid(up_floor):
                h = hash_floors(up_floor)
                if h not in hist:
                    heap.append((count, up_floor))
                    hist.add(h)
        if down > 0 and len(floors[1]): # no need to move down if floor 1 is empty
            down_floor["E"] = down
            for i in l:
                down_floor[down] = down_floor[down] | {i}
            if check_valid(down_floor):
                h = hash_floors(down_floor)
                if h not in hist:
                    heap.append((count, down_floor))
                    hist.add(h)
    

def part1(floors: Dict, steps:int = 0, test:bool = False) -> int:
    h_t = hash_floors(floors)
    hist.add(h_t)
    # first, build the next steps
    move_elevator(floors, 1)
    last = 0
    # check for solve
    while heap:
        popped = heap.pop(0)
        c_f = popped[1]
        if not c_f[1] and not c_f[2] and not c_f[3]:
            return popped[0]
        move_elevator(c_f, popped[0] + 1)
    return 9999


if __name__ == "__main__":
    DATA = """The first floor contains a polonium generator (1), a thulium generator (2), a thulium-compatible
    microchip (-2), a promethium generator (3), a ruthenium generator (4), a ruthenium-compatible microchip (-4), a cobalt 
    generator (5), and a cobalt-compatible microchip (-5).
The second floor contains a polonium-compatible microchip (-1) and a promethium-compatible microchip (-3).
The third floor contains nothing relevant.
The fourth floor contains nothing relevant."""
    """ repping the pairs as pos (gens) and neg (chips) nums; if a neg is on a floor w/o a corresponding
    positive, check for any other positive and throw error"""
    DATA = {1: {"1G", "2G", "2M", "3G", "4G", "4M", "5G", "5M"}, 2: {"1M", "3M"}, 3: set(), 4: set(), "E": 1}
    TEST_DATA = {"E": 1, 1: ["1M", "2M"], 2: ["1G"], 3: ["2G"], 4: []}
    start = datetime.now()
    print(f"Part one: {part1(DATA, test=False)}") # not 25 (tried to solve mentally, forgot you can't run the elevator without holding anything), 
    print(f"Solve time: {datetime.now()-start}")
    # next manually calc solution of 83 was also wrong; also not 53 or 52
    DATA[1].update(["6G", "6M", "7G", "7M"])
    hist = set()
    heap = []
    start = datetime.now()
    print(f"Part two: {part1(DATA, test=False)}") # getting 65 currently, which is wrong
    print(f"Solve time: {datetime.now()-start}")
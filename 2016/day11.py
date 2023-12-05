from typing import Dict, List, Tuple
import itertools

def hash_floors(floors: Dict) -> Tuple[str]:
    t = []
    for i in range(1,5):
        p = sorted(floors[i].copy())
        if floors["E"] == i:
            p.append("E")
        t.append(tuple(p))
    # print(tuple(t))
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
heap_length = []

def move_elevator(floors:Dict,count:int):
    """ This function doesn't return anything, it just adds to the heap that part1 is processing
    """
    # test every single possible move
    ones = [[x] for x in floors[floors["E"]]]
    pairs = [list(x) for x in itertools.combinations([x for x in floors[floors["E"]]], 2)]
    for i in pairs:
        if check_ele(i):
            ones.append(i)
    for l in ones:
        save = {"E":floors["E"],
                1: floors[1].copy(),
                2: floors[2].copy(),
                3: floors[3].copy(),
                4: floors[4].copy()
                }
        for i in l:
            floors[floors["E"]].remove(i)
        up = floors["E"]+1
        down = floors["E"]-1
        up_floor = {"E":up,
                    1: floors[1].copy(),
                    2: floors[2].copy(),
                    3: floors[3].copy(),
                    4: floors[4].copy()
                    }
        down_floor = {"E":down,
                    1: floors[1].copy(),
                    2: floors[2].copy(),
                    3: floors[3].copy(),
                    4: floors[4].copy()
                    }
        if up < 5 and len(l) > 1: # I'm pretty sure you always want to be moving up with two items, so let's try that
            up_floor["E"] = up
            for i in l:
                up_floor[up].add(i)
            #check valid here
            if check_valid(up_floor): # make hash above and check here
                h = hash_floors(up_floor)
                if h not in hist:
                    heap.append((count, up_floor))
                    hist.add(h)
                    # print(h)
        if down > 0 and len(floors[1]): # no need to move down if floor 1 is empty
            down_floor["E"] = down
            for i in l:
                down_floor[down].add(i)
            #check_valid here
            if check_valid(down_floor): # make hash above and check here
                h = hash_floors(down_floor)
                if h not in hist:
                    heap.append((count, down_floor))
                    hist.add(h)
                    # print(h)
        floors = save
    

def part1(floors: Dict, steps:int = 0, test:bool = False) -> int:
    """
    1) for each situation, discover all legal moves and branch (am I thinking toward a recursive solve? yeah...)
    2) but I also need previous states to be remembered, so repeated states mean fails
    based off of Peter's code, I think I have a good path forward:
    1) make a way to hash each setup, and save hashes to check for one we've seen before
        a) substep: convert to using sets instead of lists
    2) don't do recursive. Use a prioritized heap instead. (Peter used heapq but I think I can make my own solution)
    I think I can use most of my current code to make this happen
    """
    h_t = hash_floors(floors)
    hist.add(h_t)
    # hash test
    # h_t2 = hash_floors(floors)
    # if h_t == h_t2:
    #     # print ("Success! hashes match")
    #     print(h_t)
    # else:
    #     return 9900
    # first, build the next steps
    move_elevator(floors, 1)
    last = 0
    # check for solve
    while heap:
        popped = heap.pop(0)
        c_f = popped[1]
        if not c_f[1] and not c_f[2] and not c_f[3]:
            return popped[0]
        if popped[0] != last:
            last = popped[0]
            # print(f"floor: {last}; heap length: {len(heap)}")
            heap_length.append(len(heap))
        move_elevator(c_f, popped[0] + 1)
    return 9999


if __name__ == "__main__":
    import timeit
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
    print(f"Part one: {part1(DATA, test=False)}") # not 25 (tried to solve mentally, forgot you can't run the elevator without holding anything), 
    # next manually calc solution of 83 was also wrong; also not 53 or 52
    print(f"Max heap size: {max(heap_length)}; # of seen buildings: {len(hist)}")
    DATA[1].update(["6G", "6M", "7G", "7M"])
    hist = set()
    heap = []
    heap_length = []
    print(DATA)
    print(f"Part two: {part1(DATA, test=False)}") # getting 65 currently, which is wrong
    print(f"Max heap size: {max(heap_length)}; # of seen buildings: {len(hist)}")
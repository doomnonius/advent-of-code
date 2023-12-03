from typing import Dict, List
import itertools

def travel(floors: Dict, floor: int) -> int:
    # check = floors["E"].count
    # if (check > 2) or (check < 1):
    pass
        
def check_valid(floors: Dict, expected:int) -> bool:
    count = len(floors[4]) + len(floors[3]) + len(floors[2]) + len(floors[1])
    if count != expected:
        print(f"Error! Wrong number of items ({count})[12]!")
        return 9999
    for i in range(1,5):
        p = floors[i] # present
        generators = {g for g in p if g[1] == "G"}
        if generators:
            for chip in (m for m in p if m[1] == "M"):
                if f"{chip[0]}G" not in generators:
                    return False
    return True

def part1(floors: Dict, steps:int = 0, test:bool = False) -> int:
    """
    1) for each situation, discover all legal moves and branch (am I thinking toward a recursive solve? yeah...)
    2) but I also need previous states to be remembered, so repeated states mean fails
    based off of Peter's code, I think I have a good path forward:
    1) make a way to hash each setup, and save hashes to check for one we've seen before
    2) don't do recursive. Use a prioritized heap instead.
    I think I can use most of my current code to make this happen
    """
    # if test:
    #     if steps > 0: print("forked!")
    # check for solve
    if test: check = 4
    else: check = 10
    if len(floors[4]) == check and floors[1] == [] and floors[2] == [] and floors[3] == []:
        print(floors["inst"])
        return steps
    # check for creation of extra items
    count = len(floors[4]) + len(floors[3]) + len(floors[2]) + len(floors[1])
    if count != check:
        # print(f"Error! Wrong number of items ({count})[91]!")
        return 9999
    # rather than check a history, just check if steps > 75
    if steps > 50:
        return 9999
    # check if current conditions are legal; else, return 9999
    if not check_valid(floors, check):
        # if test: print("not valid!")
        return 9999
    """# check if the current layout exists in the history
    # first limit to every layout of the same size
    # make sure to check the value of E as well
    if floors in hist:
        return 9999"""
    # save current layout to history
    for i in range(1,5):
        floors[i].sort()
    # test every single possible move
    ones = [[x] for x in floors[floors["E"]]]
    pairs = [list(x) for x in itertools.combinations([x for x in floors[floors["E"]]], 2)]
    # if test: print(pairs)
    for i in pairs:
        ones.append(i)
    # if test: print(ones)
    possible = []
    for l in ones:
        # if test: print(f"l: {l}")
        save = {"E":floors["E"],
                "inst":floors["inst"],
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
                    "inst":floors["inst"],
                    1: floors[1].copy(),
                    2: floors[2].copy(),
                    3: floors[3].copy(),
                    4: floors[4].copy()
                    }
        down_floor = {"E":down,
                    "inst":floors["inst"],
                    1: floors[1].copy(),
                    2: floors[2].copy(),
                    3: floors[3].copy(),
                    4: floors[4].copy()
                    }
        # given that I have the instructions saved, I should be able to make a check to prevent \
        # undoing the move that just happened. Don't think this will really help my run times all that much though
        if up < 5:
            floors[up].append(i)
            up_floor["E"] = up
            for i in l:
                up_floor[up].append(i)
            #check valid here
            if check_valid(up_floor, check):
                possible.append(up_floor)
            up_floor["inst"] += f"{l} to {up}\n"
        if down > 0:
            down_floor["E"] = down
            for i in l:
                down_floor[down].append(i)
            #check_valid here
            if check_valid(down_floor, check):
                possible.append(down_floor)
            down_floor["inst"] += f"{l} to {down}\n"
        floors = save
    # if test: print(possible)
    return min(part1(x, steps+1, test) for x in possible)


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
    DATA = {1: ["1G", "2G", "2M", "3G", "4G", "4M", "5G", "5M"], 2: ["1M", "3M"], 3: [], 4: [], "E": 1, "inst":""}
    TEST_DATA = {"E": 1, 1: ["1M", "2M"], 2: ["1G"], 3: ["2G"], 4: [], "inst":""}
    print(f"Part one: {part1(DATA, test=False)}") # not 25 (tried to solve mentally, forgot you can't run the elevator without holding anything), 
    # next manually calc solution of 83 was also wrong; also not 53 or 52
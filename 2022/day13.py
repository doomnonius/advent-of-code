from typing import List, Dict

def part1(signals: Dict[int, List[List]]) -> int:
    retVal = 0
    for i,p in signals.items():
        if test: print(p)
        assert len(p) == 2
        if recurse(p[0], p[1], i):
            retVal += i
            print(f"{i} is valid")
        else:
            print(f"{i} is invalid")
    return retVal



def recurse(a, b, i) -> int:
    if test or i == 3: print(f"comparing {a} \nand\n {b}")
    if a and not b:
        return 0
    if not a and b:
        return 1
    if not a and not b:
        return 2
    while type(a[0]) != type(b[0]):
        if type(a[0]) == list:
            b[0] = [b[0]]
        else:
            a[0] = [a[0]]
    if type(a[0]) == int: # comparing ints
        if a[0] < b[0]:
            return 1
        elif a[0] > b[0]:
            return 0
        else:
            # if len(a) > 1 and len(b) > 1:
            a.pop(0)
            b.pop(0)
            return recurse(a, b, i)
            # else:
            #     return recurse(a[1:], b[1:], i)
    # don't need as else, but here is for lists
    if type(a[0]) == list:
        # if not a[0] and not b[0]:
        #     pass
        # else:
        # return recurse(a[0], b[0], i)
        
        # r = recurse(a[0], b[0], i)
        # if r == 1:
        #     return r
        # elif r == 0:
        #     return 0
        # else:
        #     return recurse(a[1:], b[1:], i)
        if a[0] and b[0]:
            return recurse(a[0], b[0], i)
        elif len(a) > 1 and len(b) > 1:
            return recurse(a[1:], b[1:], i)

        # if recurse(a[0], b[0], i) and len(a) > 1 and len(b) > 1:
        #     return recurse(a[1:], b[1:], i)
        # else:
        #     return recurse(a[0], b[0], i)
    return 1





def part2(nums: List[int]) -> int:
    return




if __name__ == "__main__":
    import os, timeit
    from pathlib import Path
    test = True
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    DATA = INPUT_FILE.read_text().strip().split('\n\n')
    PAIRS = {}
    index = 1
    for pair in DATA:
        a, b = pair.split('\n')
        exec(f"a, b = {a}, {b}")
        PAIRS[index] = [a,b]
        index += 1
    # print(PAIRS)
    print(f"Part 1: {part1(PAIRS)}") # not 4422, too low; nor 6418, too high
    print(f"Part 2: {part2(PAIRS)}")
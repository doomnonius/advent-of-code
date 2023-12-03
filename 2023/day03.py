from typing import Tuple, List
from string import digits

def process_data(raw_data:str) -> List[Tuple[int, str]]:
    """ the dictionary key will be the part number
        the dictionary value will be the adjacent symbols (full list)
    """
    data = raw_data.split("\n")
    # symbols = ""

    def neighbor_symbols(x:int, y:int) -> str:
        """ return all the non-digit, non-period symbols next to a spot.
            uses try for edge cases
        """
        s = ""
        # n
        try:
            c = data[y-1][x]
            if c not in digits+".":
                s += c
        except:
            pass
        # ne
        try:
            c = data[y-1][x+1]
            if c not in digits+".":
                s += c
        except:
            pass
        # e
        try:
            c = data[y][x+1]
            if c not in digits+".":
                s += c
        except:
            pass
        # se
        try:
            c = data[y+1][x+1]
            if c not in digits+".":
                s += c
        except:
            pass
        # s
        try:
            c = data[y+1][x]
            if c not in digits+".":
                s += c
        except:
            pass
        # sw
        try:
            c = data[y+1][x-1]
            if c not in digits+".":
                s += c
        except:
            pass
        # w
        try:
            c = data[y][x-1]
            if c not in digits+".":
                s += c
        except:
            pass
        # nw
        try:
            c = data[y-1][x-1]
            if c not in digits+".":
                s += c
        except:
            pass
        return s

    r = []
    x = y = 0
    while y < len(data):
        while x < len(data[y]):
            # record all symbols that appear, but why did I write this? I shouldn't need it
            # if data[y][x] not in digits+"."+symbols:
            #     symbols += data[y][x]
            #     x += 1
            #     continue
            # need to find full numbers and adjacent coords
            n = ""
            v = 0
            while x < len(data[y]) and data[y][x].isdigit():
                v *= 10
                v += int(data[y][x])
                n += neighbor_symbols(x, y)
                # print(f"number: {v}, symbols: {n}")
                # _ = input("pause to verify")
                # Warning! this will count symbols more than once (if adjacent to multiple numbers) NB for p2
                x += 1
            if v > 0:
                r.append((v,n))
            x += 1
        x = 0
        y += 1
    return r

def part1(data: List[Tuple[int, str]]) -> int:
    t = 0
    for i in data:
        # print(f"number: {i[0]}, symbols: {i[1]}")
        if len(i[1]) > 0:
            t += i[0]
    return t





def part2(nums: List[int]) -> int:
    return




if __name__ == "__main__":
    import os, timeit
    from pathlib import Path
    INPUT_FILE = Path(__file__).with_suffix(".input")
    DATA = INPUT_FILE.read_text().strip()
    DATA = process_data(DATA)
    print(f"Part 1: {part1(DATA)}") # 308893 too low; solution didn't account for a number showing up more than once
    print(f"Part 2: {part2(DATA)}")
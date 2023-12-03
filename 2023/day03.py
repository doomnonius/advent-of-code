from typing import Tuple, List, Dict
from string import digits

def process_data(raw_data:str) -> (List[Tuple[int, str]], Dict[str, List[int]]):
    """ the dictionary key will be the part number
        the dictionary value will be the adjacent symbols (full list)
    """
    data = raw_data.split("\n")
    # symbols = ""

    def neighbors(x:int, y:int) -> List[Tuple[int, int]]:
        """ return all the non-digit, non-period symbols next to a spot.
            uses try for edge cases
        """
        s = []
        # n
        try:
            if data[y-1][x] not in digits+".":
                s.append((y-1,x))
        except:
            pass
        # ne
        try:
            if data[y-1][x+1] not in digits+".":
                s.append((y-1,x+1))
        except:
            pass
        # e
        try:
            if data[y][x+1] not in digits+".":
                s.append((y,x+1))
        except:
            pass
        # se
        try:
            if data[y+1][x+1] not in digits+".":
                s.append((y+1,x+1))
        except:
            pass
        # s
        try:
            if data[y+1][x] not in digits+".":
                s.append((y+1,x))
        except:
            pass
        # sw
        try:
            if data[y+1][x-1] not in digits+".":
                s.append((y+1,x-1))
        except:
            pass
        # w
        try:
            if data[y][x-1] not in digits+".":
                s.append((y,x-1))
        except:
            pass
        # nw
        try:
            if data[y-1][x-1] not in digits+".":
                s.append((y-1,x-1))
        except:
            pass
        return s

    r = []
    # r2 can be a dict of * locs and a list of adj nums
    r2 = dict()
    x = y = 0
    while y < len(data):
        while x < len(data[y]):
            n = []
            v = 0
            while x < len(data[y]) and data[y][x].isdigit():
                v *= 10
                v += int(data[y][x])
                for i in neighbors(x, y):
                    if i not in n:
                        n.append(i)
                x += 1
            if v > 0:
                r.append((v,n))
                # here is where r2 comes in: check each item in neighbors, if * returned, add to list
                for i in n:
                    if data[i[0]][i[1]] == "*":
                        k = f"y{i[0]}x{i[1]}"
                        if k in r2.keys():
                            r2[k].append(v)
                        else:
                            r2[k] = [v]
            x += 1
        x = 0
        y += 1
    return r, r2

def part1(data: List[Tuple[int, str]]) -> int:
    t = 0
    for i in data:
        # print(f"number: {i[0]}, symbols: {i[1]}")
        if len(i[1]) > 0:
            t += i[0]
    return t


def part2(data: Dict[str, List[int]]) -> int:
    t = 0
    for k,v in data.items():
        if len(v) == 2:
            t += (v[0] * v[1])
    return t




if __name__ == "__main__":
    import os, timeit
    from pathlib import Path
    INPUT_FILE = Path(__file__).with_suffix(".input")
    DATA = INPUT_FILE.read_text().strip()
    DATA = process_data(DATA)
    print(f"Part 1: {part1(DATA[0])}") # 308893 too low; solution didn't account for a number showing up more than once
    print(f"Part 2: {part2(DATA[1])}")
from typing import List, Dict

def part1(nums) -> int:
    total = 0
    for x in nums:
        digs = x.split()
        for i in digs:
            if len(i) in [2,3,4,7]:
                total += 1
    return total

def decode(inp: str) -> dict:
    vals = inp.split()
    vals.sort(key=len) # order will be: 1, 7, 4, [5, 2, 3], [6, 0, 9], 8
    solved = {1: set(vals[0]), 7: set(vals[1]), 4: set(vals[2]), 8: set(vals[-1])}
    poss = {k:set(["a","b","c","d","e","f","g"]) for k in ["b","bl"]}
    # top bar will be diff between items 0 and 1
    poss["t"] = set(vals[1]) - set(vals[0])
    # top right and bottom right will be either of options for 1
    poss["tr"] = poss["br"] = set(vals[0])
    # middle and top left will be either of options leftover after that from 2
    poss["m"] = poss["tl"] = set(vals[2])
    for i in poss.keys():
        if poss[i] != poss["t"]: poss[i] = poss[i] - poss["t"]
    for i in poss.keys():
        if poss[i] != poss["tr"]: poss[i] = poss[i] - poss["tr"]
    for i in poss.keys():
        if poss[i] != poss["m"]: poss[i] = poss[i] - poss["m"]
    # 5 will contain t, tl's options, one of br's options - the one
    for x in vals[3:6]:
        s = set(x)
        if len((poss["t"] | poss["tl"]) & s) == 3:
            solved[5] = s
            poss["br"] = (s - (poss["t"] | poss["tl"])) & poss["br"]
            poss["tr"] = poss["tr"] - poss["br"]
            poss["b"] = (s - (poss["t"] | poss["tl"]) - poss["br"])
            poss["bl"] = poss["bl"] - poss["b"]
    for x in vals[3:6]: # just so we know everything else is found
        s = set(x)
        if len((poss["t"] | poss["bl"] | poss["tr"] | poss["b"]) & s) == 4:
            solved[2] = s
            poss["m"] = (s - (poss["t"] | poss["bl"] | poss["tr"] | poss["b"])) & poss["m"]
            poss["tl"] = poss["tl"] - poss["m"]
        if len((poss["t"] | poss["br"] | poss["tr"] | poss["b"]) & s) == 4:
            solved[3] = s
    for x in vals[6:9]:
        if list(poss["tr"])[0] not in x:
            solved[6] = set(x)
        if list(poss["bl"])[0] not in x:
            solved[9] = set(x)
        if list(poss["m"])[0] not in x:
            solved[0] = set(x)
    return solved

def part2(nums: dict[str:str]) -> int:
    retVal = 0
    for k,v in nums.items():
        temp = 0
        solved = decode(k)
        out = v.split()
        i = 0
        for x in out:
            for k,v in solved.items():
                if set(x) == v:
                    temp += (k * (10 ** abs(i - 3)))
                    i += 1
        retVal += temp
    return retVal

if __name__ == "__main__":
    import os, timeit
    from pathlib import Path
    INPUT_FILE = Path(__file__).with_suffix(".input")
    RAW_DATA = INPUT_FILE.read_text().strip().split('\n')
    DATA = {}
    for l in RAW_DATA:
        k, v = l.split(" | ")
        DATA[k] = v
    # print(DATA)
    print(f"Part 1: {part1(DATA.values())}")
    print(f"Part 2: {part2(DATA)}") # not 987295, too high
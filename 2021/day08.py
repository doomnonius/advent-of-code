from typing import List, Dict

def part1(nums) -> int:
    total = 0
    for x in nums:
        digs = x.split()
        for i in digs:
            if len(i) in [2,3,4,7]:
                total += 1
    return total

def decode(inp: str) -> int:
    vals = inp.split()
    vals.sort(key=len) # order will be: 1, 7, 4, [5, 2, 3], [6, 0, 9], 8
    print(vals)
    # top bar will be diff between items 0 and 1
    poss = {k:["a","b","c","d","e","f","g"] for k in ["tr","tl","m","b","bl","br"]}
    poss["t"] = list(set(vals[1]) - set(vals[0]))[0]
    for i in k.values():
        if poss["t"] in 



def part2(nums: dict[str:str]) -> int:
    for x in nums.keys():
        print(x)
        decode(x)
        return




if __name__ == "__main__":
    import os, timeit
    FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    file = os.path.splitext(__file__)[0][-5:]
    with open(os.path.join(FILE_DIR, file + ".input")) as f:
        RAW_DATA = f.read().strip().split('\n')
    DATA = {}
    for l in RAW_DATA:
        k, v = l.split(" | ")
        DATA[k] = v
    # print(DATA)
    print(f"Part 1: {part1(DATA.values())}")
    print(f"Part 2: {part2(DATA)}")
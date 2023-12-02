from typing import List, Dict

def part1(nums: Dict, r:int, g:int, b:int) -> int:
    t = 0
    for k, v in nums.items():
        if v["red"] <= r \
        and v["green"] <= g \
        and v["blue"] <= b:
            t += k
    return t

def part2(nums: Dict) -> int:
    t = 0
    for k, v in nums.items():
        t += (v["red"] * v["green"] * v["blue"])
    return t

if __name__ == "__main__":
    import os, timeit
    from pathlib import Path
    INPUT_FILE = Path(__file__).with_suffix(".input")
    RAW_DATA = INPUT_FILE.read_text().strip().split("\n")
    DATA = dict()
    for line in RAW_DATA:
        # print(line)
        g, d = line.split(":")
        g = int(g.split()[1])
        d = d.split(";")
        di = {"green":0,"red":0,"blue":0}
        for i in d:
            k = i.split(",")
            for j in k:
                n, c = j.split()
                n = int(n)
                if n > di[c]:
                    di[c] = n
        DATA[g] = di
    print(f"Part 1: {part1(DATA, 12, 13, 14)}")
    print(f"Part 2: {part2(DATA)}")
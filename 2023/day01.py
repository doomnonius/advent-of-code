from typing import List

def part1(nums: List[str], p2=False) -> int:
    total = 0
    num_dict = {
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9
    }
    for s in nums:
        t = o = 0
        for i in list(range(len(s))):
            try:
                if p2:
                    for k in num_dict.keys():
                        if k in s[0:i]:
                            t = num_dict[k] * 10
                            break
                if t > 0: break
                t = int(s[i]) * 10; break
            except: pass
        for i in list(range(len(s)))[::-1]:
            try:
                if p2:
                    for k in num_dict.keys():
                        if k in s[i:]:
                            o = num_dict[k]
                            break
                if o > 0: break
                o = int(s[i]); break
            except: pass
        # print(t+o)
        total += (t + o)
    return total

if __name__ == "__main__":
    import os, timeit
    from pathlib import Path
    test = False
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    DATA = INPUT_FILE.read_text().strip().split()
    # DATA = [x for x in DATA.split()] # example code
    print(DATA)
    print(f"Part 1: {part1(DATA)}")
    print(f"Part 2: {part1(DATA, True)}")
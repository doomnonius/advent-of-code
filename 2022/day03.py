from typing import List
from collections import Counter
import string

def part1(packs: List[str]) -> int:
    total = 0
    for pack in packs:
        # split into half
        comp1 = set(pack[0:len(pack)//2])
        comp2 = set(pack[len(pack)//2:])
        for i in comp1.intersection(comp2):
            total += string.ascii_letters.index(i) + 1
    return total


def part2(packs: List[str]) -> int:
    total = 0
    initial = 0
    while initial < len(packs):
        a = set(packs[initial])
        b = set(packs[initial + 1])
        c = set(packs[initial + 2])
        for i in a.intersection(b, c):
            total += string.ascii_letters.index(i) + 1
        initial += 3
    return total




if __name__ == "__main__":
    import os, timeit
    FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    file = os.path.splitext(__file__)[0][-5:]
    with open(os.path.join(FILE_DIR, file + ".input")) as f:
        DATA = f.read().strip()
    DATA = [x for x in DATA.split()] # example code
    # print(DATA)
    print(f"Part 1: {part1(DATA)}")
    print(f"Part 2: {part2(DATA)}")
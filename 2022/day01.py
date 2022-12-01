from typing import List

def part1(nums: List[List[str]]) -> int:
    e_max = 0
    for elf in nums:
        e_total = sum(int(x) for x in elf)
        if e_total > e_max:
            e_max = e_total
    return e_max

def part2(nums: List[List[str]]) -> int:
    e_max = [0,0,0]
    for elf in nums:
        e_total = sum(int(x) for x in elf)
        if e_total > min(e_max):
            e_max[e_max.index(min(e_max))] = e_total
    return sum(e_max)




if __name__ == "__main__":
    import os, timeit
    FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    file = os.path.splitext(__file__)[0][-5:]
    with open(os.path.join(FILE_DIR, file + ".input")) as f:
        DATA = f.read().strip()
    DATA = [x.split() for x in DATA.split("\n\n")] # example code
    # print(DATA)
    print(f"Part 1: {part1(DATA)}")
    print(f"Part 2: {part2(DATA)}")
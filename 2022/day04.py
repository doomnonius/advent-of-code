from typing import List

def part1(nums: List[int]) -> int:
    i = 0
    total = 0
    while i < len(nums):
        min_a, max_a, min_b, max_b = nums[i:i+4]
        if (min_a >= min_b) and (max_a <= max_b):
            total += 1
        elif (min_b >= min_a) and (max_b <= max_a):
            total += 1
        i += 4
    return total

def part2(nums: List[int]) -> int:
    i = 0
    total = 0
    while i < len(nums):
        min_a, max_a, min_b, max_b = nums[i:i+4]
        if (min_b <= min_a <= max_b) or (min_a <= min_b <= max_a):
            total += 1
        i += 4
    return total




if __name__ == "__main__":
    import os, timeit
    FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    file = os.path.splitext(__file__)[0][-5:]
    with open(os.path.join(FILE_DIR, file + ".input")) as f:
        DATA = f.read().strip().replace("-",",").replace("\n",",").split(",")
    DATA = [int(x) for x in DATA] # example code
    # print(DATA)
    print(f"Part 1: {part1(DATA)}") # not 302, too low
    print(f"Part 2: {part2(DATA)}")
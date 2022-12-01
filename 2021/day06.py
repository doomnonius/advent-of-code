from typing import List

def part1(nums: List[int], cycles: int) -> int: # horrifically inefficient, interacts with each member of list each time
    for x in range(cycles):
        new_nums = []
        for fish in nums:
            new_fish = fish - 1
            if new_fish < 0:
                new_nums.append(6)
                new_nums.append(8)
            else:
                new_nums.append(new_fish)
        nums = new_nums
    return len(nums)
        
def part2(nums: List[int], cycles: int) -> int:
    fish = {0:nums.count(0), 1:nums.count(1), 2:nums.count(2), 3:nums.count(3), 4:nums.count(4), 5:nums.count(5), 6:nums.count(6), 7:0, 8:0}
    for x in range(cycles):
        new_fish = {0:fish[1], 1:fish[2], 2:fish[3], 3:fish[4], 4:fish[5], 5:fish[6], 6:fish[7] + fish[0], 7:fish[8], 8:fish[0]}
        fish = new_fish # will I have problems with how dictionaries work?
    return sum(fish.values())
        
if __name__ == "__main__":
    import os, timeit
    FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    file = os.path.splitext(__file__)[0][-5:]
    with open(os.path.join(FILE_DIR, file + ".input")) as f:
        DATA = f.read().strip()
    DATA = [int(x) for x in DATA.split(",")] # example code
    print(DATA)
    print(f"Part 1: {part2(DATA, 80)}")
    print(f"Part 2: {part2(DATA, 256)}")
from typing import List

def part1(nums: List[int]) -> int:
    return





def part2(nums: List[int]) -> int:
    return




if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	file = os.path.splitext(__file__)[0][-5:]
	with open(os.path.join(FILE_DIR, file + ".input")) as f:
		DATA = f.read().strip()
	DATA = [int(x) for x in DATA.split()] # example code
	print(f"Part 1: {part1(DATA)}")
	print(f"Part 2: {part2(DATA)}")
    
from typing import List

def part1(nums: List[int]) -> int:
	retVal = 0
	y = nums[0]
	for x in nums:
		if x > y:
			retVal += 1
		y = x
	return retVal

def part2(nums: List[int]) -> int:
	retVal = 0
	y = sum(nums[0:3])
	for x in range(len(nums) - 2):
		r = sum(nums[x:x+3])
		if r > y:
			retVal += 1
		y = r
	return retVal


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	file = os.path.splitext(__file__)[0][-5:]
	with open(os.path.join(FILE_DIR, file + ".input")) as f:
		DATA = f.read().strip()
	DATA = [int(x) for x in DATA.split()]
	print(f"Part 1: {part1(DATA)}")
	print(f"Part 2: {part2(DATA)}")
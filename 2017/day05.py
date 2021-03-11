from typing import List

def part1(inp: List[int]) -> int:
	i = retVal = 0
	while i < len(inp):
		inp[i] += 1
		i += inp[i] - 1
		retVal += 1
	return retVal

def part2(inp: List[int]) -> int:
	i = retVal = 0
	while i < len(inp):
		if inp[i] >= 3:
			inp[i] -= 1
			i += inp[i] + 1
		else:
			inp[i] += 1
			i += inp[i] - 1
		retVal += 1
	return retVal

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day05.input")) as f:
		DATA = f.read().strip()
	DATA = [int(x) for x in DATA.split("\n")]
	# print(DATA)
	print(f"Part one: {part1(DATA.copy())}")
	print(f"Part two: {part2(DATA)}") # not 44729170, too high; 
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
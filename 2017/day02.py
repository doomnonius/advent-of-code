from typing import List
import itertools

def part1(inp: List[List[int]]) -> int:
	retVal = 0
	for row in inp:
		retVal += max(row) - min(row)
	return retVal

def part2(inp: List[List[int]]) -> int:
	retVal = 0
	for row in inp:
		for (x, y) in itertools.combinations(row, 2):
			if x % y == 0:
				retVal += x // y
			elif y % x == 0:
				retVal += y // x
	return retVal

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day02.input")) as f:
		DATA = f.read().strip()
	DATA = [x.split() for x in DATA.split("\n")]
	for y in range(len(DATA)):
		for x in range(len(DATA[y])):
			DATA[y][x] = int(DATA[y][x])
	# print(DATA)
	print(f"Part one: {part1(DATA)}")
	print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
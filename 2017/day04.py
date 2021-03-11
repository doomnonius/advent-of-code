from typing import List
import itertools


def part1(inp: List[List[str]]) -> int:
	retVal = 0
	for line in inp:
		valid = True
		for x, y in itertools.combinations(line, 2):
			if x == y:
				valid = False
				break
		retVal += valid
	return retVal

def part2(inp: List[List[str]]) -> int:
	retVal = 0
	for line in inp:
		valid = True
		for x, y in itertools.combinations(line, 2):
			if sorted(list(x)) == sorted(list(y)):
				valid = False
				break
		retVal += valid
	return retVal


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day04.input")) as f:
		DATA = f.read().strip()
	DATA = [x.split() for x in DATA.split("\n")]
	# print(DATA)
	print(f"Part one: {part1(DATA)}")
	print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
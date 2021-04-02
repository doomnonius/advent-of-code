import itertools
from typing import List
from math import prod


def part1(inp: List[str]) -> tuple:
	paper = 0
	ribbon = 0
	for line in inp:
		dims = [int(x) for x in line.split("x")]
		areas = [a[0] * a[1] for a in itertools.combinations(dims, 2)]
		perims = [a[0] + a[1] for a in itertools.combinations(dims, 2)]
		paper += sum(2*x for x in areas) + min(areas)
		ribbon += 2 * min(perims) + prod(dims)
	return paper, ribbon



if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day02.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	# DATA = ["2x3x4"]
	print(f"Part one: {part1(DATA)[0]}") # not 872898, too low; forgot there is two of each side
	print(f"Part two: {part1(DATA)[1]}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
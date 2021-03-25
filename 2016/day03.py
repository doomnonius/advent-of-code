from typing import List


def part1(inp: List[str]) -> int:
	retVal = 0
	for line in inp:
		ints = [int(x) for x in line.split()]
		l = len(ints)
		mx = ints.index(max(ints))
		if ints[mx] < ints[(mx+1)%l] + ints[(mx+2)%l]:
			retVal += 1
	return retVal


def part2(inp: List[str]) -> int:
	retVal = 0
	for i in range(len(inp)):
		inp[i] = [int(x) for x in inp[i].split()]
	for i in range(len(inp)//3):
		for j in range(3):
			ints = [inp[i*3][j], inp[(i*3)+1][j], inp[(i*3+2)][j]]
			l = len(ints)
			mx = ints.index(max(ints))
			if ints[mx] < ints[(mx+1)%l] + ints[(mx+2)%l]:
				retVal += 1
	return retVal


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day03.input")) as f:
		RAW_DATA = f.read().strip()
	DATA = RAW_DATA.split("\n")
	print(f"Part one: {part1(DATA)}")
	print(f"Part two: {part2(DATA)}") # not 1992, too high; used "+" in list instead of a comma
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
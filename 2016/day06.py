from typing import List


def part1(inp: List[str]) -> str:
	retVal = ''
	for x in range(len(inp[0])):
		count = {}
		for line in inp:
			if line[x] not in count:
				count[line[x]] = 0
			count[line[x]] += 1
		retVal += [x for x in count if count[x] == max(count.values())][0]
	return retVal


def part2(inp: List[str]) -> str:
	retVal = ''
	for x in range(len(inp[0])):
		count = {}
		for line in inp:
			if line[x] not in count:
				count[line[x]] = 0
			count[line[x]] += 1
		retVal += [x for x in count if count[x] == min(count.values())][0]
	return retVal


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day06.input")) as f:
		RAW_DATA = f.read().strip()
	DATA = RAW_DATA.split("\n")
	print(f"Part one: {part1(DATA)}")
	print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
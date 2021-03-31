


from typing import List


def part1(inp: List[str]) -> int:
	retVal = 0
	for pair in inp:
		low = int(pair[0])
		high = int(pair[1])
		if low <= retVal <= high:
			retVal = high + 1
	return retVal

def part2(inp: List[str]) -> int:
	c = 0
	retVal = 0
	index = 0
	while c <= 4294967295:
		curr_pair = [int(x) for x in inp[index]]
		low = curr_pair[0]
		high = curr_pair[1]
		while low <= c <= high:
			c = high + 1
		if high < c:
			index += 1
		if c < low:
			c += 1
			retVal += 1
	return retVal


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day20.input")) as f:
		DATA = f.read().strip()
	DATA = [x.split("-") for x in DATA.split("\n")]
	DATA.sort(key = lambda x: int(x[0]))
	# print(DATA)
	print(f"Part one: {part1(DATA)}") # not 12610189, too low; didn't convert to int before sort
	print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
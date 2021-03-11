from typing import List


def part1(inp: List[int]) -> int:
	retVal = 0
	former = []
	l = len(inp)
	while True:
		former.append(inp.copy())
		i = inp.index(max(inp))
		m = inp[i]
		inp[i] = 0
		while m > 0:
			i += 1
			inp[(i) % l] += 1
			m -= 1
		retVal += 1
		# print(inp)
		if inp in former:
			return retVal

def part2(inp: List[int]) -> int:
	retVal = 0
	former = []
	l = len(inp)
	while True:
		former.append(inp.copy())
		i = inp.index(max(inp))
		m = inp[i]
		inp[i] = 0
		while m > 0:
			i += 1
			inp[(i) % l] += 1
			m -= 1
		retVal += 1
		# print(inp)
		if inp in former:
			return retVal - former.index(inp)

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day06.input")) as f:
		DATA = f.read().strip()
	DATA = [int(x) for x in DATA.split()]
	# print(DATA)
	print(f"Part one: {part1(DATA.copy())}")
	print(f"Part two: {part2(DATA.copy())}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
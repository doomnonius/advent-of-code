import itertools, math
from typing import List


def part1(inp: List[int], sections: int) -> int:
	total = sum(inp)
	section = total // sections
	poss = set()
	li = len(inp)
	m = li
	for x in findSum(inp, section, 8):
		remaining = inp.copy()
		for z in x:
			remaining.remove(z)
		for y in findSum(remaining, section, 12):
			lx = sum(1 for _ in x)
			if lx < m:
				poss = {x}
				m = lx
			elif lx == m:
				poss.add(x)
			break
	return min(math.prod(x) for x in poss)


def findSum(inp: List[int], total: int, ma: int):
	li = len(inp)
	for i in range(li):
		for l in range(li//6, ma):
			for x in itertools.combinations(inp[i:], l):
				if sum(x) == total:
					yield x


TEST_DATA = """1
2
3
4
5
7
8
9
10
11"""


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day24.input")) as f:
		DATA = f.read().strip()
	DATA = [int(x) for x in DATA.split("\n")]
	print(f"Part one: {part1(DATA, 3)}") # not 364088754943, too high
	print(f"Part two: {part1(DATA, 4)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
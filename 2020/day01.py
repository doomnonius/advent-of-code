from typing import List


def part2(inp: List[int]) -> int:
	m = len(inp)
	x = 0
	while x < m:
		for y in inp:
			for z in inp:
				if y + inp[x] + z == 2020 and inp[x] != y and inp[x] != z and z != y:
					return inp[x] * y * z #1003971, 84035952
		x += 1


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day01.input")) as f:
		DATA = f.read().strip()
	DATA = [int(x) for x in DATA.split(",")]
	print(f"Part two: {part2(DATA)}")
	# print(f"Part two: {}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
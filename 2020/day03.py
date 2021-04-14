from typing import List


def toboggan(run: int, rise: int, inp: List[str]) -> int:
	x = y = 0
	h = len(inp)
	t = 0
	w = len(inp[0])

	while y < h:
		while x >= w:
			inp[y] += inp[y]
			w = len(inp[y])
		if inp[y][x] == "#": t += 1
		x += run
		y += rise
		w = len(inp[0])

	return t

def part1(inp: List[str]) -> int:
	return toboggan(3, 1, inp)


def part2(inp: List[str]) -> int:
	return toboggan(1, 1, inp)*toboggan(3, 1, inp)*toboggan(5, 1, inp)*toboggan(7, 1, inp)*toboggan(1, 2, inp)


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day03.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	print(f"Part one: {part1(DATA)}")
	print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
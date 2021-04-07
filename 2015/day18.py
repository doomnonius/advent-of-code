from day03 import Coord
from typing import Set


def part1(inp: Set[Coord], cycles: int, size: int, p2 = False) -> int:
	while cycles > 0:
		current = inp.copy()
		next_set = set()
		for point in current:
			c = 0
			for n in point.full_neighbors():
				c2 = 0
				if n in current:
					c += 1
				elif 0 <= n.x < size and 0 <= n.y < size:
					c2 = [p for p in n.full_neighbors() if p in current]
					if len(c2) == 3:
						next_set.add(n)
			if c in [2, 3]:
				next_set.add(point)
		cycles -= 1
		inp = next_set.copy()
		if p2:
			inp.update({Coord(0, 0), Coord(0, 99), Coord(99, 99), Coord(99, 0)})
	return len(inp)




TEST_DATA = """.#.#.#
...##.
#....#
..#...
#.#..#
####.."""


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day18.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	LIGHTS = {Coord(x, y) for y in range(len(DATA)) for x in range(len(DATA)) if DATA[x][y] == "#"}
	print(f"Part one: {part1(LIGHTS, 100, len(DATA))}") # not 9996, too high;
	LIGHTS = {Coord(x, y) for y in range(len(DATA)) for x in range(len(DATA)) if DATA[x][y] == "#"}
	LIGHTS.update({Coord(0, 0), Coord(0, 99), Coord(99, 99), Coord(99, 0)})
	print(f"Part two: {part1(LIGHTS, 100, len(DATA), True)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
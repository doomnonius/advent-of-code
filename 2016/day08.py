from day01 import Coord
from typing import List, Set


def part1(inp: List[str]) -> Set[Coord]:
	h = 6
	w = 50
	screen = set()
	for line in inp:
		split = line.split()
		if split[0] == "rect":
			size = [int(x) for x in split[1].split('x')]
			for y in range(size[1]):
				for x in range(size[0]):
					screen.add(Coord(x, y))
		else:
			if split[1] == "row":
				row = int(split[2].split('=')[1])
				remove = set()
				add = set()
				for pix in [x for x in screen if x.y == row]:
					remove.add(pix)
					add.add(Coord((pix.x + int(split[-1]))%w, pix.y))
				for r in remove:
					screen.remove(r)
				screen.update(add)
			else:
				col = int(split[2].split('=')[1])
				remove = set()
				add = set()
				for pix in [x for x in screen if x.x == col]:
					remove.add(pix)
					add.add(Coord(pix.x, (pix.y + int(split[-1]))%h))
				for r in remove:
					screen.remove(r)
				screen.update(add)
	return screen


def part2(inp: Set[Coord]) -> None:
	h = 6
	w = 50
	screen = []
	for y in range(h):
		next_row = [' '] * w
		screen.append(next_row)
	for pix in inp:
		screen[pix.y][pix.x] = '#'
	for row in screen:
		print(row)




if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day08.input")) as f:
		RAW_DATA = f.read().strip()
	DATA = RAW_DATA.split("\n")
	print(f"Part one: {len(part1(DATA))}")
	print("Part two:")
	part2(part1(DATA))
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
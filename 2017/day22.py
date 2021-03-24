from day03 import Coord
from typing import Set

def part1(inp: Set[Coord], cycles: int, mid: Coord) -> int:
	retVal = 0
	loc = mid
	direct = "u"
	turn_left = {"u": "l", "l": "d", "d": "r", "r": "u"}
	turn_right = {"u": "r", "r": "d", "d": "l", "l": "u"}
	move = {"u": Coord(0, -1), "d": Coord(0, 1), "l": Coord(-1, 0), "r": Coord(1, 0)}
	while cycles > 0:
		if loc in inp:
			direct = turn_right[direct]
			inp.remove(loc)
		else:
			direct = turn_left[direct]
			retVal += 1
			inp.add(loc)
		loc = loc + move[direct]
		cycles -= 1
	return retVal


def part2(inf: Set[Coord], cycles: int, mid: Coord) -> int:
	retVal = 0
	weak = set()
	flag = set()
	loc = mid
	direct = "u"
	turn_left = {"u": "l", "l": "d", "d": "r", "r": "u"}
	turn_right = {"u": "r", "r": "d", "d": "l", "l": "u"}
	reverse = {"u": "d", "d": "u", "l": "r", "r": "l"}
	move = {"u": Coord(0, -1), "d": Coord(0, 1), "l": Coord(-1, 0), "r": Coord(1, 0)}
	while cycles > 0:
		if loc in inf:
			direct = turn_right[direct]
			inf.remove(loc)
			flag.add(loc)
		elif loc in weak:
			weak.remove(loc)
			inf.add(loc)
			retVal += 1
		elif loc in flag:
			direct = reverse[direct]
			flag.remove(loc)
		else:
			direct = turn_left[direct]
			weak.add(loc)
		loc = loc + move[direct]
		cycles -= 1
	return retVal


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day22.input")) as f:
		RAW_DATA = f.read().strip()
	RAW_DATA = RAW_DATA.split('\n')
	DATA = set()
	for y in range(len(RAW_DATA)):
		for x in range(len(RAW_DATA[y])):
			if RAW_DATA[y][x] == "#":
				DATA.add(Coord(x, y))
	print(f"Part one: {part1(DATA.copy(), 10000, Coord(len(RAW_DATA[0])//2, len(RAW_DATA)//2))}")
	print(f"Part two: {part2(DATA.copy(), 10000000, Coord(len(RAW_DATA[0])//2, len(RAW_DATA)//2))}") # not 2535973, too high; had the counter in the wrong section
	# print(f"Time: {timeit.timeit('part1(DATA, 18)', setup='from __main__ import part1, DATA', number = 1)}")
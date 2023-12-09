from typing import Dict, List, Set, Tuple
from day01 import Coord
import string, itertools


def part1(walls: Set[Coord], points: Dict[str, Coord], p2:bool=False) -> int:
	""" finds the shortest route between each point, then finds the shortest path that visits each point
	"""
	def next_moves(loc: Coord, count: int, stack, history):
		""" doesn't return anything, just adds to the stack
		"""
		for n in loc.neighbors():
			if n not in walls and n not in history:
				stack.append((count + 1, n))
				history.add(n)

	def find_path(start: Coord, end: Coord, stack, history) -> int:
		next_moves(start, 0, stack, history)
		while True:
			count, loc = stack.pop(0)
			if loc == end:
				return count
			next_moves(loc, count, stack, history)

	paths = [x for x in itertools.permutations(range(len(points)), len(points)) if not x[0]]
	pairs = itertools.combinations(range(len(points)), 2) # this returns sorted
	distances = {k:find_path(points[k[0]], points[k[1]], [], set()) for k in pairs}

	r = 9999
	for p in paths:
		t = 0
		for i in range(len(p)-1):
			t += distances[tuple(sorted([p[i], p[i+1]]))]
		if p2:
			t += distances[(0,p[i+1])]
		if t < r: r = t
	return r

		


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day24.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	WALLS = set()
	POINTS = {}
	for row in range(len(DATA)):
		for column in range(len(DATA[row])):
			here = DATA[row][column] 
			if here == "#":
				WALLS.add(Coord(column, row))
			elif here in string.digits:
				POINTS[int(here)] = Coord(column, row)
	print(f"Part one: {part1(WALLS, POINTS)}") # not 426, too low; forgot that 0 needs to be starting point
	print(f"Part two: {part1(WALLS, POINTS, True)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
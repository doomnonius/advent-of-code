from day01 import Coord
from typing import List, Set, Tuple

visited: Set[Coord] = {Coord(1,1)}
stack: List[Tuple[int,Coord]] = []

def part1(key:int, target:Coord) -> int:
	start = Coord(1,1)
	find_walls(start, key, 0)
	while True:
		step_count, c = stack.pop(0)
		if c == target:
			return step_count
		find_walls(c, key, step_count)


def find_walls(c: Coord, key:int, steps:int):
	"""
	this won't return anything, just add new items to the list
	"""
	for n in c.neighbors():
		x,y = n.x,n.y
		form = (x**2) + (3*x) + (2*x*y) + y + (y**2) + key
		if not bin(form).count("1") % 2 and x >= 0 and y >= 0:
			if n in visited:
				continue
			visited.add(n)
			stack.append((steps+1,n))


def part2(key:int, steps:int):
	start = Coord(1,1)
	find_walls(start, key, 1)
	while True:
		step_count, c = stack.pop(0)
		if step_count > steps:
			return len(visited)
		find_walls(c, key, step_count)

if __name__ == "__main__":
	import timeit
	DATA = 1364
	# DATA = 10
	TARGET = Coord(31, 39)
	# TARGET = Coord(7, 4)
	print(f"Part one: {part1(DATA, TARGET)}") # not 324, too high; not 102, too high; not 84; not 88; 102-16 isn't 88
	visited: Set[Coord] = {Coord(1,1)}
	stack: List[Tuple[int,Coord]] = []
	print(f"Part two: {part2(DATA, 50)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
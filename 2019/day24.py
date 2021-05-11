from day10 import Coord
from typing import NamedTuple

class RecursiveCoord (NamedTuple):
	x: int
	y: int
	z: int

	def __eq__(self, other):
		if self.x == other.x and self.y == other.y and self.z == other.z:
			return True
		else:
			return False

	def __add__(self, other):
		return RecursiveCoord(self.x + other.x, self.y + other.y, self.z + other.z)

	def __repr__(self):
		return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

	def neighbors(self):
		retVal = [self + RecursiveCoord(0, 1, 0), self + RecursiveCoord(0, -1, 0), self + RecursiveCoord(1, 0, 0), self + RecursiveCoord(-1, 0, 0)]
		if self.y == 4: retVal[0] = RecursiveCoord(2, 3, self.z - 1)
		if self.y == 0: retVal[1] = RecursiveCoord(2, 1, self.z - 1)
		if self.x == 4: retVal[2] = RecursiveCoord(3, 2, self.z - 1)
		if self.x == 0: retVal[3] = RecursiveCoord(1, 2, self.z - 1)
		if self.y == 1 and self.x == 2: retVal.pop(0); retVal.extend([RecursiveCoord(x, 0, self.z + 1) for x in range(5)])
		if self.y == 3 and self.x == 2: retVal.pop(1); retVal.extend([RecursiveCoord(x, 4, self.z + 1) for x in range(5)])
		if self.y == 2 and self.x == 1: retVal.pop(2); retVal.extend([RecursiveCoord(0, y, self.z + 1) for y in range(5)])
		if self.y == 2 and self.x == 3: retVal.pop(3); retVal.extend([RecursiveCoord(4, y, self.z + 1) for y in range(5)])
		return retVal

def permutate(active, full):
	former = [active.copy()]
	while True:
		next_perm = active.copy()
		for point in full:
			n = sum(1 if x in active else 0 for x in point.neighbors())
			if point in active and n != 1:
				next_perm.remove(point)
			if point not in active and n in [1, 2]:
				next_perm.add(point)
		active = next_perm.copy()
		if active not in former:
			former.append(active.copy())
		else:
			return active
	
def calc_biodiversity(surface):
	retVal = 0
	for y in range(5):
		for x in range(5):
			if Coord(x, y) in surface:
				retVal += 2**(y + x + (4 * y))
	return retVal

def permutate2(active, loops):
	while loops > 0:
		next_perm = active.copy()
		for point in active:
			neighbors = point.neighbors()
			if sum(1 if x in active else 0 for x in neighbors) != 1:
				next_perm.remove(point)
			for n_point in neighbors:
				if n_point not in active and sum(1 if x in active else 0 for x in n_point.neighbors()) in [1, 2]:
					next_perm.add(n_point)
		active = next_perm.copy()
		loops -= 1
	return active

TEST_DATA = """....#
#..#.
#..##
..#..
#...."""

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day24.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	DATA_SET = set()
	FIELD = set()
	for y in range(len(DATA)):
		for x in range(len(DATA[0])):
			p = Coord(x, y)
			if DATA[y][x] == "#":
				DATA_SET.add(p)
			FIELD.add(p)
	TEST_DATA = TEST_DATA.split("\n")
	TEST_DATA_SET = set()
	for y in range(len(TEST_DATA)):
		for x in range(len(TEST_DATA[0])):
			p = Coord(x, y)
			if TEST_DATA[y][x] == "#":
				TEST_DATA_SET.add(p)
	print(f"Part one: {calc_biodiversity(permutate(DATA_SET, FIELD))}") # not 21532058, too low; used wrong data collection types
	print(f"Test two: {len(permutate2({RecursiveCoord(c.x, c.y, 0) for c in TEST_DATA_SET}, 10))}")
	print(f"Part two: {len(permutate2({RecursiveCoord(c.x, c.y, 0) for c in DATA_SET}, 200))}") # not 37888, too high; not 1922, too low [because I ran the test data set...]
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
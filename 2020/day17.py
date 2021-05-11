from typing import Dict, List, NamedTuple, Set
from itertools import combinations, product

## Don't need to make a whole plane, with empty spots 'n shit. Can do like I did in day 24.

class Coord3d(NamedTuple):
	x: int
	y: int
	z: int

	def neighbors(self):
		return {Coord3d(x[0], x[1], x[2]) for x in  product([-1, 0, 1], repeat=3) if x != (0, 0, 0)}
	
	def __add__(self, other):
		return Coord3d(self.x + other.x, self.y + other.y, self.z + other.z)
	
	def __repr__(self):
		return "(" + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ")"

class Coord4d(NamedTuple):
	x: int
	y: int
	z: int
	t: int

	def neighbors(self):
		return {Coord4d(x[0], x[1], x[2], x[3]) for x in  product([-1, 0, 1], repeat=4) if x != (0, 0, 0, 0)}
	
	def __add__(self, other):
		return Coord4d(self.x + other.x, self.y + other.y, self.z + other.z, self.t + other.t)
	
	def __repr__(self):
		return "(" + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ',' + str(self.t) + ")"

class Space:
	def __init__(self, initial_state: Set[Coord3d]):
		""" Note: 1 to 3 and -1 to -3 are mirrors.
		"""
		self.layout = initial_state

	def permutate(self):
		old_layout = self.layout.copy()
		for point in old_layout:
			n = {point+x for x in point.neighbors()}
			n_count = 0
			for pn in n:
				# count active neighbors
				if pn in old_layout:
					n_count += 1
				# check if any become active
				else:
					n2 = {pn + y for y in pn.neighbors()}
					n2_count = 0
					for pn2 in n2:
						if pn2 in old_layout:
							n2_count += 1
					if n2_count == 3:
						self.layout.add(pn)
			# check if any become inactive
			if n_count not in [2, 3]:
				self.layout.remove(point)
		return self

	
	def run(self, count):
		while count > 0:
			self.permutate()
			count -= 1
		return self

	def count(self):
		return len(self.layout)


TEST_DATA=""".#.
..#
###""" # should return 112 for p1, 848 for p2

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day17.input")) as f:
		DATA = f.read().strip()
	ROWS = DATA.split("\n")
	PLANE = set()
	PLANE2 = set()
	for row in range(len(ROWS)):
		for char in range(len(ROWS[row])):
			if ROWS[row][char] == "#":
				PLANE.add(Coord3d(row, char, 0))
	for row in range(len(ROWS)):
		for char in range(len(ROWS[row])):
			if ROWS[row][char] == "#":
				PLANE2.add(Coord4d(row, char, 0, 0))
	print(PLANE2)
	print(f"Part one: {Space(PLANE).run(6).count()}")
	print(f"Part two: {Space(PLANE2).run(6).count()}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
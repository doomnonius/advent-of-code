from typing import Dict, List, NamedTuple
from itertools import combinations

class Dimensions(NamedTuple):
	z: int
	y: int
	x: int


class Space:
	def __init__(self, initial_state):
		""" Note: 1 to 3 and -1 to -3 are mirrors.
		"""
		self.layout = initial_state
		self.dim = Dimensions(len(self.layout), len(self.layout[0]), len(self.layout[0][0]))

	def generate_layer(self):
		new_plane = []
		while len(new_plane) < self.dim.y:
			new_line = [0] * self.dim.x
			new_plane.append(new_line)
		self.layout[self.dim.z+1] = new_plane
		return self
	

	def extend_layer(self):
		# make sure it stays a square
		for key in self.layout.keys():
			for i in range(self.dim.y):
				self.layout[key][i] = [0] + self.layout[key][i]
				self.layout[key][i].append(0)
		self.dim.x += 2
		new_line = [0] * self.dim.x
		self.layout[key] = new_line + self.layout[key]
		self.layout[key].append(new_line)
		self.dim.y += 2
		return self


	def permutate(self, count = 0):
		for key in self.layout.keys():
			for coords in [c for c in combinations(range(self.dim.x), 2) if (0 in c or self.dim.x-1 in c)]:
				if self.layout[key][coords[0]][coords[1]] == 1:
					self.extend_layer()
					broken = True
					break
			if broken: break
		if sum(sum(L) for L in self.layout[len(self.layout)-1]) > 0:
			self.generate_layer()
		## This is where the main code body will be
		while count > 0:
			self.permutate()
			count -= 1
		return self

	
	def count_neighbors(self, coord: tuple):
		neighbors = 0
		return neighbors

	def count(self):
		c = 0
		for key in self.layout.keys():
			x = sum(sum(L) for L in self.layout[key])
			if key != 0: x *= 2
			c += x
		return c


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day\\.input")) as f:
		DATA = f.read().strip()
	ROWS = DATA.split("\n")
	PLANE = {0: [[],[],[],[],[],[],[],[]]}
	for i in len(ROWS):
		for char in ROWS[i]:
			if char == ".":
				PLANE[0][i].append(0)
			else:
				PLANE[0][i].append(1)
	print(f"Part one: {Space(PLANE).permutate(6).count()}")
	# print(f"Part two: {}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
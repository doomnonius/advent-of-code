from typing import Dict, List, NamedTuple
from itertools import combinations, product

class Space:
	def __init__(self, initial_state):
		""" Note: 1 to 3 and -1 to -3 are mirrors.
		"""
		self.layout = initial_state
		self.dim = {"z": len(self.layout), "y": len(self.layout[0]), "x": len(self.layout[0][0])}

	def generate_layer(self):
		new_plane = []
		while len(new_plane) < self.dim["y"]:
			new_line = [0] * self.dim["x"]
			new_plane.append(new_line)
		self.layout[self.dim["z"]] = new_plane
		self.dim["z"] += 1
		return self
	

	def extend_layer(self):
		self.dim["x"] += 2
		new_line = [0] * self.dim["x"]
		# print(f"y: {self.dim['y']}")
		for key in self.layout.keys():
			for i in range(self.dim["y"]):
				self.layout[key][i] = [0] + self.layout[key][i]
				self.layout[key][i].append(0)
			# print(f"e1: {self.layout}")
			self.layout[key] = [new_line] + self.layout[key]
			# print(f"e2: {self.layout}")
			self.layout[key].append(new_line)
		self.dim["y"] += 2
		return self


	def permutate(self):
		broken = False
		self.generate_layer()
		print("1: ", self.layout)
		for key in self.layout.keys():
			for coords in [c for c in combinations(range(self.dim["x"]), 2) if (0 in c or self.dim["x"]-1 in c)]:
				if self.layout[key][coords[0]][coords[1]] == 1:
					self.extend_layer() # this will always return a square
					broken = True
					break
			if broken: break
		if sum(sum(L) for L in self.layout[self.dim["z"]-2]) > 0:
			self.generate_layer()
		print("2: ", self.layout)
		## This is where the main code body will be
		next_state = self.layout.copy()
		for z in range(len(self.layout)-2):
			for y in range(1, len(self.layout[z])-1):
				for x in range(1, len(self.layout[z][y])-1):
					if self.layout[z][y][x] == 1 and self.count_neighbors((x, y, z)) not in [2, 3]:
						next_state[z][y][x] = 0
					elif self.layout[z][y][x] == 0 and self.count_neighbors((x, y, z)) == 3:
						next_state[z][y][x] = 1
		self.layout = next_state
		return self

	
	def run(self, count):
		while count > 0:
			self.permutate()
			count -= 1
		return self


	def count_neighbors(self, coord: tuple):
		neighbors = 0
		for x in product([-1, 0, 1], repeat=3):
			if x != (0, 0, 0):
				z = abs(coord[2] + x[2])
				# print(f"x,y,z: {coord[0]+x[0], coord[1]+x[1], z}")
				if self.layout[z][coord[1]+x[1]][coord[0]+x[0]] == 1:
					neighbors += 1
		return neighbors

	def count(self):
		c = 0
		for key in self.layout.keys():
			x = sum(sum(L) for L in self.layout[key])
			if key != 0: x *= 2
			c += x
		return c


TEST_DATA=""".#.
..#
###""" # should return 112

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day17.input")) as f:
		DATA = f.read().strip()
	ROWS = TEST_DATA.split("\n")
	PLANE = {0: []}
	for i in range(len(ROWS)):
		PLANE[0].append([])
		for char in ROWS[i]:
			if char == ".":
				PLANE[0][i].append(0)
			else:
				PLANE[0][i].append(1)
	print(PLANE)
	print(f"Part one: {Space(PLANE).run(6).count()}")
	# print(f"Part two: {}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
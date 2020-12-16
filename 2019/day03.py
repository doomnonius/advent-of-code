"""
Brainstorming:
- make a list of every coordinate each wire touches, based on the directional input
- compare the lists, find the common coordinates
- calculate the taxicab distance for each coordinate set (for points p1,q1 and p2,q2 = abs(p1-q1) + abs(p2-q2))
"""
from typing import List, Set

class Wire:
	def __init__(self, directions: List[str]):
		corners = []
		x = y = 0
		for d in directions:
			num = int(d[1:])
			if d[0] == "D":
				y -= num
				next_point = (y, x)
			elif d[0] == "U":
				y += num
				next_point = (y, x)
			elif d[0] == "R":
				x += num
				next_point = (y, x)
			elif d[0] == "L":
				x -= num
				next_point = (y, x)
			corners.append(next_point)
		self.corners = corners
		self.pairs = [(self.corners[x], self.corners[x+1]) for x in range(len(self.corners)-1)]

	def overlap(self, other) -> List[tuple]:
		cross = []
		# print(self.pairs[0])
		for coords_1 in self.pairs:
			for coords_2 in other.pairs:
				if coords_2[0][0] == coords_2[1][0] and coords_1[0][1] == coords_1[1][1]: # this means 2 is horizontal, 1 is vertical
					cross.append((coords_2[0][0], coords_1[0][1]))
				if coords_1[0][0] == coords_1[1][0] and coords_2[0][1] == coords_2[1][1]: # this means 1 is horizontal, 2 is vertical
					cross.append((coords_1[0][0], coords_2[0][1]))
		print(cross)
		return cross


def manhattan(point: tuple):
	""" Takes a list of cross points and calculates the taxicab distance for each.
	"""
	return abs(point[0]) + abs(point[1])

TEST_DATA = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day03.input")) as f:
		DATA = f.read().strip()
	WIRE1, WIRE2 = TEST_DATA.split("\n")
	WIRE1 = Wire(WIRE1.split(","))
	print(WIRE1.pairs)
	WIRE2 = Wire(WIRE2.split(","))
	print(WIRE2.pairs)
	print(f"Part one: {min(manhattan(x) for x in WIRE1.overlap(WIRE2))}")
	# print(f"Part two: {}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
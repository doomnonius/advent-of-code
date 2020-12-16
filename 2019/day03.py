from typing import List, Set

class Coord:
	def __init__(self, y, x):
		self.y = y
		self.x = x

	def __repr__(self):
		return f"{(self.y, self.x)}"

class Wire:
	def __init__(self, directions: List[str]):
		corners = [Coord(0,0)]
		x = y = 0
		for d in directions:
			num = int(d[1:])
			if d[0] == "D":
				y -= num
				next_point = Coord(y, x)
			elif d[0] == "U":
				y += num
				next_point = Coord(y, x)
			elif d[0] == "R":
				x += num
				next_point = Coord(y, x)
			elif d[0] == "L":
				x -= num
				next_point = Coord(y, x)
			corners.append(next_point)
		self.corners = corners
		self.pairs = [(self.corners[x], self.corners[x+1]) for x in range(len(self.corners)-1)]

	def overlap(self, other) -> List[tuple]:
		cross = []
		# print(self.pairs[0])
		for coords_1 in self.pairs:
			for coords_2 in other.pairs:
				if coords_2[0].y == coords_2[1].y and coords_1[0].x == coords_1[1].x and (coords_2[0].x < coords_1[0].x < coords_2[1].x or coords_2[0].x > coords_1[0].x > coords_2[1].x) and (coords_1[0].y < coords_2[0].y < coords_1[1].y or coords_1[0].y > coords_2[0].y > coords_1[1].y): # this means 2 is horizontal, 1 is vertical
					cross.append(Coord(coords_2[0].y, coords_1[0].x))
				if coords_1[0].y == coords_1[1].y and coords_2[0].x == coords_2[1].x and (coords_1[0].x < coords_2[0].x < coords_1[1].x or coords_1[0].x > coords_2[0].x > coords_1[1].x) and (coords_2[0].y < coords_1[0].y < coords_2[1].y or coords_2[0].y > coords_1[0].y > coords_2[1].y): # this means 1 is horizontal, 2 is vertical
					cross.append(Coord(coords_1[0].y, coords_2[0].x))
		return cross


def manhattan(point) -> int:
	""" Takes a list of cross points and calculates the taxicab distance for each.
	"""
	return abs(point.y) + abs(point.x)

def steps(point, wire1, wire2) -> int:
	count = 0
	i = 0
	j = 0
	while i < len(wire1.corners)-1:
		x1 = wire1.corners[i].x
		y1 = wire1.corners[i].y
		x2 = wire1.corners[i+1].x
		y2 = wire1.corners[i+1].y
		if (x1 < point.x < x2 or x1 > point.x > x2) and y1 == point.y:
			count += abs(point.x - x1)
			break
		elif (y1 < point.y < y2 or y1 > point.y > y2) and x1 == point.x:
			count += abs(point.y - y1)
			break
		else:
			count += abs(x2-x1) + abs(y2-y1)
		i += 1
	while j < len(wire2.corners)-1:
		x1 = wire2.corners[j].x
		y1 = wire2.corners[j].y
		x2 = wire2.corners[j+1].x
		y2 = wire2.corners[j+1].y
		if (x1 < point.x < x2 or x1 > point.x > x2) and y1 == point.y:
			count += abs(point.x - x1)
			break
		elif (y1 < point.y < y2 or y1 > point.y > y2) and x1 == point.x:
			count += abs(point.y - y1)
			break
		else:
			count += abs(x2-x1) + abs(y2-y1)
		j += 1
	return count

TEST_DATA = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day03.input")) as f:
		DATA = f.read().strip()
	WIRE1, WIRE2 = DATA.split("\n")
	WIRE1 = Wire(WIRE1.split(","))
	WIRE2 = Wire(WIRE2.split(","))
	print(f"Part one: {min(manhattan(x) for x in WIRE1.overlap(WIRE2))}")
	print(f"Part two: {min(steps(x, WIRE1, WIRE2) for x in WIRE1.overlap(WIRE2))}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
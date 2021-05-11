from typing import List


class Coord:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return f"{(self.y, self.x)}"

	def __add__(self, other):
		return Coord(self.x + other.x, self.y + other.y)

	def __mul__(self, other: int):
		return Coord(self.x * other, self.y * other)
	
	def full_neighbors(self):
		return [self + Coord(0, 1), self + Coord(0, -1), self + Coord(1, 0), self + Coord(-1, 0), self + Coord(1, 1), self + Coord(1, -1), self + Coord(-1, -1), self + Coord(-1, 1)]

	def neighbors(self):
		return [self + Coord(0, 1), self + Coord(0, -1), self + Coord(1, 0), self + Coord(-1, 0)]

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __hash__(self):
		return hash((self.x, self.y))


def part1(inp: List[str]) -> int:
	start = Coord(0, 0)
	facing = 0
	turn_left = {0:3, 3:2, 2:1, 1:0}
	turn_right = {0:1, 1:2, 2:3, 3:0}
	visited = {start}
	move = {0: Coord(0, -1), 2: Coord(0, 1), 3: Coord(-1, 0), 1: Coord(1, 0)}
	done = False
	for inst in inp:
		if inst[0] == "L":
			facing = turn_left[facing]
		elif inst[0] == "R":
			facing = turn_right[facing]
		count = int(inst[1:])
		while count > 0:
			start = start + move[facing]
			count -= 1
			if start in visited and not done:
				print(f"Part two: {abs(start.x) + abs(start.y)}") # not 283, too high; was only looking at points of turns
				done = True
			else:
				visited.add(start)
	return abs(start.x) + abs(start.y)


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day01.input")) as f:
		RAW_DATA = f.read().strip()
	DATA = RAW_DATA.split(", ")
	print(f"Part one: {part1(DATA)}")
	# print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
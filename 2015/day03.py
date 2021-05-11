


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


def part1(inp: str) -> int:
	loc = Coord(0, 0)
	visited = {loc}
	for char in inp:
		if char == "^":
			loc = loc + Coord(0, -1)
		elif char == "v":
			loc = loc + Coord(0, 1)
		elif char == "<":
			loc = loc + Coord(-1, 0)
		else:
			loc = loc + Coord(1, 0)
		visited.add(loc)
	return len(visited)


def part2(inp: str) -> int:
	loc = Coord(0, 0)
	loc2 = Coord(0, 0)
	visited = {loc}
	for char in inp[::2]:
		if char == "^":
			loc = loc + Coord(0, -1)
		elif char == "v":
			loc = loc + Coord(0, 1)
		elif char == "<":
			loc = loc + Coord(-1, 0)
		else:
			loc = loc + Coord(1, 0)
		visited.add(loc)
	for char in inp[1::2]:
		if char == "^":
			loc2 = loc2 + Coord(0, -1)
		elif char == "v":
			loc2 = loc2 + Coord(0, 1)
		elif char == "<":
			loc2 = loc2 + Coord(-1, 0)
		else:
			loc2 = loc2 + Coord(1, 0)
		visited.add(loc2)
	return len(visited)


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day03.input")) as f:
		DATA = f.read().strip()
	print(f"Part one: {part1(DATA)}")
	print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
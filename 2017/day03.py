class Coord:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return f"{(self.y, self.x)}"

	def __add__(self, other):
		return Coord(self.x + other.x, self.y + other.y)
	
	def full_neighbors(self):
		return [self + Coord(0, 1), self + Coord(0, -1), self + Coord(1, 0), self + Coord(-1, 0), self + Coord(1, 1), self + Coord(1, -1), self + Coord(-1, -1), self + Coord(-1, 1)]

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y


def manhattan(point: Coord) -> int:
	""" Takes a list of cross points and calculates the taxicab distance for each.
	"""
	return abs(point.y) + abs(point.x)


def part1(inp: int) -> int:
	x = 0
	square = 1
	total = 1
	while square**2 < inp:
		x += 1
		square += 2
		total = square**2
	m = square // 2
	y = m - 1
	total = (square - 2)**2 + 1
	if (inp - total) <= (y + m):
		y -= (inp - total)
		print(f"Coord: {Coord(x, y)}")
		return manhattan(Coord(x, y))
	else:
		total += y + m
		y = -m
	if (inp - total) <= (x + m):
		x -= (inp - total)
		print(f"Coord: {Coord(x, y)}")
		return manhattan(Coord(x, y))
	else:
		total += x + m
		x = -m
	if (inp - total) <= (abs(y) + m):
		y += (inp - total)
		print(f"Coord: {Coord(x, y)}")
		return manhattan(Coord(x, y))
	else:
		total += abs(y) + m
		y = m
	if (inp - total) <= (abs(x) + m):
		x += (inp - total)
		print(f"Coord: {Coord(x, y)}")
		return manhattan(Coord(x, y))
	else:
		print("Something has gone wrong here...")
		

def part2(inp: int) -> int:
	value = 1
	square = 1
	total = square**2
	index = 1
	x = y = 0
	side_length = 1
	side_progress = 1
	side = 0
	points = {(x, y): 1}
	while value < inp:
		## this part handles increasing x and y properly
		if index == total: # ie square is completed
			x += 1
			square += 2
			side_length = (square**2 - total)//4
			side_progress = 1
			side = 0
			total = square**2
			index += 1
		elif side_progress < side_length:
			side_progress += 1
			index += 1
			if side == 0:
				y -= 1
			if side == 1:
				x -= 1
			if side == 2:
				y += 1
			if side == 3:
				x += 1
		elif side_progress == side_length:
			if side == 3:
				x += 1
				index += 1
			else:
				side += 1
				side_progress = 0
				continue
		next_val = 0
		p = Coord(x, y)
		for n in p.full_neighbors():
			# print(n)
			if (n.x, n.y) in points.keys():
				next_val += points[(n.x, n.y)]
		points[(p.x, p.y)] = next_val
		value = next_val
		# print(value)
	return value


if __name__ == "__main__":
	import timeit
	DATA = 289326
	print(f"Part one: {part1(DATA)}")
	print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
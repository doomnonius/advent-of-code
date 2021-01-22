from itertools import permutations
from typing import List, Set, NamedTuple, Tuple

class Coord (NamedTuple):
	x: int
	y: int
	
	def __eq__(self, other):
		if self.x == other.x and self.y == other.y:
			return True
		else:
			return False

	def __add__(self, other):
		return Coord(self.x + other.x, self.y + other.y)

	def __repr__(self):
		return "(" + str(self.x) + ", " + str(self.y) + ")"

def count_asteroids(point: Coord, field: Set[Coord], size: Tuple, angles: List[Coord]) -> int:
	hits = set()
	for angle in angles:
		vec = angle + point
		while 0 <= vec[0] < max(size) and 0 <= vec[1] < max(size):
			if vec in field:
				hits.add(vec)
				break
			else:
				vec = vec + point
	print(f"point: {point}, hits: {hits}")
	return len(hits), point
	
	
def list_angles(size: Tuple):
	
	def key():
		return lambda z: z.y/z.x

	rng = range(-max(size)+1, max(size))
	angles = [Coord(0, -1)] + remove_dupes(sorted([Coord(x, y) for x, y in permutations(rng, 2) if x > 0 and y < 0], key = key())) + [Coord(1, 0)] + remove_dupes(sorted([Coord(x, y) for x, y in permutations(rng, 2) if x > 0 and y > 0], key = key())) + [Coord(0, 1)] + remove_dupes(sorted([Coord(x, y) for x, y in permutations(rng, 2) if x < 0 and y > 0], key = key())) + [Coord(-1, 0)] + remove_dupes(sorted([Coord(x, y) for x, y in permutations(rng, 2) if x < 0 and y < 0], key = key()))
	
	return(angles)

def remove_dupes(l: List[Coord]):
	i = 0
	while True:
		for c in l[i+1:]:
			# print(f"l[i]: {l[i].y/l[i].x}")
			if l[i].y/l[i].x == c.y/c.x:
				# print(f"c: {c.y/c.x}")
				l.remove(c)
		if i + 1 < len(l): i += 1
		else: break
	return l

def check_points(rows: List[List[int]], size: Tuple) -> int:
	y = x = 0
	m = (0, 0)
	asteroids = set()
	angles = list_angles(size)
	print(angles)
	for row in rows:
		for point in row:
			if point == 1:
				asteroids.add(Coord(x, y))
			x += 1
		y += 1
		x = 0
	print(len(asteroids))
	for ast in asteroids:
		count = count_asteroids(ast, asteroids, size, angles)
		if count[0] > m[0]:
			m = count
	return m



TEST_DATA = """.#..#
.....
#####
....#
...##"""

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day10.input")) as f:
		DATA = f.read().strip()
	FIELD = [[1 if char == "#" else 0 for char in row] for row in DATA.split("\n")]
	TEST_FIELD = [[1 if char == "#" else 0 for char in row ] for row in TEST_DATA.split("\n")]
	SIZE = (len(FIELD[0]), len(FIELD))
	TEST_SIZE = (len(TEST_FIELD[0]), len(TEST_FIELD))
	# print(list_angles(SIZE))
	count, point = check_points(TEST_FIELD, TEST_SIZE)
	print(f"Part one: {count}")
	# print(f"Part one: {check_points(FIELD, SIZE)[0]}") # not 281, too low
	# print(f"Part two: {}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
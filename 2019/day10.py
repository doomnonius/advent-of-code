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

	def reduce(self, max):
		x = self.x
		y = self.y
		while max > 1:
			if x % max == 0 and y % max == 0:
				x //= max
				y //= max
			max -= 1
		return Coord(x, y)


def count_asteroids(point: Coord, field: Set[Coord], size: Tuple, angles: List[Coord]) -> int:
	hits = []
	for angle in angles:
		vec = angle + point
		while 0 <= vec[0] < max(size) and 0 <= vec[1] < max(size):
			if vec in field:
				hits.append(vec)
				break
			else:
				vec = vec + angle
	return len(hits), point
	
def key():
	return lambda z: z.y/z.x
	
def list_angles(size: Tuple):
	rng = range(-max(size)+1, max(size))
	angles = [Coord(0, -1)] + remove_dupes(sorted([Coord(x, y) for x, y in permutations(rng, 2) if x > 0 and y < 0], key = key())) + [Coord(1, 0)] + remove_dupes(sorted([Coord(x, y) for x, y in permutations(rng, 2) if x > 0 and y > 0] + [Coord(1, 1)], key = key())) + [Coord(0, 1)] + remove_dupes(sorted([Coord(x, y) for x, y in permutations(rng, 2) if x < 0 and y > 0], key = key())) + [Coord(-1, 0)] + remove_dupes(sorted([Coord(x, y) for x, y in permutations(rng, 2) if x < 0 and y < 0] + [Coord(-1, -1)], key = key()))
	
	return(angles)

def remove_dupes(l: List[Coord]):
	i = 0
	red = False
	while True:
		for c in l[i+1:]:
			if l[i].y/l[i].x == c.y/c.x:
				l.remove(c)
				red = True
			if red:
				l[i] = l[i].reduce(max([abs(z.x) for z in l] + [abs(z.y) for z in l]))
				red = False
		if i + 1 < len(l): i += 1
		else: break
	return l

def check_points(rows: List[List[int]], size: Tuple) -> int:
	m = (0, 0)
	angles = list_angles(size)
	asteroids = convert_to_set(rows)
	for ast in asteroids:
		count = count_asteroids(ast, asteroids, size, angles)
		if count[0] > m[0]:
			m = count
	return m

def convert_to_set(rows: List[List[int]]):
	y = x = 0
	asteroids = set()
	for row in rows:
		for point in row:
			if point == 1:
				asteroids.add(Coord(x, y))
			x += 1
		y += 1
		x = 0
	return asteroids

def find_200(point: Coord, field: Set[Coord], size: Tuple):
	angles = list_angles(size)
	destroyed = 0
	retVal = 0
	last_field = 1000
	while True:
		i = 0
		while i < len(angles):
			check = point + angles[i]
			while 0 <= abs(check.x) <= max(size) and 0 <= abs(check.y) <= max(size):
				if check in field:
					field.remove(check)
					destroyed += 1
					if destroyed == 200:
						retVal = check.x*100 + check.y
					break
				else:
					check = check + angles[i]
			i += 1
		if len(field) < 50:
			last_field = len(field)
		if len(field) == last_field:
			return retVal


TEST_DATA = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day10.input")) as f:
		DATA = f.read().strip()
	FIELD = [[1 if char == "#" else 0 for char in row] for row in DATA.split("\n")]
	# TEST_FIELD = [[1 if char == "#" else 0 for char in row ] for row in TEST_DATA.split("\n")]
	SIZE = (len(FIELD[0]), len(FIELD))
	# TEST_SIZE = (len(TEST_FIELD[0]), len(TEST_FIELD))
	# t_count, t_point = check_points(TEST_FIELD, TEST_SIZE)
	# print(f"Part one: {t_count}")
	# print(t_point)
	count, point = check_points(FIELD, SIZE)
	print(f"Part one: {count}") # not 281, too low
	print(f"Time: {timeit.timeit('check_points(FIELD, SIZE)', setup='from __main__ import check_points, FIELD, SIZE', number = 1)}")
	# print(f"Part two: {find_200(t_point, convert_to_set(TEST_FIELD), TEST_SIZE)}")
	print(f"Part two: {find_200(point, convert_to_set(FIELD), SIZE)}") # not 703, too high; 
	print(f"Time: {timeit.timeit('find_200(point, convert_to_set(FIELD), SIZE)', setup='from __main__ import find_200, point, convert_to_set, FIELD, SIZE', number = 1)}")
from typing import NamedTuple

class Coord (NamedTuple):
	x: int
	y: int

	def neighbors(self):
		ne = Coord(self.x, self.y+1)
		nw = Coord(self.x-1, self.y+1)
		w = Coord(self.x-1, self.y)
		se = Coord(self.x+1, self.y-1)
		sw = Coord(self.x, self.y-1)
		e = Coord(self.x+1, self.y)
		return {ne, nw, w, sw, se, e}


def calculate_coord(line):
	i = 0
	x = 0
	y = 0
	n = s = False
	while i < len(line):
		if line[i] == "n":
			y += 1
			i += 1
			n = True
		elif line[i] == "s":
			y -= 1
			i += 1
			s = True
		if line[i] == "w" and not s:
			x -= 1
		elif line[i] == "e" and not n:
			x += 1
		n = s = False
		i += 1
	return Coord(x,y)

def find_coords(data):
	hits = set()
	for line in data:
		point = calculate_coord(line)
		if point in hits:
			hits.remove(point)
		else:
			hits.add(point)
	return hits

def check_n(layout, point, black=True):
	c = 0
	for p in point.neighbors():
		if p in layout:
			c += 1
	return c

def permutate(layout, count):
	while count > 0:
		old_layout = layout.copy()
		for point in old_layout:
			n = point.neighbors()
			if len([p for p in point.neighbors() if p in old_layout]) not in [1, 2]:
				layout.remove(point)
			for p in n:
				if p not in layout and len([x for x in p.neighbors() if x in old_layout]) == 2:
					layout.add(p)
		count -= 1
	return layout

TEST_DATA = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day24.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	print(f"Part one: {len(find_coords(DATA))}") # not 343, too low
	print(f"Part two: {len(permutate(find_coords(DATA), 100))}")
	print(f"Time: {timeit.timeit('len(permutate(find_coords(DATA), 100))', setup='from __main__ import permutate, find_coords, DATA', number = 1)}")
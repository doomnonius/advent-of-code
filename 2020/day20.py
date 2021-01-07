import math, itertools
from typing import List

class Image:
	def __init__(self, data):
		self.lines = data.split("\n")
		self.id = int(self.lines[0].split(" ")[1][0:4])
		self.top = self.lines[1]
		self.top_count = self.top.count("#")
		self.bottom = self.lines[10]
		self.bottom_count = self.bottom.count("#")
		self.left = "".join([x[0] for x in self.lines[1:11]])
		self.left_count = self.left.count("#")
		self.right = "".join([x[9] for x in self.lines[1:11]])
		self.right_count = self.right.count("#")
		self.data = []
		self.orientation = {"rotations":0, "flipped": False}

	def rotate_edges(self, turns=1):
		while turns > 0:
			save, save_count = self.top, self.top_count
			self.top, self.top_count = self.right, self.right_count
			self.right, self.right_count = self.bottom[::-1], self.bottom_count
			self.bottom, self.bottom_count = self.left, self.left_count
			self.left, self.left_count = save[::-1], save_count
			turns -= 1
			self.orientation["rotations"] = (self.orientation["rotations"] + 1) % 4
		return(self)

	def flip(self):
		self.top = self.top[::-1]
		self.right = self.right[::-1]
		self.bottom = self.bottom[::-1]
		self.left = self.left[::-1]
		self.orientation["flipped"] = not self.orientation["flipped"]
		return self

	def __repr__(self):
		# return f"Top: {self.top}\nBottom: {self.bottom}\nLeft: {self.left}\nRight: {self.right}"
		return str(self.id)

	def __eq__(self, other):
		if self.id == other.id:
			return True
		else:
			return False
		

class Board:
	def __init__(self, images: List, size: int):
		self.images = images
		self.size = size
		self.outline = []
		dim_1 = dim_2 = 0
		while dim_1 < size:
			self.outline.append([])
			while dim_2 < size:
				self.outline[dim_1].append([])
				dim_2 += 1
			dim_2 = 0
			dim_1 += 1

	def assemble(self):
		"""
		This function will figure out how to put together the pieces.
		Start by comparing each image to each other image.
		"""
		self.potentials = {}
		for a, b in itertools.permutations(self.images, 2):
			rotation_a = 0
			while rotation_a < 8:
				rotation_b = 0
				while rotation_b < 8:
					if a.right_count == b.left_count:
						if a.right == b.left:
							if a.id not in self.potentials.keys():
								self.potentials[a.id] = []
							# potentials[a.id].append(((a.orientation["rotations"], a.orientation["flipped"]), b.id, (b.orientation["rotations"], b.orientation["flipped"])))
							if b.id not in self.potentials[a.id]:
								self.potentials[a.id].append(b.id)
					b.rotate_edges()
					rotation_b += 1
					if rotation_b % 4 == 0:
						b.flip()
				a.rotate_edges()
				rotation_a += 1
				if rotation_a % 4 == 0:
					a.flip()
		# print(self.potentials)
		# I can't visualize how to solve this one
		
		

monster_pattern = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
		
print(monster_pattern)

TEST_DATA = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day20.input")) as f:
		DATA = f.read().strip()
	IMAGES = [Image(x) for x in DATA.split("\n\n")]
	SQUARE_SIZE = int(math.sqrt(len(IMAGES)))
	BOARD = Board(IMAGES, SQUARE_SIZE)
	# print(IMAGES[0])
	# IMAGES[0].rotate_edges() # this is working
	# print(IMAGES[0])
	BOARD.assemble()
	print(BOARD.outline)
	ans = [x.id for x in IMAGES if len(BOARD.potentials[x.id]) == 2]
	print(ans)
	print(f"Part one: {math.prod(ans)}")
	# print(f"Part two: {}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
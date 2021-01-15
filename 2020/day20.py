import math, itertools
from typing import List, Tuple, Set

import numpy as np

CAM_PRINT = {
	True: "#",
	False: ".",
}

np.set_printoptions(linewidth=500, formatter={"bool": lambda x: CAM_PRINT[x]})


class Image:
	def __init__(self, data):
		self.lines = data.split("\n")
		self.id = int(self.lines[0].split(" ")[1][0:4])
		lit_pixels = [[c == "#" for c in line] for y, line in enumerate(self.lines[1:])]
		self.full_pixels = np.array(lit_pixels, dtype=np.bool)
		print(self.full_pixels)
		self.define_edges()
		self.edge_hashes = {self.left, self.right, self.top, self.bottom, self.left[::-1], self.right[::-1], self.top[::-1], self.bottom[::-1]}
		assert len(self.edge_hashes) == 8, "Edge hashes should have 8 members."
		self.orientation = {"rotations":0, "flipped": False}
		self.right_n = None
		self.left_n = None
		self.down_n = None
		self.up_n = None
		self._lock = False
	
	def define_edges(self):
		self.top = tuple(self.full_pixels[0])
		self.bottom = tuple(self.full_pixels[9])
		self.left = tuple(([x[0] for x in self.full_pixels[0:10]]))
		self.right = tuple(([x[9] for x in self.lines[0:10]]))

	def _rotate_90(self):
		if not self._lock:
			self.full_pixels = np.rot90(self.full_pixels)
		self.define_edges()

	def _flip_vertical(self):
		if not self._lock:
			self.full_pixels = np.flipud(self.full_pixels)
		self.define_edges()

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

	def right(self, image: Image) -> Image:
		pot_n = self.potentials[image.id]
		assert len(pot_n) <= 2, "Length should be 2 or less"
		for i in pot_n:
			for img in self.images:
				if img.id == i:
					i_img = img
					break
			while rot_a < 8:
				while rot_b < 8:
					if image.right == i_img.left:
						image._lock = True
						i_img._lock = True
						break
					i_img._rotate_90()
					rot_b += 1
					if rot_b % 4 == 0:
						i_img._flip_vertical()
				image._rotate_90()
				rot_a += 1
				if rot_a % 4 == 0:
					image._flip_vertical
		return i

	def down(self, image: Image) -> Image:
		pot_n = self.potentials[image.id]
		assert len(pot_n) == 1, "Length should be 1"
		for i in self.potentials[image.id]:
			pass
		return i
	
	def rotate_board(self):
		pass

	def assemble(self):
		"""
		This function will figure out how to put together the pieces.
		Start by comparing each image to each other image.
		"""
		self.potentials = {}
		for a, b in itertools.permutations(self.images, 2):
			for edge in a.edge_hashes:
				if edge in b.edge_hashes:
					if a.id not in self.potentials.keys():
						self.potentials[a.id] = []
					if b.id not in self.potentials[a.id]:
						self.potentials[a.id].append(b.id)
					if b.id not in self.potentials.keys():
						self.potentials[b.id] = []
					if a.id not in self.potentials[b.id]:
						self.potentials[b.id].append(a.id)
		# I can't visualize how to solve this one atm
		# From Peter's solution:
		# 	- use np, it has good built-ins
		#	- only worry about moving right and down
		#	- I have a lot of the pieces already, just need to put them together properly
		for k in self.potentials.keys():
			for i in self.images:
				if i.id == k:
					k_image = i
					break
			row = 0
			column = 0
			if len(self.potentials[k]) == 2:
				while column < self.size:
					first_image_in_row = k_image
					while row < self.size:
						k_image.right_n = self.right(k_image)
						k_image.right_n.left_n = k_image
						k_image = k_image.right_n
						row += 1
					row = 0
					k_image = first_image_in_row
					k_image.down_n = self.down(k_image)
					k_image.down_n.up_n = k_image
					k_image = k_image.down_n
					column += 1

	def find_monsters(self):
		MONSTER = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
		print(MONSTER)

		
		

# test result should be 273

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day20.testinput")) as f:
		DATA = f.read().strip()
	IMAGES = [Image(x) for x in DATA.split("\n\n")]
	SQUARE_SIZE = int(math.sqrt(len(IMAGES)))
	BOARD = Board(IMAGES, SQUARE_SIZE)
	BOARD.assemble()
	ans = [x.id for x in IMAGES if len(BOARD.potentials[x.id]) == 2]
	print(ans)
	print(f"Part one: {math.prod(ans)}")
	print(BOARD.potentials)
	BOARD.find_monsters()
	# print(f"Part two: {}") 
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
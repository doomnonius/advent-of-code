import math
from typing import List, Tuple, Set, Optional

import numpy as np

CAM_PRINT = {
	True: "#",
	False: ".",
}

np.set_printoptions(linewidth=500, formatter={"bool": lambda x: CAM_PRINT[x]})

MONSTER_STR = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""

DIRECTIONS = {
	"up": lambda x, rev=False: (0, slice(None, None, -1 if rev else None)),
	"down": lambda x, rev=False: (x, slice(None, None, -1 if rev else None)),
	"left": lambda x, rev=False: (slice(None, None, -1 if rev else None)),
	"right": lambda x, rev=False: (slice(None, None, -1 if rev else None))
}

REV_DIRS = {
	"up": "down",
	"down": "up",
	"left": "right",
	"right": "left"
}

class Camera:
	id: int
	full_pixels: np.ndarray
	last_row: int
	edge_hashes: Set[Tuple[bool, ...]]
	edge_neighbors: List["Camera"]

	def __init__(self, raw_input: str):
		camid, *lines = raw_input.split("\n")
		self.id = int(camid[5:-1])
		lit_pixels = [[c =="#" for c in line] for y, line in enumerate(lines)]
		self.full_pixels = np.array(lit_pixels, dtype=np.bool)
		leny, lenx = self.full_pixels.shape
		last = lenx - 1
		assert lenx == leny, "We should only have squares"
		self.last_row = last
		self.edge_hashes = [tuple(self.full_pixels[d(last, rev=b)]) for d in DIRECTIONS.values() for b in (True, False)]
		self.edge_neighbor = []

	def edge_dir_hash(self, direction: str):
		return tuple(self.full_pixels[DIRECTIONS[direction](self.last_row)])

	@property
	def right_cam(self) -> Optional["Camera"]:
		right_hash = self.edge_dir_hash("right")
		try:
			return next(n for n in self.edge_neighbors if right_hash in n.edge_hashes)
		except StopIteration:
			return None

	@property
	def down_cam(self) -> Optional["Camera"]:
		down_hash = self.edge_dir_hash("down")
		try:
			return next(n for n in self.edge_neighbors if down_hash in n.edge_hashes)
		except StopIteration:
			return None
	
	@property
	def actual_pixels(self) -> np.ndarray:
		return self.full_pixels[1 : self.last_row, 1 : self.last_row]

	def fill_out_neighbors(self, other_cameras: List["Camera"]):
		self.edge_neighbors = [cam for cam in other_cameras if cam.id != self.id and cam.edge_hashes & self.edge_hashes]
		
	def _rotate_90(self):
		self.full_pixels = np.rot90(self.full_pixels)
		
	def _flip_vertical(self):
		self.full_pixels = np.flipud(self.full_pixels)

	def _all_rotations(self):
		for _ in range(4):
			yield
			self._rotate_90()
		self._flip_vertical()
		for _ in range(4):
			yield
			self._rotate_90()
	
	def corner_rotate_to_be_top_left(self):
		assert len(self.edge_neighbors) == 2, "I'm only a corner if I have exactly two neighbors"
		neighbor_hashes = self.edge_neighbors[0].edge_hashes | self.edge_neighbors[1].edge_hashes
		while not (self.edge_dir_hash("right") in neighbor_hashes and self.edge_dir_hash("down") in neighbor_hashes):
			self._rotate_90()

	def rotate_me_to_match_edge(self, coming_from_dir: str, from_cam: "Camera"):
		from_edge = from_cam.edge_dir_hash(REV_DIRS[coming_from_dir])
		rotate_iterator = self._all_rotations()
		while self.edge_dir_hash(coming_from_dir) != from_edge:
			next(rotate_iterator)

	def __repr__(self):
		return f"Camera({self.id}, {[n.id for n in self.edge_neighbors]})"


def multiply_corner_ids(cameras: List[Camera]) -> int:
	corner_cams = [cam for cam in cameras if len(cam.edge_neighbors) == 2]
	assert len(corner_cams) == 4, "Should only be 4 corners"
	return math.prod(cam.id for cam in corner_cams)

def build_grid(cameras: List[Camera]) -> np.ndarray:
	a_corner = next(cam for cam in cameras if len(cam.edge_neighbors) == 2)
	a_corner.corner_rotate_to_be_top_left()
	row_start = a_corner
	full_grid = None
	while True: # Should return out once done with last row
		tile_ids = f"{row_start.id}"
		row = row_start.actual_pixels
		cur_cam = row_start
		while True: # Should break out once we hit end-of-row
			next_cam = cur_cam.right_cam
			if not next_cam:
				break
			tile_ids += f" | {next_cam.id}"
			next_cam.rotate_me_to_match_edge("left", cur_cam)
			row = np.concatenate((row, next_cam.actual_pixels), axis=1)
			cur_cam = next_cam
		full_grid = np.concatenate((full_grid, row), axis=0) if full_grid is not None else row
		down_cam = row_start.down_cam
		if not down_cam:
			return full_grid
		down_cam.rotate_me_to_match_edge("up", row_start)
		row_start = down_cam

def build_monster(blob: str) -> np.ndarray:
	lit_pixels = [[c == "#" for c in line] for y, line in enumerate(blob.strip("\n").split("\n"))]
	return np.array(lit_pixels, dtype=np.bool)

def count_monsters_in_grid(grid: np.ndarray, monster: np.ndarray) -> int:
	gridy, gridx = grid.shape
	mony, monx = monster.shape
	count = 0
	for y in range(gridy - mony + 1):
		for x in range(gridx-monx + 1):
			if np.array_equal(grid[y : y + mony, x : x + monx] & monster, monster):
				count += 1
	return count

def count_monsters_in_grid_any_rotation(grid: np.ndarray, monster: np.ndarray) -> int:
	def _rotations(old_grid: np.ndarray) -> np.ndarray:
		for i in range(4):
			yield np.flipud(np.rot90(old_grid, k=i))
			yield np.rot90(old_grid, k=i)

		for rotated_grid in _rotations(grid):
			mon_count = count_monsters_in_grid(rotated_grid, monster)
			if mon_count != 0:
				return mon_count

# test result should be 273

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day20.input")) as f:
		DATA = f.read().strip()
	CAMERAS = [Camera(x) for x in DATA.split("\n\n")]
	__run_fill = [cam.fill_out_neighbors(CAMERAS) for cam in CAMERAS]
	print(f"Part one: {multiply_corner_ids(CAMERAS)}")
	CAMERA_GRID = build_grid(CAMERAS)
	MONSTER = build_monster(MONSTER_STR)
	NUM_MONSTERS = count_monsters_in_grid_any_rotation(CAMERA_GRID, MONSTER)
	print(f"Part two: {np.count_nonzero(CAMERA_GRID) - np.count_nonzero(MONSTER) * NUM_MONSTERS}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")


	# SQUARE_SIZE = int(math.sqrt(len(IMAGES)))
	# BOARD = Board(IMAGES, SQUARE_SIZE)
	# BOARD.assemble()
	# ans = [x.id for x in IMAGES if len(BOARD.potentials[x.id]) == 2]
	# print(ans)


	# class Image:
# 	def __init__(self, data):
# 		self.lines = data.split("\n")
# 		self.id = int(self.lines[0].split(" ")[1][0:4])
# 		lit_pixels = [[c == "#" for c in line] for y, line in enumerate(self.lines[1:])]
# 		self.full_pixels = np.array(lit_pixels, dtype=np.bool)
# 		print(self.full_pixels)
# 		self.define_edges()
# 		self.edge_hashes = {self.left, self.right, self.top, self.bottom, self.left[::-1], self.right[::-1], self.top[::-1], self.bottom[::-1]}
# 		assert len(self.edge_hashes) == 8, "Edge hashes should have 8 members."
# 		self.orientation = {"rotations":0, "flipped": False}
# 		self.right_n = None
# 		self.left_n = None
# 		self.down_n = None
# 		self.up_n = None
# 		self._lock = False
	
# 	def define_edges(self):
# 		self.top = tuple(self.full_pixels[0])
# 		self.bottom = tuple(self.full_pixels[9])
# 		self.left = tuple(([x[0] for x in self.full_pixels[0:10]]))
# 		self.right = tuple(([x[9] for x in self.lines[0:10]]))

# 	def _rotate_90(self):
# 		if not self._lock:
# 			self.full_pixels = np.rot90(self.full_pixels)
# 		self.define_edges()

# 	def _flip_vertical(self):
# 		if not self._lock:
# 			self.full_pixels = np.flipud(self.full_pixels)
# 		self.define_edges()

# 	def __repr__(self):
# 		# return f"Top: {self.top}\nBottom: {self.bottom}\nLeft: {self.left}\nRight: {self.right}"
# 		return str(self.id)

# 	def __eq__(self, other):
# 		if self.id == other.id:
# 			return True
# 		else:
# 			return False
		

# class Board:
# 	def __init__(self, images: List, size: int):
# 		self.images = images
# 		self.size = size

# 	def right(self, image: Image) -> Image:
# 		pot_n = self.potentials[image.id]
# 		assert len(pot_n) <= 2, "Length should be 2 or less"
# 		for i in pot_n:
# 			for img in self.images:
# 				if img.id == i:
# 					i_img = img
# 					break
# 			while rot_a < 8:
# 				while rot_b < 8:
# 					if image.right == i_img.left:
# 						image._lock = True
# 						i_img._lock = True
# 						break
# 					i_img._rotate_90()
# 					rot_b += 1
# 					if rot_b % 4 == 0:
# 						i_img._flip_vertical()
# 				image._rotate_90()
# 				rot_a += 1
# 				if rot_a % 4 == 0:
# 					image._flip_vertical
# 		return i

# 	def down(self, image: Image) -> Image:
# 		pot_n = self.potentials[image.id]
# 		assert len(pot_n) == 1, "Length should be 1"
# 		for i in self.potentials[image.id]:
# 			pass
# 		return i
	
# 	def rotate_board(self):
# 		pass

# 	def assemble(self):
# 		"""
# 		This function will figure out how to put together the pieces.
# 		Start by comparing each image to each other image.
# 		"""
# 		self.potentials = {}
# 		for a, b in itertools.permutations(self.images, 2):
# 			for edge in a.edge_hashes:
# 				if edge in b.edge_hashes:
# 					if a.id not in self.potentials.keys():
# 						self.potentials[a.id] = []
# 					if b.id not in self.potentials[a.id]:
# 						self.potentials[a.id].append(b.id)
# 					if b.id not in self.potentials.keys():
# 						self.potentials[b.id] = []
# 					if a.id not in self.potentials[b.id]:
# 						self.potentials[b.id].append(a.id)
# 		# I can't visualize how to solve this one atm
# 		# From Peter's solution:
# 		# 	- use np, it has good built-ins
# 		#	- only worry about moving right and down
# 		#	- I have a lot of the pieces already, just need to put them together properly
# 		for k in self.potentials.keys():
# 			for i in self.images:
# 				if i.id == k:
# 					k_image = i
# 					break
# 			row = 0
# 			column = 0
# 			if len(self.potentials[k]) == 2:
# 				while column < self.size:
# 					first_image_in_row = k_image
# 					while row < self.size:
# 						k_image.right_n = self.right(k_image)
# 						k_image.right_n.left_n = k_image
# 						k_image = k_image.right_n
# 						row += 1
# 					row = 0
# 					k_image = first_image_in_row
# 					k_image.down_n = self.down(k_image)
# 					k_image.down_n.up_n = k_image
# 					k_image = k_image.down_n
# 					column += 1


# 	def find_monsters(self):
# 		MONSTER = """                  # 
# #    ##    ##    ###
#  #  #  #  #  #  #   """
# 		print(MONSTER)
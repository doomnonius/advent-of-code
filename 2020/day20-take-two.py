import math
from typing import List, Set, Tuple

MONSTER_STR = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """


class Image:
	def __init__(self, data: str) -> None:
		split = data.split('\n')
		self.id = int(split[0].split()[1][:-1])
		self.pic = []
		for row in split[1:]:
			self.pic.append(tuple([1 if x == "#" else 0 for x in row]))
		self.edge_hashes = self.calc_edge_hashes()
		self.edge_neighbors = set()
	

	def calc_edge_hashes(self) -> List[tuple]:
		retVal = {"T": tuple(self.pic[0]), "B": tuple(self.pic[-1]), "L": tuple([x[0] for x in self.pic]), "R": tuple([x[-1] for x in self.pic])}
		retVal.update({"F"+x:y[::-1] for x, y in retVal.items()})
		return retVal
	
	
	def fill_out_neighbors(self, other_cameras: List["Image"]) -> None:
		self.edge_neighbors = {cam for cam in other_cameras if cam.id != self.id and cam.overlap(self)}

	
	def overlap(self, other: "Image") -> bool:
		for x in self.edge_hashes.values():
			if x in other.edge_hashes.values():
				return True
		return False

	
	def shared_side(self, stable: "Image", debug: bool = False) -> str:
		for k,v in self.edge_hashes.items():
			for e in stable.edge_hashes.values():
				if v == e:
					return k
	
	
	def shared_sides_to_top_left(self, others: List["Image"]) -> Tuple[str, str]:
		retVal = []
		for k,v in self.edge_hashes.items():
			for other in others:
				for k1,v1 in other.edge_hashes.items():
					if v == v1:
						retVal.append(k)
						if len(retVal) == len(others):
							return retVal
		return retVal


	def rotate_to_top_left(self) -> None:
		for _ in self._all_rotations():
			to_match = self.shared_sides_to_top_left(self.edge_neighbors)
			if to_match == ['B', 'R'] or to_match == ['R', 'B']:
				return


	def _rotate_90(self) -> None:
		self.pic = list(zip(*self.pic[::-1]))
		self.edge_hashes = self.calc_edge_hashes()
		

	def _flip_vertical(self) -> None:
		self.pic = [x[::-1] for x in self.pic]
		self.edge_hashes = self.calc_edge_hashes()


	def _flip_horizontal(self) -> None:
		self._rotate_90()
		self._rotate_90()
		self._flip_vertical()



	def _all_rotations(self):
		for _ in range(4):
			yield
			self._rotate_90()
		self._flip_vertical()
		for _ in range(4):
			yield
			self._rotate_90()
		self._flip_vertical()


	def __repr__(self):
		return f"Camera({self.id}, {[n.id for n in self.edge_neighbors]})"


def part1(inp: List[Image]) -> int:
	return math.prod(x.id for x in inp if len(x.edge_neighbors) == 2)


def build_grid(images: List[Image]) -> List[List[int]]:
	a_corner = next(img for img in images if len(img.edge_neighbors) == 2)
	a_corner.rotate_to_top_left()
	row_start = a_corner
	row_head = row_start
	grid = [[a_corner]]
	row = 0
	while row < int(math.sqrt(len(images))):
		found = False
		for n in row_head.edge_neighbors:
			if row_head.shared_side(n) == 'R':
				for _ in n._all_rotations():
					if n.shared_side(row_head) == 'L':
						if n.edge_hashes["L"] != row_head.edge_hashes['R']:
							n._flip_horizontal()
						assert n.edge_hashes["L"] == row_head.edge_hashes['R'], "Needs mirroring!"
						row_head = n
						grid[row].append(n)
						break
				found = True
				break
		if not found:
			row += 1
			for n in row_start.edge_neighbors:
				if row_start.shared_side(n) == 'B':
					for _ in n._all_rotations():
						shared = n.shared_side(row_start)
						if shared == 'T': # not flipping as needed
							if n.pic[0] != row_start.pic[-1]:
								n._flip_vertical()
							assert n.pic[0] == row_start.pic[-1], "Needs mirroring!"
							row_start = n
							row_head = row_start
							grid.append([n])
							break
					break
	true_grid = []
	for row in grid:
		for i in range(1,9):
			new_row = []
			for img in row:
				new_row += list(img.pic[i])[1:-1]
			true_grid.append(new_row.copy())
	return true_grid


def find_monster(grid: List[List[str]]) -> int:
	found = 0
	m_split = [tuple([1 if x == "#" else 0 for x in y]) for y in MONSTER_STR.split('\n')[1:]]
	len_mon = len(m_split[0])
	h_mon = len(m_split)
	m_oct_count = sum(sum(r) for r in m_split)
	row = col = 0
	while row < len(grid) - h_mon:
		while col < len(grid[row]) - len_mon:
			section = [line[col:col+len_mon] for line in grid[row:row+h_mon]]
			if sum(sum(r) for r in section) < m_oct_count:
				...
			else:
				invalid = False
				for i in range(len(section)):
					for j in range(len(section[i])):
						if m_split[i][j] and not section[i][j]:
							invalid = True
							break
					if invalid: break
				if not invalid:
					found += 1
					col += len_mon - 1
			col += 1
		row += 1
		col = 0
	return found * m_oct_count

	
def part2(inp: List[Image]) -> int:
	grid = build_grid(inp)
	oct_count = sum(sum(r) for r in grid)
	count = find_monster(grid)
	while not count:
		grid = list(zip(*grid[::-1]))
		count = find_monster(grid)
	return oct_count - count



if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day20.input")) as f:
		DATA = f.read().strip()
	DATA = [Image(x) for x in DATA.split("\n\n")]
	for x in DATA:
		x.fill_out_neighbors(DATA)
	print(f"Part one: {part1(DATA)}")
	print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
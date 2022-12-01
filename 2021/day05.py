from typing import NamedTuple, List

class Coord (NamedTuple):
	x: int
	y: int

	def __add__(self, other):
		return Coord(self.x + other.x, self.y + other.y)
	
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y
	
	def __hash__(self):
		return hash((self.x, self.y))
	
	def ortho(self, other):
		if self.x == other.x:
			return "v"
		elif self.y == other.y:
			return "h"
		else:
			return False

	def left(self, other):
		if self.x < other.x:
			return self
		else:
			return other


def part1(inp: List[Coord], test: bool, diag: bool = False) -> int:
	coords = set()
	doubled = set()
	for pair in range(len(inp)//2):
		c1, c2 = inp[pair*2], inp[pair*2+1]
		if test: print(c1, c2)
		dire = c1.ortho(c2)
		if not dire:
			if test: print("not orthogonal, continuing")
			if diag:
				# note for continuation: I need to know the direction of the diagonal
				# find which has lower x, then choose to go up or down
				leftmost = c1.left(c2)
				l = leftmost.x
				y = leftmost.y
				maxx = max(c1.x, c2.x)
				for c in range(maxx - minx + 1):
					new_c = Coord(l + c, miny + c)
					if test: print(new_c)
					if new_c not in coords:
						coords.add(new_c)
					else:
						doubled.add(new_c)
			continue
		else:
			if dire == "v":
				maxy = max(c1.y, c2.y)
				miny = min(c1.y, c2.y)
				for c in range(maxy - miny + 1):
					new_c = Coord(c1.x, miny + c)
					if test: print(new_c)
					if new_c not in coords:
						coords.add(new_c)
					else:
						doubled.add(new_c)
			elif dire == "h":
				maxx = max(c1.x, c2.x)
				minx = min(c1.x, c2.x)
				for c in range(maxx - minx + 1):
					new_c = Coord(minx + c, c1.y)
					if test: print(new_c)
					if new_c not in coords:
						coords.add(new_c)
					else:
						doubled.add(new_c)
	if test: print(coords)
	if test: print(doubled)
	return len(doubled)






if __name__ == "__main__":
	import os, timeit
	test = True
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	file = os.path.splitext(__file__)[0][-5:]
	if test:
		with open(os.path.join(FILE_DIR, file + ".testinput")) as f:
			DATA = f.read().strip()
	else:
		with open(os.path.join(FILE_DIR, file + ".input")) as f:
			DATA = f.read().strip()
	DATA = [Coord(int(x[0]), int(x[1])) for x in [y.split(",") for y in DATA.replace(" -> ", '\n').split("\n")]]
	if test: print(DATA)
	print(f"Part 1: {part1(DATA, test)}")
	print(f"Part 2: {part1(DATA, test, True)}")
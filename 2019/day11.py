from day02 import Computer
from typing import List, Set, NamedTuple

class Coord (NamedTuple):
	x: int
	y: int

	def __add__(self, other):
		return Coord(self.x + other.x, self.y + other.y)

class Robot (Computer):
	def __init__(self, instructions):
		super().__init__(instructions)
		self.white = set()
		self.painted = set()
		self.location = Coord(0, 0)
		self.o = 0
		self.o_list = [Coord(0, 1), Coord(1, 0), Coord(0, -1), Coord(-1, 0)]

	def output(self, data):
		self.out = data
		# print("Hello")
		return self

	def move(self, dir: int) -> Coord:
		if dir == 0:
			self.o = (self.o+3)%4
		elif dir == 1:
			self.o = (self.o+1)%4
		else:
			print("move() received faulty direction data")
		self.location = self.location + self.o_list[self.o]

	def input(self) -> int:
		if self.location in self.white:
			return 1
		else:
			return 0
		

def count_paint(robot: Robot):
	status = robot.run_codes()
	o = 0
	while not robot.done:
		if status == 0 and o % 2 == 0:
			o += 1
			if robot.location in robot.white:
				robot.white.remove(robot.location)
			robot.painted.add(robot.location)
		elif status == 1 and o % 2 == 0:
			o += 1
			robot.white.add(robot.location)
			robot.painted.add(robot.location)
		elif o % 2 == 1:
			robot.move(status)
			o += 1
		else:
			print("we shouldn't be here")
		status = robot.run_codes()
	return len(robot.painted)

def paint(inst: List[int]):
	robot = Robot(DATA)
	robot.white = {Coord(0, 0)}
	count_paint(robot)
	min_x = min(z.x for z in robot.white)
	min_y = min(z.y for z in robot.white)
	max_x = max(z.x for z in robot.white)
	max_y = max(z.y for z in robot.white)
	h = max_y - min_y + 1
	w = max_x - min_x + 1
	reg = []
	while h > 0:
		row = []
		reg.append(row)
		while w > 0:
			row.append(" ")
			w -= 1
		h -= 1
		w = max_x - min_x + 3
	for coord in robot.white:
		x = coord.x + abs(min_x) - 2
		y = coord.y + abs(min_y)
		reg[y][x] = "X"
	reg = reg[::-1]
	for row in reg:
		for char in row:
			print(char, end='')
		print()
	


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day11.input")) as f:
		DATA = f.read().strip()
	DATA = [int(x) for x in DATA.split(",")]
	robot = Robot(DATA)
	print(f"Part one: {count_paint(robot)}") # not 249, too low
	print(f"Part two: {paint(DATA)}") # not EPALUFAH; returned the answer upside down (but not backwards) - now fixed
	print(f"Time: {timeit.timeit('paint(DATA)', setup='from __main__ import paint, DATA', number = 1)}")
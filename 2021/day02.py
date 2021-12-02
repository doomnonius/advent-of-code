from typing import NamedTuple, List

class Coord (NamedTuple):
	x: int
	y: int

	def __add__(self, other):
		return Coord(self.x + other.x, self.y + other.y)


class Coord3 (NamedTuple):
	x: int
	y: int
	z: int

	def __add__(self, other):
		return Coord3(self.x + other.x, self.y + other.y, self.z + other.z)


def part1(insts: List[List[str]]) -> int:
	start = Coord(0, 0)
	for inst in insts:
		command, num = inst
		if command == "down":
			start = start + Coord(0, int(num))
		elif command == "up":
			start = start + Coord(0, -int(num))
		elif command == "forward":
			start = start + Coord(int(num), 0)
		else:
			print(f"Invalid command: {command}")
	return start.x * start.y


def part2(insts: List[List[str]]) -> int:
	start = Coord3(0, 0, 0)
	for inst in insts:
		command, num = inst
		if command == "down":
			start = start + Coord3(0, 0, int(num))
		elif command == "up":
			start = start + Coord3(0, 0, -int(num))
		elif command == "forward":
			start = start + Coord3(int(num), start.z * int(num), 0)
		else:
			print(f"Invalid command: {command}")
	return start.x * start.y


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	file = os.path.splitext(__file__)[0][-5:]
	with open(os.path.join(FILE_DIR, file + ".input")) as f:
		DATA = f.read().strip()
	DATA = [x.split() for x in DATA.split("\n")]
	print(f"Part 1: {part1(DATA)}")
	print(f"Part 2: {part2(DATA)}")
from day01 import Coord
from typing import List


KEYPAD = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
KEYPAD2 = [[0, 0, "1", 0, 0], [0, "2", "3", "4", 0], ["5", "6", "7", "8", "9"], [0, "A", "B", "C", 0], [0, 0, "D", 0, 0]]
TEST_DATA = """ULL
RRDDD
LURDL
UUUUD"""

def part1(inp: List[str]) -> str:
	start = Coord(1, 1)
	move = {"U": Coord(0, -1), "D": Coord(0, 1), "L": Coord(-1, 0), "R": Coord(1, 0)}
	retVal = ''
	for line in inp:
		for char in line:
			next_spot = start + move[char]
			if 0 <= next_spot.x < 3 and 0 <= next_spot.y < 3:
				start = next_spot
		retVal += KEYPAD[start.y][start.x]
	return retVal


def part2(inp: List[str]) -> str:
	start = Coord(0, 2)
	move = {"U": Coord(0, -1), "D": Coord(0, 1), "L": Coord(-1, 0), "R": Coord(1, 0)}
	retVal = ''
	for line in inp:
		for char in line:
			next_spot = start + move[char]
			if 0 <= next_spot.x < 5 and 0 <= next_spot.y < 5 and KEYPAD2[next_spot.y][next_spot.x] != 0:
				start = next_spot
		retVal += KEYPAD2[start.y][start.x]
	return retVal


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day02.input")) as f:
		RAW_DATA = f.read().strip()
	DATA = RAW_DATA.split("\n")
	print(f"Part one: {part1(DATA)}") # not 88999, too high; 
	print(f"Part two: {part2(DATA)}") # not 57DDB; typo'd answer (transposed B for 8)
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
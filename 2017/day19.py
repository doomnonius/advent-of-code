from typing import List
from day03 import Coord
import string

def part1(inp: List[str]) -> str:
	retVal = ''
	retVal2 = 1
	loc = Coord(inp[0].index("|"), 0)
	max_y = len(inp)
	max_x = len(inp[0])
	direction = "s"
	directions = {"n": Coord(0, -1), "s": Coord(0, 1), "w": Coord(-1, 0), "e": Coord(1, 0)}
	opposites = {"n": "s", "s": "n", "w": "e", "e": "w"}
	loc = loc + directions[direction]
	uppers = list(string.ascii_uppercase)
	while max_x > loc.x >= 0 and max_y > loc.y >= 0:
		spot = inp[loc.y][loc.x]
		# print(loc)
		if spot == "+":
			# find which direction is next
			for k,v in directions.items():
				if k != direction and k != opposites[direction]:
					n = inp[loc.y + v.y][loc.x + v.x]
				else:
					n = ''
				if n in ["|", "-"]:
					direction = k
					break
					# print(f"New direction: {direction}")
		elif spot == " ":
			# assert 0 == 1, f"We've strayed off the trail! {retVal}"
			return retVal, retVal2
		elif spot in uppers:
			retVal += spot
		elif spot == 'E':
			print(spot)
		loc = loc + directions[direction]
		retVal2 += 1
	return retVal, retVal2

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day19.input")) as f:
		RAW_DATA = f.read()
	DATA = RAW_DATA.split("\n")
	# print(DATA[0])
	print(f"Part one: {part1(DATA)[0]}")
	print(f"Part two: {part1(DATA)[1]}")
	# print(f"Time: {timeit.timeit('part2(DATA)', setup='from __main__ import part2, DATA', number = 10)}")
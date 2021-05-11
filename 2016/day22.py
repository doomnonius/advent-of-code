from typing import List
from day01 import Coord


class Node:
	def __init__(self, data: str) -> None:
		split = data.split()
		loc_split = split[0].split("-")
		self.loc = Coord(int(loc_split[1][1:]), int(loc_split[2][1:]))
		self.size = int(split[1][:-1])
		self.used = int(split[2][:-1])
		self.free = int(split[3][:-1])


def part1(inp: List[Node]) -> int:
	retVal = 0
	for i in inp:
		for j in [x for x in inp if x.loc != i.loc]:
			if i.used != 0 and j.free >= i.used:
				retVal += 1
	return retVal





if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day22.input")) as f:
		DATA = f.read().strip()
	DATA = [Node(x) for x in DATA.split("\n")[2:]]
	print(f"Part one: {part1(DATA)}") # not 3061, too high; not 2044, too high; forgot to cast size/used/free to ints
	# print(f"Part two: {}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
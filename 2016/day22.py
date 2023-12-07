from typing import List, Tuple
from itertools import permutations
from statistics import mean
from day01 import Coord

class Node:
	def __init__(self, data: str) -> None:
		split = data.split()
		loc_split = split[0].split("-")
		self.loc = Coord(int(loc_split[1][1:]), int(loc_split[2][1:]))
		self.size = int(split[1][:-1])
		self.used = int(split[2][:-1])
		self.free = int(split[3][:-1])

	def __repr__(self):
		return f"loc: {(self.loc.x, self.loc.y)}, size: {self.size}, used: {self.used}, free: {self.free}" # repr for Coord is (y,x) for some reason!?!?!?

def part1(inp: List[Node]) -> int:
	retVal = 0
	for i,j in permutations(inp, 2):
		if i.used != 0 and j.free >= i.used:
				retVal += 1
	return retVal

def part2(inp: List[Node]):
	"""
	This is going to be a maze in multiple parts: we need to move the data we want, but we need to be moving
	an empty node around to make it happen. First, we need to find the shortest path between our position and
	the destination node. Second, we need to get the empty node to the next spot on that path. Third, we need to
	repeatedly find the fastest way to get the empty node back to the next spot on our fastest path.
	My concern is for step three: is it possible there is a less efficient path to the goal (step one) that is 
	more efficient in step three?
	"""
	stack:List[Tuple[int, Node, List[Node]]] = []
	all_locs = {x.loc for x in inp}
	all_blocks = {x.loc for x in inp if x.size > 100}
	goal = [y for y in inp if y.loc == Coord(max(x.loc.x for x in inp),0)][0]
	target_a = goal.loc
	target_b = Coord(0,0)
	free = [y for y in inp if not y.used][0].loc

	def next_moves(c:Coord, steps:List[Coord]) -> List[Coord]:
		""" This won't return anything, just add to the stack.
		"""
		n = [x for x in c.neighbors() if x not in all_blocks and x in all_locs]
		for i in n:
			all_blocks.add(i)
			s = steps.copy()
			s.append(i)
			stack.append((i, s))

	def find_path(start, end) -> List[Coord]:
		all_blocks.add(start)
		next_moves(start, [])
		while True:
			c, path = stack.pop(0)
			if c == end:
				return path
			next_moves(c, path)

	route = find_path(target_a, target_b)
	r = 0
	for i in range(len(route)):
		stack:List[Tuple[int, Node, List[Node]]] = []
		all_blocks = {x.loc for x in inp if x.size > 100}
		if i: all_blocks.add(route[i-1])
		r += len(find_path(free, route[i])) + 1
		if not i:
			free = target_a
		else:
			free = route[i-1]
	return r
	## used these to grok what the layout
	# print(target)
	# print(f"average size: {mean(x.size for x in inp)}, average used: {mean(x.used for x in inp)}, average free: {mean(x.free for x in inp)}")
	# print(f"max size: {max(x.size for x in inp)}, max used: {max(x.used for x in inp)}, max free: {max(x.free for x in inp)}")
	# print(f"min size: {min(x.size for x in inp)}, min used: {min(x.used for x in inp)}, min free: {min(x.free for x in inp)}")
	# [print(x) for x in inp if x.used == 0]
	# [print(x) for x in inp if x.size > 100]
	# [print(x) for x in inp if x.free > 60]

if __name__ == "__main__":
	from datetime import datetime
	import os
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day22.input")) as f:
		DATA = f.read().strip()
	DATA = [Node(x) for x in DATA.split("\n")[2:]]
	print(f"Part one: {part1(DATA)}") # not 3061, too high; not 2044, too high; forgot to cast size/used/free to ints
	start = datetime.now()
	print(f"Part two: {part2(DATA)}")
	print(f"run time: {datetime.now() - start}")
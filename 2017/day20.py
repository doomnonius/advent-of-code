import re
from typing import NamedTuple, List
from itertools import product


class Coord3d(NamedTuple):
	x: int
	y: int
	z: int

	def neighbors(self):
		return {Coord3d(x[0], x[1], x[2]) for x in product([-1, 0, 1], repeat=3) if x != (0, 0, 0)}
	
	def __add__(self, other):
		return Coord3d(self.x + other.x, self.y + other.y, self.z + other.z)
	
	def __repr__(self):
		return "(" + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ")"


class Particle:
	def __init__(self, data, ident) -> None:
		pattern = r"p=<(?P<pos>.+,.+,.+)>, v=<(?P<vel>.+,.+,.+)>, a=<(?P<acc>.+,.+,.+)>"
		data = re.match(pattern, data)
		self.id = ident
		self.pos = Coord3d(*[int(a) for a in (data.group('pos').split(','))])
		self.vel = Coord3d(*[int(a) for a in (data.group('vel').split(','))])
		self.acc = Coord3d(*[int(a) for a in (data.group('acc').split(','))])
		self.value = manhattan(self.pos)
		
	def next(self):
		# print(self.pos)
		self.vel = self.vel + self.acc
		self.pos = self.pos + self.vel
		# print(self.pos)
		self.value = manhattan(self.pos)
		return self


	def __repr__(self) -> str:
		return f"{self.id}"


def manhattan(p) -> int:
	return (abs(p.x) + abs(p.y) + abs(p.z))


def part2(inp: List[str]) -> int:
	repeat = 0
	while True:
		length_store = len(inp)
		for part in inp:
			part.next()
		posts = {part.id:part.pos for part in inp}
		pos_list = list(posts.values())
		for v in pos_list:
			if pos_list.count(v) > 1:
				[inp.remove(x) for x in inp if x.pos == v]
		if len(inp) == length_store:
			repeat += 1
		else:
			repeat = 0
		if repeat >= 1000:
			return len(inp)


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day20.input")) as f:
		RAW_DATA = f.read().strip()
	DATA = []
	i = 0
	for x in RAW_DATA.split("\n"):
		DATA.append(Particle(x, i))
		i += 1
	# print(DATA)
	print(f"Part one: {[x.id for x in DATA if manhattan(x.acc) == min(manhattan(p.acc) for p in DATA)][0]}") # not 168, too low; not 241, too low; 
	print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('part2(DATA)', setup='from __main__ import part2, DATA', number = 10)}")
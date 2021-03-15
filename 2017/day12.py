from typing import List

class Pipe:
	def __init__(self, data: str):
		self.id, others = data.split(" <-> ")
		self.connected = others.split(", ")

	def __repr__(self) -> str:
		return f"Pipe {self.id} connects to {self.connected}"

def part1(inp: List[Pipe], hits = set(), pipe = None, key = "0") -> int:
	if hits == set():
		for p in inp:
			if p.id != key:
				continue
			hits.add(p.id)
			part1(inp, hits, p)
	if pipe != None:
		for p in pipe.connected:
			if p.id not in hits:
				hits.add(p.id)
				part1(inp, hits, p)
	else:
		return(hits)

def part2(inp: List[Pipe]) -> int:
	groups = []
	for pipe in inp:
		potential = part1(inp, hits = set(), key = pipe.id) # don't know why I have to redeclare hits as an empty set
		if potential not in groups:
			groups.append(potential.copy())
	return len(groups)


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day12.input")) as f:
		RAW_DATA = f.read().strip()
	DATA = [Pipe(x) for x in RAW_DATA.split("\n")]
	for x in DATA:
		for i in range(len(x.connected)):
			for z in DATA:
				if z.id == x.connected[i]:
					x.connected[i] = z
	print(f"Part one: {len(part1(DATA))}") # not 2000, too high; forgot that p.id is a string
	print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
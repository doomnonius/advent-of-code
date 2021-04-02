from typing import List, Set
from day03 import Coord


def part1(inp: List[str]) -> int:
	on = set()
	for line in inp:
		if line.count(" ") == 3:
			command, start, th, end = line.split()
		else:
			commanda, commandb, start, th, end = line.split()
			command = commanda+commandb
		start = [int(x) for x in start.split(',')]
		end = [int(x) for x in end.split(',')]
		if command == "toggle":
			for c in light_section(start, end):
				if c in on:
					on.remove(c)
				else:
					on.add(c)
		elif command == "turnoff":
			for c in light_section(start, end):
				if c in on:
					on.remove(c)
		else:
			for c in light_section(start, end):
				on.add(c)
	return len(on)
		
				
def light_section(start: List[int], end: List[int]) -> Set[Coord]:
	for x in range(start[0], end[0]+1):
		for y in range(start[1], end[1]+1): 
			yield Coord(x, y)


def part2(inp: List[str]) -> int:
	on = {Coord(x, y):0 for x in range(1000) for y in range(1000)}
	for line in inp:
		if line.count(" ") == 3:
			command, start, th, end = line.split()
		else:
			commanda, commandb, start, th, end = line.split()
			command = commanda+commandb
		start = [int(x) for x in start.split(',')]
		end = [int(x) for x in end.split(',')]
		if command == "toggle":
			for c in light_section(start, end):
				on[c] += 2
		elif command == "turnoff":
			for c in light_section(start, end):
				if on[c] > 0:
					on[c] -= 1
		else:
			for c in light_section(start, end):
				on[c] += 1
	return sum(x for x in on.values())



if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day06.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	print(f"Part one: {part1(DATA)}")
	print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('part1(DATA)', setup='from __main__ import part1, DATA', number = 1)}")
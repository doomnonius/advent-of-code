import itertools
from typing import List


class City:
	def __init__(self, data: str) -> None:
		self.name = data
		self.others = {}

	def __repr__(self) -> str:
		return f"{self.name}: {len(self.others)}"


def part1(inp: List[City]) -> int:
	m = 10000000
	for x in [list(z) for z in itertools.permutations(inp, 8)]:
		d = 0
		for i in range(len(x) - 1):
			current = x[i]
			d += int(current.others[x[i+1].name])
			if d > m:
				break
		if d < m:
			m = d
	return m
			

def part2(inp: List[City]) -> int:
	m = 0
	for x in [list(z) for z in itertools.permutations(inp, 8)]:
		d = 0
		for i in range(len(x) - 1):
			current = x[i]
			d += int(current.others[x[i+1].name])
		if d > m:
			m = d
	return m


def add_distances(data: List[List[str]], cities: List[City]) -> None:
	for line in data:
		for city in cities:
			if city.name == line[0]:
				city.others[line[2]] = line[-1]
			if city.name == line[2]:
				city.others[line[0]] = line[-1]


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day09.input")) as f:
		DATA = f.read().strip()
	DATA = [y.split() for y in DATA.split("\n")]
	CITIES = {x[0] for x in DATA}
	CITIES.update({x[2] for x in DATA})
	CITIES = [City(x) for x in CITIES]
	# print(CITIES)
	add_distances(DATA, CITIES)
	# print(CITIES)
	print(f"Part one: {part1(CITIES)}")
	print(f"Part two: {part2(CITIES)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
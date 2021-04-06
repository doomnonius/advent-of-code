import itertools
from typing import List, Dict


class Person:
	def __init__(self, data: str) -> None:
		self.name = data
		self.relates = {}

	def update(self, neighbor: str, sign: str, num: str) -> None:
		if sign == "gain":
			value = int(num)
		else:
			value = int('-' + num)
		self.relates[neighbor] = value

	def __repr__(self) -> str:
		return f"{self.relates}"


def part1(inp: Dict[str, Person]) -> int:
	m = 0
	l = len(inp)
	for combo in itertools.permutations(inp.keys(), l):
		happiness = 0
		for person in range(len(combo)):
			happiness += inp[combo[person]].relates[combo[(person + 1) % l]] + inp[combo[person]].relates[combo[(person - 1) % l]]
		if happiness > m:
			m = happiness
	return m


def parse(inp: List[str]) -> Dict[str, Person]:
	persons = {}
	for line in inp:
		split = line.split()
		p, sign, num, neighbor = split[0], split[2], split[3], split[-1][:-1]
		if p not in [x for x in persons]:
			persons[p] = Person(p)
		persons[p].update(neighbor, sign, num)
	return persons



if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day13.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	PERSONS = parse(DATA)
	print(f"Part one: {part1(PERSONS)}")
	YOU = Person("You")
	for person in PERSONS:
		PERSONS[person].relates["You"] = 0
		YOU.relates[person] = 0
	PERSONS['You'] = YOU
	print(f"Part two: {part1(PERSONS)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
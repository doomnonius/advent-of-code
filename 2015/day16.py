from typing import List


KNOWN = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}


class Sue:
	def __init__(self, data: str) -> None:
		split = data.split()
		self.num_attrs = (len(split) - 2)//2
		self.id = int(split[1][:-1])
		self.attrs = {}
		for x in range(self.num_attrs):
			if x < self.num_attrs - 1:
				self.attrs[split[2*(x+1)][:-1]] = int(split[2*(x+1)+1][:-1])
			else:
				self.attrs[split[2*(x+1)][:-1]] = int(split[2*(x+1)+1])

	def __repr__(self) -> str:
		return f"{self.id}: {self.attrs}"


def part1(inp: List[Sue]) -> int:
	good = set()
	for x in inp:
		good.add(x)
		for attr in KNOWN:
			if attr in x.attrs.keys():
				if x.attrs[attr] != KNOWN[attr]:
					good.remove(x)
					break
	return min(x.id for x in good)


def part2(inp: List[Sue]) -> int:
	good = set()
	for x in inp:
		good.add(x)
		for attr in KNOWN:
			if attr in x.attrs.keys():
				if attr == "cats" or attr == "trees":
					if x.attrs[attr] <= KNOWN[attr]:
						good.remove(x)
						break
				elif attr == "pomeranians" or attr == "goldfish":
					if x.attrs[attr] >= KNOWN[attr]:
						good.remove(x)
						break
				elif x.attrs[attr] != KNOWN[attr]:
					good.remove(x)
					break
	return min(x.id for x in good)


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day16.input")) as f:
		DATA = f.read().strip()
	DATA = [Sue(x) for x in DATA.split("\n")]
	print(f"Part one: {part1(DATA)}")
	print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
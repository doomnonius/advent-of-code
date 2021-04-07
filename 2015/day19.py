from os import replace
from typing import Dict, List


class Replace:
	def __init__(self, initial: str) -> None:
		self.initial = initial
		self.out = set()


def part1(replacements: Dict[str, Replace], compound: str) -> int:
	retVal = set()
	i = 0
	l = len(compound)
	while i < l:
		atom = compound[i]
		if i < l - 1 and compound[i+1].islower():
			atom += compound[i+1]
		for o in replacements[atom]


		i += len(atom)



def parse(inp: List[str]) -> Dict[str, Replace]:
	replacements = {}
	for line in inp:
		start, end = line.split()[0::2]
		if start not in replacements.keys():
			replacements[start] = Replace(start)
		replacements[start].out.add(end)
	return replacements




if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day19.input")) as f:
		DATA = f.read().strip()
	DATA1, DATA2 = DATA.split("\n\n")
	DATA1 = parse(DATA1.split("\n"))
	print(f"Part one: {part1(DATA1, DATA2)}")
	# print(f"Part two: {}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
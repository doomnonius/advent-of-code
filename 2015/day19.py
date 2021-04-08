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
		la = len(atom)
		if atom in replacements:
			for o in replacements[atom].out:
				retVal.add(compound[:i] + o + compound[i+la:])
		i += la
	return len(retVal)


def part2(rev_replace: Dict[str, str], compound: str, retVal = 0) -> int:
	while compound:
		for molecule in rev_replace:
			if (c := compound.count(molecule)):
				retVal += c
				compound = compound.replace(molecule, rev_replace[molecule])
				compound = compound.replace('e', '')
	return retVal



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
	REPLACE, TARGET = DATA.split("\n\n")
	REPLACE = parse(REPLACE.split("\n"))
	print(f"Part one: {part1(REPLACE, TARGET)}")
	REVERSE_REPLACE = {x:y for y in REPLACE.keys() for x in REPLACE[y].out}
	print(f"Part two: {part2(REVERSE_REPLACE, TARGET)}") # got it first try, pretty sure very lucky and not necessarily replicable with other inputs
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
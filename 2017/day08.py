from typing import List


def part1(inp: List[str]) -> int:
	registers = {}
	for line in inp:
		register, command, num, i, nom, comp, pred = line.split()
		if register not in registers.keys():
			registers[register] = 0
		if nom not in registers.keys():
			registers[nom] = 0
		if eval (" ".join([f"registers['{nom}']", comp, pred])):
			if command == "dec":
				registers[register] -= int(num)
			else:
				registers[register] += int(num)
	return max(registers.values())

def part2(inp: List[str]) -> int:
	registers = {}
	m = 0
	for line in inp:
		register, command, num, i, nom, comp, pred = line.split()
		if register not in registers.keys():
			registers[register] = 0
		if nom not in registers.keys():
			registers[nom] = 0
		if eval (" ".join([f"registers['{nom}']", comp, pred])):
			if command == "dec":
				registers[register] -= int(num)
			else:
				registers[register] += int(num)
		m = max(max(registers.values()), m)
	return m

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day08.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	# print(DATA)
	print(f"Part one: {part1(DATA.copy())}")
	print(f"Part two: {part2(DATA.copy())}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
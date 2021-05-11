from typing import List

class Prog:
	def __init__(self, data: str):
		data = data.replace(")", "")
		if ">" in data:
			first, second = data.split(" -> ")
			self.holds = second.split(", ")
		else:
			first = data
			self.holds = None
		self.name, self.weight = first.split(" (")
		self.children = []
		self.parent = None
		self.total_weight = 0

	def __repr__(self):
		return f"{self.name} weighs {self.weight} on its own and {self.total_weight} in total and holds {self.holds}"

def part1(inp: List[Prog]) -> str:
	for program in inp:
		if program.parent == None:
			return program.name

def part2(inp: List[Prog]) -> str:
	for program in inp:
		for i in range(len(program.children)-1):
			nom = program.children[i].total_weight
			pred = program.children[i + 1].total_weight
			if nom != pred:
				print(f"{program.children}")
				# I finished this one off by hand with the printed info above

				# if program.children.count(nom) > 1:
				# 	diff = nom - pred
				# 	print(diff)
				# 	return int(program.children[i + 1].weight) - diff
				# else:
				# 	diff = pred - nom
				# 	print(diff)
				# 	return int(program.children[i].weight) - diff
	return "I finished this one off by hand with the printed info above"
	

def calcWeight(inp: List[Prog]) -> int:
	retVal = 0
	for program in inp:
		if program.children:
			retVal += int(program.weight) + calcWeight(program.children)
		else:
			retVal += int(program.weight)
	return retVal

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day07.input")) as f:
		DATA = f.read().strip()
	DATA = [Prog(x) for x in DATA.split("\n")]
	for program in DATA:
		if program.holds:
			for pro in program.holds:
				for p in DATA:
					if p.name == pro:
						program.children.append(p)
						p.parent = program.name
	for program in DATA:
		program.total_weight = calcWeight([program])
	print(f"Part one: {part1(DATA)}")
	print(f"Part two: {part2(DATA.copy())}") # not 5537, too high; not 2741, also too high
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
import string
from typing import List


TEST_DATA = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""


def part1(inp: List[str], p2 = False) -> int:
	regs = {}
	j = 0
	broken = False
	while j < len(inp):
		ins, out = inp[j].split(" -> ")
		if p2 and out == "b":
			ins = '16076'
		split = ins.split()
		for i in range(len(split)):
			if isNumber(split[i]) and len(split) > 1:
				split[i] = int(split[i])
			elif split[i].islower() and len(split) > 1:
				if split[i] not in regs:
					hold = inp.pop(j)
					inp.append(hold)
					broken = True
					break
				split[i] = regs[split[i]]
			elif len(split) > 1:
				command = split[i]
			else:
				if isNumber(split[i]): command = int(split[i])
				else:
					if split[i] not in regs:
						hold = inp.pop(j)
						inp.append(hold)
						broken = True
						break
					command = regs[split[i]]
		if broken:
			broken = False
			continue
		if command == "AND":
			result = split[0] & split[2]
		elif command == "LSHIFT":
			result = split[0] << split[2]
		elif command == "RSHIFT":
			result = split[0] >> split[2]
		elif command == "OR":
			result = split[0] | split[2]
		elif command == "NOT":
			result = ~split[1]
		else:
			result = command
		if result < 0: result += 65536
		regs[out] = result
		inp.pop(0)
	return regs


def isNumber(val: str) -> bool:
	try:
		int(val)
	except ValueError:
		return False
	return True


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day07.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	print(f"Part one: {part1(DATA.copy())['a']}")
	print(f"Part two: {part1(DATA, True)['a']}") # honestly, this is pretty jank
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
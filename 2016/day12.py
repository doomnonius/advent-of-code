


from typing import List


def part1(inp: List[str], regs = {}, debug = False) -> int:
	i = 0
	l = len(inp)
	while i < l:
		if inp[i][0:3] == "cpy" or inp[i][0:3] == "jnz":
			command, noun, verb = inp[i].split()
		else:
			command, noun, verb = inp[i].split() + ["z"]
		if isNumber(noun):
			noun = int(noun)
		else:
			if noun not in regs.keys():
				regs[noun] = 0
		if isNumber(verb):
			verb = int(verb)
		else:
			if verb not in regs.keys():
				regs[verb] = 0
		if command == "cpy":
			try:
				regs[verb] = regs[noun]
			except KeyError:
				regs[verb] = noun
		elif command == "inc":
			regs[noun] += 1
		elif command == "dec":
			regs[noun] -= 1
		elif command == 'jnz':
			try:
				if regs[noun] != 0:
					i += verb
					continue
			except KeyError:
				if noun != 0:
					i += verb
					continue
		i += 1
		if debug: print(regs)
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
	with open(os.path.join(FILE_DIR, "day12.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	print(f"Part one: {part1(DATA)['a']}")
	print(f"Part two: {part1(DATA, {'c': 1})['a']}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
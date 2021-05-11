from typing import List


def part1(inp: List[str], regs = {}, p2 = False) -> int:
	i = 0
	l = len(inp)
	if not p2:
		regs['a'] = 7
	else:
		regs['a'] = 10
	toggled = set()
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
		if (command == "cpy" and i not in toggled) or (command == "jnz" and i in toggled):
			try:
				regs[verb] = regs[noun]
			except KeyError:
				regs[verb] = noun
		elif (command == "inc" and i not in toggled) or (command == "dec" and i in toggled) or (command == "tgl" and i in toggled):
			regs[noun] += 1
		elif (command == "dec" and i not in toggled) or (command == "inc" and i in toggled):
			regs[noun] -= 1
		elif (command == 'jnz' and i not in toggled) or (command == "cpy" and i in toggled):
			# print(regs)
			if isNumber(verb):
				verb = int(verb)
			else:
				if verb not in regs.keys():
					regs[verb] = 0
				verb = regs[verb]
			try:
				if regs[noun] != 0:
					i += verb
					continue
			except KeyError:
				if noun != 0:
					i += verb
					continue
		elif command == "tgl" and i not in toggled:
			print(regs)
			try:
				hits = i + noun
			except:
				hits = i + regs[noun]
			if hits in toggled:
				toggled.remove(hits)
			else:
				toggled.add(hits)
		i += 1
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
	with open(os.path.join(FILE_DIR, "day23.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	print(f"Part one: {part1(DATA)['a']}")
	print(f"Part two: {part1(DATA, p2 = True)['a']}") # not 3636508, too low; 
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
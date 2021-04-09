from typing import Dict, List


def part1(inp: List[str], regs: Dict[str, int]) -> int:
	i = 0
	l = len(inp)
	while i < l:
		line = inp[i].split()
		command = line[0]
		if len(line) == 3:
			reg = line[1][:-1]
			jump = int(line[2])
			cond = regs[reg] % 2
			if command == 'jio' and regs[reg] == 1:
				i += jump
				continue
			elif command == 'jie' and not cond:
				i += jump
				continue
		else:
			reg = line[1]
			if command == 'hlf':
				regs[reg] /= 2
			elif command == 'tpl':
				regs[reg] *= 3
			elif command == 'inc':
				regs[reg] += 1
			elif command == 'jmp':
				i += int(reg)
				continue
		i += 1
	return regs['b']


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day23.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	print(f"Part one: {part1(DATA, {'a': 0, 'b': 0})}")
	print(f"Part two: {part1(DATA, {'a': 1, 'b': 0})}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
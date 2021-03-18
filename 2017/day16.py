from typing import List
import string

def part1(inp: List[str], dancers = []) -> List[str]:
	if not dancers:
		dancers = list(string.ascii_lowercase)[:16]
	for inst in inp:
		if inst[0] == "s":
			n = int(inst[1:])
			dancers = dancers[-n:] + dancers[:-n]
		elif inst[0] == "x":
			s = inst[1:].split("/")
			n1 = int(s[0])
			n2 = int(s[1])
			dancers[n1], dancers[n2] = dancers[n2], dancers[n1]
		elif inst[0] == "p":
			s = inst[1:].split("/")
			n1 = dancers.index(s[0])
			n2 = dancers.index(s[1])
			dancers[n1], dancers[n2] = dancers[n2], dancers[n1]
		else:
			print("How did this happen?")
	return dancers

def part2(inp: List[str]) -> str:
	dancers = list(string.ascii_lowercase)[:16]
	dancers = part1(inp, dancers)
	prev_states = [''.join(dancers)]
	print(''.join(dancers))
	print(prev_states[0])
	for _ in range(1000000000-1):
		dancers = part1(inp, dancers)
		result = ''.join(dancers)
		if result == prev_states[0]:
			break
		else:
			prev_states.append(result)
		assert result == ''.join(dancers), "Not equiv"
	mod_val = len(prev_states)
	location = 1000000000 % mod_val
	return prev_states[(location - 1) % mod_val]

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day16.input")) as f:
		RAW_DATA = f.read().strip()
	DATA = RAW_DATA.split(",")
	print(f"Part one: {''.join(part1(DATA))}")
	print(f"Part two: {''.join(part2(DATA))}") # not bkgcdefiholnpmja; nor pacdefghijkbknlom; nor bdgnkefijolcpmha; lists were not working how I expected
	# print(f"Time: {timeit.timeit('part2(DATA)', setup='from __main__ import part2, DATA', number = 10)}")
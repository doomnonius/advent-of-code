from typing import List, Tuple


class Component:
	def __init__(self, inp: str) -> None:
		a, b = inp.split("/")
		self.show = inp
		self.port1 = int(a)
		self.port2 = int(b)
		self.avail = {self.port1: True, self.port2: True}
		self.value = self.port1 + self.port2
		self.used = False

	def __repr__(self) -> str:
		return f"{self.show}"

def part1(inp: List[Component], empty: int, string = []) -> int:
	found = False
	options = []
	for comp in [x for x in inp if empty in x.avail.keys() and not x.used]:
		if comp.avail[empty]:
			comp.avail[empty] = False
			comp.used = True
			found = True
			string.append(comp)
			if comp.avail[comp.port1]:
				options.append(comp.value + part1(inp, comp.port1, string.copy()))
			else:
				options.append(comp.value + part1(inp, comp.port2, string.copy()))
			comp.avail[empty] = True
			comp.used = False
	if not found:
		return 0
	else:
		return max(options)

def part2(inp: List[Component], empty: int, l = 0, string = []) -> Tuple[int]:
	found = False
	options = []
	for comp in [x for x in inp if empty in x.avail.keys() and not x.used]:
		if comp.avail[empty]:
			l += 1
			comp.avail[empty] = False
			comp.used = True
			found = True
			string.append(comp)
			if comp.avail[comp.port1]:
				r = part2(inp, comp.port1, l, string.copy())
				options.append((comp.value + r[0], r[1]))
			else:
				r = part2(inp, comp.port2, l, string.copy())
				options.append((comp.value + r[0], r[1]))
			comp.avail[empty] = True
			comp.used = False
			l -= 1
	if not found:
		if l >= 56:
			print(sum(comp.value for comp in inp if comp.used == True))
		return (0, l)
	else:
		longest = max(x[1] for x in options)
		longest_options = [x for x in options if x[1] == longest]
		return (max(x[0] for x in longest_options), longest)

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day24.input")) as f:
		RAW_DATA = f.read().strip()
	DATA = [Component(x) for x in RAW_DATA.split('\n')]
	print(f"Part one: {part1(DATA, 0)}") # not 2368, too high; not 1531, too low; not 2046, too high; my loop was marking something as unusable that should have been usable again later - ie if a, d, and f matched the condition, if would run properly with a as the condition, but with d as the condition a would be marked as invalid for use later in the chain; the fix also enabled me to remove the memory intensive copying
	print(f"Part two: {part2(DATA, 0)[0]}") # not 1488, too low; # needed to reset the length counter same as reseting the components
	# print(f"Time: {timeit.timeit('part1(DATA, 18)', setup='from __main__ import part1, DATA', number = 1)}")
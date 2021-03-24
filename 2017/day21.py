from typing import List
from math import sqrt

PATTERN = ".#...####"
# PATTERN = "abcdefghijklmnop"
# PATTERN = "abcdefghijklmnopqrstuvwxyzabcdefghij"

def mirror(patt: List[str]) -> List[str]:
	for i in range(len(patt)):
		patt[i] = patt[i][::-1]
	return patt

def rotate(patt: List[str]) -> List[str]:
	l = len(patt)
	if l == 2:
		tl = patt[0][0]
		tr = patt[0][1]
		br = patt[1][1]
		bl = patt[1][0]
		patt[0] = bl + tl
		patt[1] = br + tr
	elif l == 3:
		tl = patt[0][0]
		tm = patt[0][1]
		tr = patt[0][2]
		rm = patt[1][2]
		br = patt[2][2]
		bm = patt[2][1]
		bl = patt[2][0]
		lm = patt[1][0]
		m = patt[1][1]
		patt[0] = bl + lm + tl
		patt[1] = bm + m + tm
		patt[2] = br + rm + tr
	else:
		assert 0 == 1, f"length shouldn't be {l}"
	return patt

class Rule:
	def __init__(self, line) -> None:
		self.in_patt, self.out_patt = [x.split("/") for x in line.split(" => ")]
		if len(self.in_patt) == 2:
			self.size = 2
		else:
			self.size = 3
		self.octo = sum(x.count("#") for x in self.in_patt)
		self.alts = set()
		for _ in range(8):
			self.in_patt = rotate(self.in_patt)
			if _ % 4 == 0:
				self.in_patt = mirror(self.in_patt)
			self.alts.add(''.join(self.in_patt))


	def __repr__(self) -> str:
		return f"{self.in_patt} -> {self.out_patt}"


def part1(inp: List[Rule], cycles) -> str:
	pat = PATTERN
	while cycles > 0:
		# print(f"Cycle: {abs(6 - cycles)}")
		pat = permutate(inp, pat)
		cycles -= 1
	return pat


def permutate(rules: List[Rule], pattern: str) -> str:
	size = int(sqrt(len(pattern)))
	mod_two = (size % 2 == 0)
	if mod_two:
		mod = 2
	else:
		mod = 3
	sub_starts = []
	for i in range(size//mod):
		sub_starts += [(size * x) + i for x in range(size//mod)]
	sub_starts.sort()
	returns = []
	for i in sub_starts:
		x = pattern[i*mod:(i+1)*mod] + pattern[i*mod+(size):(i+1)*mod+(size)]
		if mod == 3:
			x += pattern[i*mod+(size*2):(i+1)*mod+(size*2)]
		for rule in rules:
			if rule.octo != x.count("#"):
				continue
			if x in rule.alts:
				returns.append(rule.out_patt)
	#build the new pattern from returns
	row_length = int(sqrt(len(returns)))
	if row_length == 1:
		return ''.join(returns[0])
	#else
	retVal = ''
	for i in range(row_length):
		next_set = returns[i*row_length:(i+1)*row_length]
		for m in range(mod+1):
			retVal += ''.join(a[m] for a in next_set)
	return retVal

if __name__ == "__main__":
	import os, datetime
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day21.input")) as f:
		RAW_DATA = f.read().strip()
	DATA = [Rule(x) for x in RAW_DATA.split('\n')]
	print(f"Part one: {part1(DATA, 5).count('#')}") # not 118, too low; not 134, too low; not 363, too high; should have checked for divis by 2 instead of divis by 3
	print(f"Part two: {part1(DATA, 18).count('#')}") # 20 seconds to solve
	# print(f"Time: {timeit.timeit('part1(DATA, 18)', setup='from __main__ import part1, DATA', number = 1)}")
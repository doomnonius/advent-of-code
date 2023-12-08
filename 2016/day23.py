from typing import List, Dict

class Instruction:
	def __init__(self, inp:str):
		r = inp.split()
		try:
			self.command, self.noun, self.verb = r
			if self.verb[-1].isdigit():
				self.verb_d = True
				self.verb = int(self.verb)
			else:
				self.verb_d = False
		except:
			self.command, self.noun = r
			self.verb = False
		if self.noun[-1].isdigit():
			self.noun_d = True
			self.noun = int(self.noun)
		else:
			self.noun_d = False

	def __repr__(self):
		if self.verb: return f"{self.command, self.noun, self.verb}"
		return f"{self.command, self.noun}"
	
	def toggle(self):
		swaps = {
			"dec":"inc",
		   	"tgl":"inc",
			"inc":"dec",
			"jnz":"cpy",
			"cpy":"jnz"
			}
		self.command = swaps[self.command]
		# print("Toggled!")

	def execute(self, d:Dict, inp:List, i, p2):
		# optimizations
		if i == 2:
			d['a'] = d['a'] * d['b']
			return 10
		if self.command == "inc":
			d[self.noun] += 1
			return i + 1
		elif self.command == "dec":
			d[self.noun] -= 1
			return i + 1
		elif self.command == "cpy":
			# cpy will always have str as verb
			if self.noun_d:
				d[self.verb] = self.noun
				return i + 1
			d[self.verb] = d[self.noun]
			return i + 1
		elif self.command == "jnz":
			if self.verb_d:
				r = self.verb
			else:
				r = d[self.verb]
			if self.noun_d:
				if self.noun != 0:
					return i + r
				return i + 1
			# print(d[self.noun])
			if d[self.noun] != 0:
				return i + r
			return i + 1
		elif self.command == "tgl":
			if self.noun_d:
				r = self.noun
			else:
				r = d[self.noun]
			try:
				inp[i + r].toggle()
			except:
				pass
		return i + 1
			


def part1(inp: List[Instruction], regs = {}, p2 = False) -> int:
	i = 0
	l = len(inp)
	if not p2:
		regs = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
	else:
		regs= {'a': 12, 'b': 0, 'c': 0, 'd': 0}
	
	track = []

	count = 0
	while i < l:
		i = inp[i].execute(regs, inp, i, p2)
	# notes:
	# i 2-9 is a = a * b - this is part that needed to be optimized - manually multiplying 9 digit numbers by adding one number at a time is ... not efficient
	# instruction in i[10] to dec b is important
	# i 11-15 is c = b * 2, then 16 toggles the instruction c away
	# i 17 sets c to -16, then i 18 jumps us to i 2
	# the last thing toggled away is 18 jumping us back down, when b = 1, c = 1 (because jnz is now copy), d = 0
	# so by the time we have toggled i 18, 20, 22, 24
	# 19 makes c 94
	# we loop i 20-22, 20 makes d 82, and 21-23 a = a + d
	# 24 decreases c
	# 25 jumps based on c
	# a += so d (82) * c (94) times
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
		RAW_DATA = f.read().strip()
	DATA = [Instruction(x) for x in RAW_DATA.split("\n")]
	# DATA = DATA.split("\n")
	print(f"Part one: {part1(DATA)['a']}")
	DATA = [Instruction(x) for x in RAW_DATA.split("\n")]
	print(f"Part two: {part1(DATA, p2 = True)['a']}") # not 3636508, too low; 479,001,600 + (94*82) = 479009308
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
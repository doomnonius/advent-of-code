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
		if self.command == "inc":
			d[self.noun] += 1
			return i + 1
		elif self.command == "mul":
			d[self.noun] *= d[self.verb]
			return i + 1
		elif self.command == "add":
			d[self.noun] += d[self.verb]
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
		regs['a'] = 7
	else:
		regs['a'] = 12
	
	if p2: # I'm dumb, Peter would have had different instructions than me. I'm going to write some code to look
		# loops, and then either manually shortcut or make the code shortcut for me
		inp[2] = Instruction("mul a b")
		for x in range(3,11):
			inp[x] = Instruction("nop a b")
		inp[21] = Instruction("add d a")
		inp[22] = Instruction("nop a b")
		inp[23] = Instruction("nop a b")

	count = 0
	while i < l:
		i = inp[i].execute(regs, inp, i, p2)
		if not count % 1000:
			print(regs)

	# toggled = set()
	# while i < l:
	# 	if inp[i][0:3] == "cpy" or inp[i][0:3] == "jnz":
	# 		command, noun, verb = inp[i].split()
	# 	else:
	# 		command, noun, verb = inp[i].split() + ["z"]
	# 	if isNumber(noun):
	# 		noun = int(noun)
	# 	else:
	# 		if noun not in regs.keys():
	# 			regs[noun] = 0
	# 	if isNumber(verb):
	# 		verb = int(verb)
	# 	else:
	# 		if verb not in regs.keys():
	# 			regs[verb] = 0
	# 	if (command == "cpy" and i not in toggled) or (command == "jnz" and i in toggled):
	# 		try:
	# 			regs[verb] = regs[noun]
	# 		except KeyError:
	# 			regs[verb] = noun
	# 	elif (command == "inc" and i not in toggled) or (command == "dec" and i in toggled) or (command == "tgl" and i in toggled):
	# 		regs[noun] += 1
	# 	elif (command == "dec" and i not in toggled) or (command == "inc" and i in toggled):
	# 		regs[noun] -= 1
	# 	elif (command == 'jnz' and i not in toggled) or (command == "cpy" and i in toggled):
	# 		# print(regs)
	# 		if isNumber(verb):
	# 			verb = int(verb)
	# 		else:
	# 			if verb not in regs.keys():
	# 				regs[verb] = 0
	# 			verb = regs[verb]
	# 		try:
	# 			if regs[noun] != 0:
	# 				i += verb
	# 				continue
	# 		except KeyError:
	# 			if noun != 0:
	# 				i += verb
	# 				continue
	# 	elif command == "tgl" and i not in toggled:
	# 		print(regs, toggled)
	# 		try:
	# 			hits = i + noun
	# 		except:
	# 			hits = i + regs[noun]
	# 		if hits in toggled:
	# 			toggled.remove(hits)
	# 		else:
	# 			toggled.add(hits)
	# 	i += 1
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
	print(f"Part two: {part1(DATA, p2 = True)['a']}") # not 3636508, too low; something around 479,001,600
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
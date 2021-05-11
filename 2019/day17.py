from typing import List
from day10 import Coord
from day02 import Computer

class Ascii (Computer):
	def __init__(self, inst):
		super().__init__(inst)
		self.scaffold = set()
		self.x = 0
		self.y = 0
		self.inp_c = 0
		self.main_routine = ["A", ",", "B", ",", "B", ",", "A", ",", "C", ",", "B", ",", "C", ",", "C", ",", "B", ",", "A", "\n"]
		self.move_a = ["R", ",", "10",  ",", "R", ",", "8", ",", "L", ",", "10", ",", "L", ",", "10", "\n"]
		self.move_b = ["R", ",", "8", ",", "L", ",", "6", ",", "L", ",", "6", "\n"]
		self.move_c = ["L", ",", "10", ",", "R", ",", "10", ",", "L", ",", "6", "\n"]
		self.y_n = ["n", "\n"]
		self.routines = [self.main_routine, self.move_a, self.move_b, self.move_c, self.y_n]
		self.next_routine = []

	def output(self, data):
		if data < 200: print(chr(data), end='')
		else: self.out = data
		if data == 35: self.scaffold.add(Coord(self.x, self.y))
		self.x += 1
		if data == 10:
			self.y += 1
			self.x = 0
		return self

	def input(self):
		if not self.next_routine and self.inp_c < 5:
			self.next_routine = self.routines[self.inp_c]
			self.next_routine = ''.join(self.next_routine)
			print(f"{self.next_routine}")
			self.inp_c += 1
		retVal = self.next_routine[0]
		self.next_routine = self.next_routine[1:]
		return ord(retVal)


	def run_codes(self, index_return = 0, at_index = 0):
		# needed to remove the return after running opcode 3
		while True:
			initial_opcode = self.codes[self.index]
			opcode = initial_opcode%100
			p1 = initial_opcode//100%10
			p2 = initial_opcode//1000%10
			p3 = initial_opcode//10000
			if opcode == 1:
				self.code1(p1, p2, p3)
			if opcode == 2:
				self.code2(p1, p2, p3)
			if opcode == 3:
				self.code3(p1)
			if opcode == 4:
				self.code4(p1)
			if opcode == 5:
				self.code5(p1, p2)
			if opcode == 6:
				self.code6(p1, p2)
			if opcode == 7:
				self.code7(p1, p2, p3)
			if opcode == 8:
				self.code8(p1, p2, p3)
			if opcode == 9:
				self.code9(p1)
			if opcode == 99:
				self.done = True
				try: return self.out
				except: return self.codes[index_return]

def alignment_parameters(inst: List[int]) -> int:
	retVal = 0
	robot = Ascii(inst)
	while not robot.done:
		robot.run_codes()
	for scaffold in robot.scaffold:
		c = 0
		for n in scaffold.neighbors():
			if n in robot.scaffold:
				c += 1
		if c == 4:
			retVal += scaffold.x * scaffold.y
	return retVal

def explore_scaffold(inst: List[int]):
	robot = Ascii(inst)
	robot.replace(0, 2)
	"""normally there would be code here, but I ended up solving this one by hand. felt easier.
	in retrospect I think it would have been quite easy to map instead of counting by hand, but even then I would have 
	found the patterns manually.
	the challenge with this one was figuring out how to do 10, was actually really easy but I overcomplicated it"""
	retVal = robot.run_codes()
	return retVal

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day17.input")) as f:
		DATA = f.read().strip()
	DATA = [int(x) for x in DATA.split(",")]
	print(f"Part one: {alignment_parameters(DATA.copy())}")
	print(f"Part two: {explore_scaffold(DATA)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
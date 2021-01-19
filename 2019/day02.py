from typing import List

class Computer:
	def __init__(self, codes: List, index = 0, inp = []):
		self.codes = codes
		self.index = index
		self.input_list = inp
		self.done = False
	
	def __repr__(self):
		return str(self.codes)

	def code1(self, p1, p2, p3):
		self.codes[self.parameter(p3, self.index + 3)] = self.codes[self.parameter(p1, self.index + 1)] + self.codes[self.parameter(p2, self.index + 2)]
		self.index += 4
		return self

	def code2(self, p1, p2, p3):
		self.codes[self.parameter(p3, self.index + 3)] = self.codes[self.parameter(p1, self.index + 1)] * self.codes[self.parameter(p2, self.index + 2)]
		self.index += 4
		return self

	def code3(self, p1):
		self.codes[self.parameter(p1, self.index + 1)] = self.input()
		self.index += 2
		return self

	def code4(self, p1):
		self.output(self.codes[self.parameter(p1, self.index + 1)])
		self.index += 2

	def code5(self, p1, p2):
		if self.codes[self.parameter(p1, self.index+1)]: # because anything not 0 = true in python
			self.index = self.codes[self.parameter(p2, self.index+2)]
		else:
			self.index += 3
		return self

	def code6(self, p1, p2):
		if not self.codes[self.parameter(p1, self.index+1)]: # because 0 = false in python
			self.index = self.codes[self.parameter(p2, self.index+2)]
		else:
			self.index += 3
		return self

	def code7(self, p1, p2, p3):
		if self.codes[self.parameter(p1, self.index+1)] < self.codes[self.parameter(p2, self.index+2)]:
			self.codes[self.parameter(p3, self.index+3)] = 1
		else:
			self.codes[self.parameter(p3, self.index+3)] = 0
		self.index += 4
		return self

	def code8(self, p1, p2, p3):
		if self.codes[self.parameter(p1, self.index+1)] == self.codes[self.parameter(p2, self.index+2)]:
			self.codes[self.parameter(p3, self.index+3)] = 1
		else:
			self.codes[self.parameter(p3, self.index+3)] = 0
		self.index += 4
		return self

	def input(self):
		if self.input_list:
			return self.input_list.pop(0)
		else:
			raise IndexError

	def output(self, data):
		self.out = data
		# print(data)

	def parameter(self, p, index):
		if p == 0:
			return self.codes[index]
		elif p == 1:
			return index

	def replace(self, index: int, new_num: int):
		self.codes[index] = new_num
		return self

	def noun(self, n: int):
		self.codes[1] = n
		return self

	def verb(self, n: int):
		self.codes[2] = n
		return self

	def run_codes(self, index_return = 0, at_index = 0):
		while True:
			# print(f"i: {self.index}")
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
				return self.out
			if opcode == 5:
				self.code5(p1, p2)
			if opcode == 6:
				self.code6(p1, p2)
			if opcode == 7:
				self.code7(p1, p2, p3)
			if opcode == 8:
				self.code8(p1, p2, p3)
			if opcode == 99:
				self.done = True
				try: return self.out
				except: return self.codes[index_return]

def test_codes(codes):
	x = y = 0
	while x < 99:
		while y < 99:
			comp = Computer(codes.copy(), 0)
			comp.noun(x)
			comp.verb(y)
			if comp.run_codes() == 19690720:
				return 100 * x + y
			y += 1
			# print(f"x: {x}, y: {y}")
		x += 1
		y = 0
		# print(f"x: {x}, y: {y}")



TEST_DATA = """1,9,10,3,2,3,11,0,99,30,40,50"""

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day02.input")) as f:
		DATA = f.read().strip()
	CODES = [int(x) for x in DATA.split(",")]
	BACKUP = CODES.copy()
	OPLIST = Computer(CODES, 0)
	OPLIST.replace(1, 12)
	OPLIST.replace(2, 2)
	print(f"Part one: {OPLIST.run_codes()}") # not 512, too low; not 29848, too low; -> 3716250 - forgot to read instructions properly
	print(f"Part two: {test_codes(BACKUP)}") # not 13600, too high; -> 6472 - interpreted math order of operations incorrectly
	print(f"Time: {timeit.timeit('test_codes(BACKUP)', setup='from __main__ import test_codes, BACKUP', number = 1)}")
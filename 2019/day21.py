from day02 import Computer

class Spring (Computer):
	def __init__(self, inst):
		super().__init__(inst)
		self.entered = False
		self.all_inputs = []

	def output(self, data):
		if data < 200: print(chr(data), end='')
		else: self.out = data
		return self

	def input(self):
		if not self.input_list and not self.entered:
			self.input_list = list(self.all_inputs.pop())[::-1]
			self.entered = True
		elif not self.input_list and self.entered:
			self.entered = False
			return 10
		return ord(self.input_list.pop())

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

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day21.input")) as f:
		DATA = f.read().strip()
	DATA = [int(x) for x in DATA.split(",")]
	springyboi = Spring(DATA.copy())
	springyboi.all_inputs = ['NOT A J', 'NOT B T', 'OR T J', 'NOT C T', 'OR T J', 'AND D J', 'WALK'][::-1]
	print(f"Part one: {springyboi.run_codes()}") # not 109, too low
	springierboi = Spring(DATA.copy())
	springierboi.all_inputs = ['NOT A J', 'NOT B T', 'OR T J', 'NOT C T', 'OR T J', 'OR J T', 'AND H J', 'OR E J', 'AND D J', 'AND T J', 'RUN'][::-1]
	print(f"Part two: {springierboi.run_codes()}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
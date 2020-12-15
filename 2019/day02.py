from typing import NamedTuple, List

class Computer(NamedTuple):
	codes: List
	
	def __repr__(self):
		return str(self.codes)

	def index_out(self, index: int) -> int:
		return self.codes[index]

	def __iadd__(self, other):
		self.codes[self.codes[other + 3]] = self.codes[self.codes[other + 1]] + self.codes[self.codes[other + 2]]
		return self

	def __imul__(self, other):
		self.codes[self.codes[other + 3]] = self.codes[self.codes[other + 1]] * self.codes[self.codes[other + 2]]
		return self

	def replace(self, index: int, new_num: int):
		self.codes[index] = new_num
		return self

def run_codes(comp):
	i = 0
	while True:
		# print(f"{comp}, i: {i}")
		opcode = comp.index_out(i)
		if opcode == 1:
			comp += i
			i += 4
		if opcode == 2:
			comp *= i
			i += 4
		if opcode == 99:
			return comp.index_out(0)

def test_codes(codes):
	x = y = 0
	while x < 99:
		while y < 99:
			comp = Computer(codes.copy())
			comp.replace(1, x)
			comp.replace(2, y)
			if run_codes(comp) == 19690720:
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
	OPLIST = Computer(CODES)
	OPLIST.replace(1, 12)
	OPLIST.replace(2, 2)
	print(f"Part one: {run_codes(OPLIST)}") # not 512, too low; not 29848, too low; -> 3716250 - forgot to read instructions properly
	print(f"Part two: {test_codes(BACKUP)}") # not 13600, too high; -> 6472 - interpreted math order of operations incorrectly
	print(f"Time: {timeit.timeit('test_codes(BACKUP)', setup='from __main__ import test_codes, BACKUP', number = 1)}")
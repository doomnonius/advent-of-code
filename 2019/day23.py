from typing import List
from day02 import Computer

class Network (Computer):
	def __init__(self, inst, inp: int):
		super().__init__(inst)
		self.inp = inp
		self.out = []
		self.queue = []
		self.address = None

	def output(self, data):
		if len(self.out) < 3:
			self.out.append(data)
		else:
			self.out = []
			self.out.append(data)
		return self

	def input(self):
		if type(self.address) != int:
			self.address = self.inp
			return self.inp
		try:
			if not self.queue[0]:
				self.queue.pop(0)
		except: ...
		if not self.queue:
			return -1
		return self.queue[0].pop(0)


	def run_codes(self, index_return = 0, at_index = 0):
		# needed to customize how to deal with input and output
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
				if not self.queue:
					return
			if opcode == 4:
				self.code4(p1)
				if len(self.out) == 3:
					return self.out
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


def part1(inst: List[int]):
	network = {x:Network(inst.copy(), x) for x in range(50)}
	while True:
		for comp in network.values():
			ret = "filler"
			while ret:
				ret = comp.run_codes()
				if ret:
					if ret[0] == 255:
						return ret[2]
					network[ret[0]].queue.append(ret[1:])

def part2(inst: List[int]):
	network = {x:Network(inst.copy(), x) for x in range(50)}
	nat = []
	count = 0
	repeats = 0
	last_nat_y = "filler"
	while True:
		prev_count = count
		for comp in network.values():
			ret = "filler"
			while ret:
				ret = comp.run_codes()
				if ret:
					count += 1
					if ret[0] == 255:
						nat = ret[1:]
					else: network[ret[0]].queue.append(ret[1:])
		if count == prev_count:
			repeats += 1
			if repeats > 3:
				network[0].queue.append(nat)
				if nat[1] == last_nat_y:
					return nat[1]
				last_nat_y = nat[1]
		else:
			repeats = 0


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day23.input")) as f:
		DATA = f.read().strip()
	DATA = [int(x) for x in DATA.split(",")]
	print(f"Part one: {part1(DATA.copy())}")
	print(f"Part two: {part2(DATA.copy())}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
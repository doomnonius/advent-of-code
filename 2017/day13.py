from typing import List
from copy import deepcopy
import math

class Layer:
	def __init__(self, data) -> None:
		depth, rng = data.split(": ")
		self.depth = int(depth)
		self.range = int(rng)
		self.loc = 1
		self.down = True
		self.cycle = (self.range - 1) * 2

	def move(self):
		if self.down and self.loc < self.range:
			self.loc += 1
		elif self.down:
			self.down = False
			self.loc -= 1
		elif not self.down and self.loc > 1:
			self.loc -= 1
		else:
			self.down = True
			self.loc += 1
		return self

	def unsafe(self, delay) -> bool:
		return (delay + self.depth) % self.cycle == 0

	def __repr__(self) -> str:
		return f"Depth: {self.depth}; range: {self.range}; loc: {self.loc}"

def part1(inp: List[Layer]) -> int:
	retVal = 0
	pos = 0
	depths = [x.depth for x in inp]
	layers = {x:y for x,y in zip(depths, inp)}
	end = max(depths)
	while pos <= end:
		# check here if in same spot
		if pos in depths:
			column = layers[pos]
			if column.loc == 1:
				retVal += column.depth * column.range
		for layer in inp:
			layer.move()
		pos += 1
	return retVal

def part2(inp: List[Layer]) -> int:
	delay = 0
	step = 1
	while True:
		count = 0
		for layer in inp:
			if layer.unsafe(delay):
				delay += step
				count += 1
			if layer.cycle == 2:
				step = 2
		if count == 0:
			print(f"Part two: {delay}")
			return delay

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day13.input")) as f:
		RAW_DATA = f.read().strip()
	DATA = [Layer(x) for x in RAW_DATA.split("\n")]
	# print(DATA)
	print(f"Part one: {part1(DATA)}") # not 6912, too high; 3322 also too high; poor use of if/else in Layer.move()
	# print(f"Part two: {part2(DATA)}")
	print(f"Time: {timeit.timeit('part2(DATA)', setup='from __main__ import part2, DATA', number = 10)}")
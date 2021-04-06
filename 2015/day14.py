from typing import List


class Reindeer:
	def __init__(self, data) -> None:
		split = data.split()
		self.name = split[0]
		self.speed = int(split[3])
		self.time = int(split[6])
		self.rest = int(split[-2])
		self.loc = 0
		self.score = 0

	def resting(self, time) -> bool:
		cycle = self.time + self.rest
		return time % cycle >= self.time


def part1(inp: List[Reindeer], cycles: int) -> int:
	i = 0
	while i < cycles:
		for x in inp:
			if not x.resting(i):
				x.loc += x.speed
		i += 1
	return max(x.loc for x in inp)


def part2(inp: List[Reindeer], cycles: int) -> int:
	i = 0
	while i < cycles:
		for x in inp:
			if not x.resting(i):
				x.loc += x.speed
		i += 1
		lead = max(x.loc for x in inp)
		for x in inp:
			if x.loc == lead:
				x.score += 1
	return max(x.score for x in inp)


TEST_DATA = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day14.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	REINDEER = [Reindeer(x) for x in DATA]
	print(f"Part one: {part1(REINDEER, 2503)}")
	print(f"Part two: {part2([Reindeer(x) for x in DATA], 2503)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
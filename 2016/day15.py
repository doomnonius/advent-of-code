from typing import List
import math


class Disc:
	def __init__(self, inp: str) -> None:
		split = inp.split()
		self.id = int(split[1][1:])
		self.positions = int(split[3])
		self.pos = int(split[-1][:-1])

	def valid_ts(self, time: int) -> bool:
		return (time + self.pos + self.id) % self.positions == 0

def part1(inp: List[Disc]) -> int:
	timestamp = 0
	step = 1
	for disc in inp:
		while not disc.valid_ts(timestamp):
			timestamp += step
		# print(f"before: {step}")
		step = (step * disc.positions) // math.gcd(step, disc.positions)
		# print(f"after: {step}")
	return timestamp


if __name__ == "__main__":
	import timeit
	DATA = """Disc #1 has 7 positions; at time=0, it is at position 0.
Disc #2 has 13 positions; at time=0, it is at position 0.
Disc #3 has 3 positions; at time=0, it is at position 2.
Disc #4 has 5 positions; at time=0, it is at position 2.
Disc #5 has 17 positions; at time=0, it is at position 0.
Disc #6 has 19 positions; at time=0, it is at position 7."""
	DATA = [Disc(x) for x in DATA.split('\n')]
	print(f"Part one: {part1(DATA)}") # not 192997, too high; not 192996, too high; 
	print(f"Part two: {part1(DATA + [Disc('Disc #7 has 11 positions; at time=0, it is at position 0.')])}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
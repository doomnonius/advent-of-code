
TEST_DATA = "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"

def part1(inp: str) -> str:
	retVal = ''
	inp = list(inp)[::-1]
	while len(inp) > 0:
		next_char = inp.pop()
		if next_char == "(":
			inst = ''
			while (n := inp.pop()) != ")":
				inst += n
			count, repeat = [int(x) for x in inst.split('x')]
			excerpt = ''
			for _ in range(count):
				excerpt += inp.pop()
			for _ in range(repeat):
				retVal += excerpt
		else:
			retVal += next_char
	return retVal


def part2(inp: str) -> str:
	retVal = 0
	inp = list(inp)[::-1]
	while len(inp) > 0:
		next_char = inp.pop()
		if next_char == "(":
			inst = ''
			while (n := inp.pop()) != ")":
				inst += n
			count, repeat = [int(x) for x in inst.split('x')]
			excerpt = ''
			for _ in range(count):
				excerpt += inp.pop()
			excerpt = part2(excerpt)
			for _ in range(repeat):
				retVal += excerpt
		else:
			retVal += 1
	return retVal


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day09.input")) as f:
		DATA = f.read().strip()
	print(f"Part one: {len(part1(DATA))}") # not 3608, too low; forgot to change input file to day 9
	print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('part2(DATA)', setup='from __main__ import part2, DATA', number = 1)}")
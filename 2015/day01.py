def part2(inp: str) -> int:
	retVal = 1
	floor = 0
	for i in inp:
		if i == "(":
			floor += 1
		else:
			floor -= 1
		if floor < 0:
			return retVal
		retVal += 1


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day01.input")) as f:
		DATA = f.read().strip()
	UP = DATA.count('(')
	DOWN = DATA.count(')')
	print(f"Part one: {UP - DOWN}")
	print(f"Part two: {part2(DATA)}") # not 1784, too high; was 1783 - retVal increase in wrong spot
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
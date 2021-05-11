def part1(inp: str) -> int:
	i = 0
	retVal = 0
	while i < len(inp):
		if inp[i] == inp[(i + 1) % len(inp)]:
			retVal += int(inp[i])
		i += 1
	return retVal

def part2(inp: str) -> int:
	i = 0
	retVal = 0
	half = len(inp)//2
	while i < len(inp):
		if inp[i] == inp[(i + half) % len(inp)]:
			retVal += int(inp[i])
		i += 1
	return retVal


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day01.input")) as f:
		DATA = f.read().strip()
	TEST_DATA = "12131415"
	print(f"Part one: {part1(DATA)}")
	print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
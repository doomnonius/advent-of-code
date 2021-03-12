

def part1(inp: str) -> int:
	i = 0
	score = 0
	retVal = 0
	open_angle = False
	while i < len(inp):
		char = inp[i]
		if not open_angle:
			if char == "{":
				score += 1
			elif char == "<":
				open_angle = True
			elif char == "}":
				retVal += score
				score -= 1
		else:
			if char == ">":
				open_angle = False
			elif char == "!":
				i += 1
		i += 1
	return retVal


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day09.input")) as f:
		DATA = f.read().strip()
	TEST_DATA = "{{<a!>},{<a!>},{<a!>},{<ab>}}"
	# print(DATA)
	print(f"Part one: {part1(DATA)}")
	# print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
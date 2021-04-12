def part1(inp: tuple, initial: int) -> int:
	pos = 1
	target = findPos(inp[0], inp[1])
	for x in codeGenerator(initial):
		pos += 1
		if pos == 2:
			assert x == 31916031, f"Incorrect result {x}!"
		if pos == target:
			return x


def findPos(row: int, column: int):
	row_start = row + column - 2
	return ((row_start**2 + row_start) // 2) + column


def codeGenerator(inp: int) -> int:
	while True:
		inp *= 252533
		inp %= 33554393
		yield inp



if __name__ == "__main__":
	import timeit
	DATA = "To continue, please consult the code grid in the manual.  Enter the code at row 2947, column 3029."
	DATA = (2947, 3029)
	INIT = 20151125
	print(f"Part one: {part1(DATA, INIT)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
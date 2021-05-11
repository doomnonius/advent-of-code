def part1(inp: str, rows) -> int:
	retVal = 0
	l = len(inp)
	while rows > 0:
		retVal += inp.count(".")
		next_row = ''
		for i in range(l):
			skip_l = False
			skip_r = False
			c = 0
			left = i - 1
			right = i + 1
			if left < 0:
				skip_l = True
			if right >= l:
				skip_r = True
			if not skip_l and inp[left] == "^":
				c += 1
			if not skip_r and inp[right] == '^':
				c += 1
			if c == 1:
				next_row += "^"
			else:
				next_row += "."
		assert len(next_row) == len(inp), f"next row incomplete, {len(inp) - len(next_row)} missing"
		# print(inp)
		inp = next_row
		rows -= 1
	return retVal


if __name__ == "__main__":
	import timeit
	DATA = "^^^^......^...^..^....^^^.^^^.^.^^^^^^..^...^^...^^^.^^....^..^^^.^.^^...^.^...^^.^^^.^^^^.^^.^..^.^"
	ROWS = 40
	# DATA = ".^^.^.^^^^"
	# ROWS = 10
	print(f"Part one: {part1(DATA, ROWS)}")
	print(f"Part two: {part1(DATA, 400000)}")
	# print(f"Time: {timeit.timeit('part1(DATA, LENGTH2)', setup='from __main__ import DATA, LENGTH2, part1', number = 1)}")
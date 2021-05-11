def part1(inp: str, cycles: int) -> int:
	while cycles > 0:
		inp = lookSay(inp)
		cycles -= 1
	return len(inp)


def lookSay(inp: str) -> str:
	last_char = ''
	retVal = ''
	c = 1
	for i in range(len(inp) + 1):
		try:
			curr_char = inp[i]
		except:
			curr_char = ''
		if curr_char == last_char:
			c += 1
		elif last_char != '':
			retVal += str(c)
			retVal += last_char
			c = 1
		last_char = curr_char
	return retVal


if __name__ == "__main__":
	import timeit
	DATA = "1113122113"
	print(f"Part one: {part1(DATA, 40)}")
	print(f"Part two: {part1(DATA, 50)}") # 6.57 sec
	# print(f"Time: {timeit.timeit('part1(DATA, 50)', setup='from __main__ import part1, DATA', number = 1)}")
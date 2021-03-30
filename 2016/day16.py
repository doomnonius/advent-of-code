def part1(inp: str, target: int) -> str:
	while len(inp) < target:
		inp += "0" + inverse(inp[::-1])
	inp = condense(inp[:target])
	return inp
	
def condense(inp: str) -> str:
	while len(inp) % 2 == 0:
		new_inp = ''
		h = len(inp) // 2
		for x in range(h):
			pair = inp[x*2:(x+1)*2]
			if pair[0] == pair[1]:
				new_inp += '1'
			else:
				new_inp += '0'
		inp = new_inp
	return inp


def inverse(inp: str) -> str:
	retVal = ''
	opps = {'0': '1', '1': '0'}
	for char in inp:
		retVal += opps[char]
	return retVal


if __name__ == "__main__":
	import timeit
	DATA = "11110010111001001"
	LENGTH1 = 272
	LENGTH2 = 35651584
	print(f"Part one: {part1(DATA, LENGTH1)}")
	print(f"Part two: {part1(DATA, LENGTH2)}") # fairly slow, ~ 50s
	# print(f"Time: {timeit.timeit('part1(DATA, LENGTH2)', setup='from __main__ import DATA, LENGTH2, part1', number = 1)}")
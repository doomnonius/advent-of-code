def part1(inp: int) -> int:
	retVal = []
	locs = [0] * (inp // 10)
	locs2 = [0] * (inp // 10)
	for i in range(1, inp // 10):
		visited = 0
		for j in range(i, inp // 10, i):
			if visited <= 50:
				locs2[j] += 11 * i
				visited += 1
			locs[j] += i * 10
	for x in locs:
		if x > inp:
			retVal.append(locs.index(x))
			break
	for x in locs2:
		if x > inp:
			retVal.append(locs2.index(x))
			break
	return retVal


if __name__ == "__main__":
	import timeit
	DATA = 29000000
	p1, p2 = part1(DATA)
	print(f"Part one: {p1}") # didn't read carefully, thought I was looking for equal, not greater than; also stole Peter's algo, it was just better than mine
	print(f"Part two: {p2}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
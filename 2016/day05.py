import hashlib


def part1(inp: str) -> str:
	retVal = ''
	i = 0
	while len(retVal) < 8:
		key = inp + str(i)
		hsh = hashlib.md5(key.encode('utf-8')).hexdigest()
		if hsh[0:5] == "00000":
			retVal += hsh[5]
		i += 1
	return retVal


def part2(inp: str) -> str:
	retVal = ['.','.','.','.','.','.','.','.']
	i = 0
	while '.' in retVal:
		key = inp + str(i)
		hsh = hashlib.md5(key.encode('utf-8')).hexdigest()
		if hsh[0:5] == "00000" and 0 <= int(hsh[5], 16) < 8:
			if retVal[int(hsh[5])] == '.':
				retVal[int(hsh[5])] = hsh[6]
		i += 1
	return ''.join(retVal)


if __name__ == "__main__":
	import timeit
	DATA = "reyedfim"
	# DATA = "abc"
	# print(DATA)
	print(f"Part one: {part1(DATA)}")
	print(f"Part two: {part2(DATA)}") # not e635d627; added check so it only grabs the first match for each index
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
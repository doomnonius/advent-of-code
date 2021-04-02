import hashlib


def part1(inp: str) -> int:
	i = 1
	key = inp + str(i)
	hsh = hashlib.md5(key.encode('utf-8')).hexdigest()
	while hsh[0:5] != "00000":
		i += 1
		key = inp + str(i)
		hsh = hashlib.md5(key.encode('utf-8')).hexdigest()
	return i


def part2(inp: str) -> int:
	i = 1
	key = inp + str(i)
	hsh = hashlib.md5(key.encode('utf-8')).hexdigest()
	while hsh[0:6] != "000000":
		i += 1
		key = inp + str(i)
		hsh = hashlib.md5(key.encode('utf-8')).hexdigest()
	return i


if __name__ == "__main__":
	import timeit
	DATA = "ckczppom"
	print(f"Part one: {part1(DATA)}")
	print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
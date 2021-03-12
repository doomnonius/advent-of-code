from typing import List
from functools import reduce

def part1(lengths: List[int], l: List[int], i = 0, skip = 0) -> int:
	l_leng = len(l)
	for leng in lengths:
		total = i + leng
		if total <= l_leng:
			if i == 0:
				l[i:total] = l[total-1:i:-1] + [l[i]]
			else:
				l[i:total] = l[total-1:i-1:-1]
		else:
			diff = total - l_leng
			to_rev = l[i:] + l[:diff]
			assert len(to_rev) == leng, f"to_rev ({len(to_rev)}) is not the correct length ({leng})"
			to_rev = to_rev[::-1]
			l[:diff] = to_rev[leng-diff:]
			l[i:] = to_rev[:leng-diff]
		assert len(l) == l_leng, f"l has shrunk to {len(l)} after length {leng}!"
		i = (total + skip) % l_leng
		skip += 1
	return l[0] * l[1], l, i, skip

def part2(lengths: str, l: List[int], suffix: List[int]) -> str:
	# step zero, declare variables
	full_lengths = []
	i = 0
	skip = 0
	# step one, convert lengths to ascii
	for char in lengths:
		full_lengths.append(ord(char))
	# step two, add suffix
	full_lengths.extend(suffix)
	# step three, run it 64 times (may be able to call a modified part1 for this)
	for _ in range(64):
		z, l, i, skip = part1(full_lengths, l, i = i, skip = skip)
	# step four, create a dense hash
	dense = []
	for x in range(16):
		start = 16 * x
		end = 16 * (x+1)
		assert len(l[start:end]) == 16, "sublist is incorect length"
		dense.append(reduce(lambda x, y: x ^ y, l[start:end]))
	# step five, return 32 char hexadecimal hash
	retVal = ''
	for c in dense:
		r = hex(c)[2:]
		if len(r) == 1:
			r = "0" + r
		retVal += r
	assert len(retVal) == 32, f"retVal is {len(retVal)} characters long"
	return retVal

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day10.input")) as f:
		RAW_DATA = f.read().strip()
	DATA = [int(x) for x in RAW_DATA.split(",")]
	SUFFIX = [17, 31, 73, 47, 23]
	BASIC_LIST = list(range(256))
	print(f"Part one: {part1(DATA, BASIC_LIST.copy())[0]}")
	print(f"Part two: {part2(RAW_DATA, BASIC_LIST, SUFFIX)}") # not be91062a680f581bd5f9754b9adae590; I forgot how lists work again
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
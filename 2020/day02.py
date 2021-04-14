import re
from typing import List


def part1(inp: List[str]) -> int:
	search_str = r'(\d+)-(\d+)\s(\w):\s(\w+)'
	valid = 0

	for x in inp:
		ret = re.search(search_str, x)
		mini = int(ret.group(1))
		maxi = int(ret.group(2))
		char = ret.group(3)
		pw = ret.group(4)
		if mini <= pw.count(char) <= maxi:
			valid += 1
	return valid


def part2(inp: List[str]) -> int:
	search_str = r'(\d+)-(\d+)\s(\w):\s(\w+)'
	valid = 0

	for x in inp:
		ret = re.search(search_str, x)
		mini = int(ret.group(1))
		maxi = int(ret.group(2))
		char = ret.group(3)
		pw = ret.group(4)
		if ((pw[mini-1] == char) + (pw[maxi-1] == char)) == 1:
			valid += 1
	return valid


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day02.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	print(f"Part one: {part1(DATA)}")
	print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
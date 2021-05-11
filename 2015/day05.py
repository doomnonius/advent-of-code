from typing import List
import re

two_pair = re.compile(r"([a-z])\1")
one_two_one = re.compile(r"([a-z])[a-z]\1")
repeat_pair = re.compile(r"([a-z])([a-z]).*\1\2")

def part1(inp: List[str]) -> int:
	nice = 0
	pat2 = ['ab', 'cd', 'pq', 'xy']
	for line in inp:
		if (sum(1 for x in two_pair.finditer(line))) and (len([x for x in pat2 if x in line]) == 0) and (len([x for x in line if x in 'aeiou']) > 2):
			nice += 1
	return nice


def part2(inp: List[str]) -> int:
	nice = 0
	for line in inp:
		if sum(1 for x in one_two_one.finditer(line)) and sum(1 for x in repeat_pair.finditer(line)):
			nice += 1
	return nice


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day05.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	print(f"Part one: {part1(DATA)}") # not 167, too low; not 577, too high; 
	print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
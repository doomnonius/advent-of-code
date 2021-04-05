import re, codecs
from typing import List

ascii_check = re.compile(r'\\x[0-9a-f]{2}')
slash_quote = re.compile(r'\\"')
slash_slash = re.compile(r'\\\\')


def part1(inp: List[str]) -> int:
	count = 0
	for line in inp:
		for _ in line:
			count += 1
	return count - sum(len(codecs.decode(x[1:-1], 'unicode_escape')) for x in inp)


def part2(inp: List[str]) -> int:
	char_count = encoded_count = 0
	for line in inp:
		for char in line:
			char_count += 1
			encoded_count += 1
			if char == '"':
				encoded_count += 1
			elif char == '\\':
				encoded_count += 1
		encoded_count += 2
		# print(encoded_count)
	return encoded_count - char_count


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day08.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	# DATA = [r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"']
	# print([len(x[1:-1]) for x in DATA])
	print(f"Part one: {part1(DATA)}")
	print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
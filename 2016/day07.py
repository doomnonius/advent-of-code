from typing import List


def part1(inp: List[str]) -> int:
	retVal = 0
	for line in inp:
		cond1 = True # no patt in brackets
		cond2 = False # patt outside brackets
		line = line.replace("]", "[")
		splits = line.split("[")
		bracket = splits[1::2]
		no_bracket = splits[0::2]
		for brack in bracket:
			if containsPatt1(brack):
				cond1 = False
				break
		for sub in no_bracket:
			if containsPatt1(sub):
				cond2 = True
		if cond1 and cond2:
			retVal += 1
	return retVal


def part2(inp: List[str]) -> int:
	retVal = 0
	for line in inp:
		cond1 = False # no patt in brackets
		cond2 = False # patt outside brackets
		line_mod = line.replace("]", "[")
		splits = line_mod.split("[")
		no_bracket = splits[0::2]
		bracket = splits[1::2]
		hits = []
		for sub in no_bracket:
			res = containsPatt2(sub)
			if res[0]:
				hits += res[1]
				cond2 = True
		for brack in bracket:
			for tup in hits:
				res2 = containsPatt2(brack, tup)
				if res2[0]:
					print(line)
					cond1 = True
					break
		if cond1 + cond2 == 2:
			retVal += 1
	return retVal


def containsPatt1(inp: str) -> bool:
	for i in range(len(inp) - 3):
		if inp[i] == inp[i+3] and inp[i] != inp[i+1] and inp[i+1] == inp[i+2]:
			return True
	return False

def containsPatt2(inp: str, chars = False) -> tuple:
	retVal = []
	if not chars:
		for i in range(len(inp) - 2):
			if inp[i] == inp[i+2] and inp[i] != inp[i+1]:
				retVal.append((inp[i], inp[i+1]))
	else:
		for i in range(len(inp) - 2):
			if inp[i] == chars[1] and inp[i] == inp[i+2] and inp[i+1] == chars[0]:
				return (True, retVal)
	if retVal:
		return (True, retVal)
	return (False, retVal)


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day07.input")) as f:
		RAW_DATA = f.read().strip()
	DATA = RAW_DATA.split("\n")
	print(f"Part one: {part1(DATA)}")
	print(f"Part two: {part2(DATA)}") # not 119, too low; not 163, too low; was stopping early in line 35, not finding all aba patterns
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
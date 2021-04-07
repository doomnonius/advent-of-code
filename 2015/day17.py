from typing import Dict, List


def part1(inp: List[str], vol: int, b: List[int], vals: Dict[int, int]) -> int:
	built = b.copy()
	retVal = 0
	l = len(inp)
	if l == 0:
		return 0
	for i in range(l):
		item = inp[0]
		built.append(item)
		if sum(built) < vol:
			retVal += part1(inp[1:], vol, built.copy(), vals)
		elif sum(built) == vol:
			retVal += 1
			if len(built) not in vals:
				vals[len(built)] = 0
			vals[len(built)] += 1
			built = built[:-1]
		built = b.copy()
		inp = inp[1:]
	return retVal


TEST_DATA = """20
15
10
5
5"""


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day17.input")) as f:
		DATA = f.read().strip()
	DATA = [int(x) for x in DATA.split("\n")]
	DATA.sort(reverse=True)
	TEST_DATA = [int(x) for x in TEST_DATA.split("\n")]
	VALS = {}
	print(f"Part one: {part1(DATA, 150, [], VALS)}")
	print(f"Part two: {VALS[min(VALS.keys())]}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
from typing import List


def amazing_formula(map: List[str]):
	pass

TEST_DATA = """
#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################"""

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day18.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	TEST_DATA = TEST_DATA.split("\n")[1:]
	print(f"Part one: {TEST_DATA}")
	# print(f"Part two: {}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
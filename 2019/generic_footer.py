if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day\\.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	print(f"Part one: {DATA}")
	# print(f"Part two: {min(steps(x, WIRE1, WIRE2) for x in WIRE1.overlap(WIRE2))}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
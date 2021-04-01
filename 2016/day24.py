










if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day24.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	print(f"Part one: {part1(DATA)}")
	# print(f"Part two: {}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
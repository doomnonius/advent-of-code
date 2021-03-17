



if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day16.input")) as f:
		RAW_DATA = f.read().strip()
	DATA = RAW_DATA.split(",")
	# print(DATA)
	# print(f"Part one: {part1(DATA)}")
	# print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('part2(DATA)', setup='from __main__ import part2, DATA', number = 10)}")
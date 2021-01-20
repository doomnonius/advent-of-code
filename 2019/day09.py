from day02 import Computer

TEST_DATA = """109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"""

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day09.input")) as f:
		DATA = f.read().strip()
	DATA = [int(x) for x in DATA.split(",")]
	TEST_DATA = [int(x) for x in TEST_DATA.split(",")]
	print(f"Part one: {Computer(DATA.copy(), inp=[1]).run_codes()}")
	print(f"Part two: {Computer(DATA.copy(), inp=[2]).run_codes()}")
	print(f"Time: {timeit.timeit('Computer(DATA.copy(), inp=[2]).run_codes()', setup='from __main__ import Computer, DATA', number = 1)}")
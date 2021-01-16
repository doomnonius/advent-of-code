from day02 import Computer
import itertools

TEST_DATA = """3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"""

def calc_max_thrust(data):
	m = 0
	for var in itertools.permutations([0,1,2,3,4], 5):
		n = out = 0
		for num in var:
			run = Computer(data.copy()).noun(out) # this shouldn't actually be a noun, but an input -> change how input works
			run.input_data = num
			print(run)
			out = run.run_codes()
			n += out
			print("Ding!")
		if n > m:
			m = n
	return m

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day07.input")) as f:
		DATA = f.read().strip()
	DATA = [int(x) for x in DATA.split(",")]
	TEST_DATA = [int(x) for x in TEST_DATA.split(",")]
	print(f"Part one: {calc_max_thrust(TEST_DATA.copy())}")
	# print(f"Part two: {}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
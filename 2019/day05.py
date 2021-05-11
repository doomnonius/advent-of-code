from day02 import Computer

TEST_DATA = """3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"""

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day05.input")) as f:
		DATA = f.read().strip()
	DATA = [int(x) for x in DATA.split(",")]
	p1 = Computer(DATA.copy(), inp=[1])
	while p1.run_codes() == 0:
		p1.run_codes()
	print(f"Part one: {p1.out}")
	print(f"Part two: {Computer(DATA, inp=[5]).run_codes()}") # not 9234535, too high; 
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
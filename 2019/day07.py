from day02 import Computer
import itertools

TEST_DATA = """3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"""

def calc_max_thrust(data):
	m = 0
	for var in itertools.permutations([0,1,2,3,4], 5):
		# print(f"Arrangement: {var}")
		out = 0
		for num in var:
			inputs = [num, out]
			run = Computer(data.copy(), inp=inputs) # this shouldn't actually be a noun, but an input -> change how input works
			# print(run.input_list)
			out = run.run_codes()
			# print(f"Run: {run}")
			# print(f"Out: {out}")
			# print("Ding!")
		if out > m:
			m = out
	return m

def calc_max_thrust_feedback(data):
	m = 0
	for var in itertools.permutations(range(5,10), 5):
		# print(f"Arrangement: {var}")
		out = 0
		amps = []
		# initialize
		for i in range(len(var)):
			inputs = [var[i], out]
			run = Computer(data.copy(), inp=inputs)
			out = run.run_codes()
			amps.append(run)
		i = 0
		while not amps[4].done:
			amps[i].input_list = [out]
			out = amps[i].run_codes()
			if i < 4: i += 1
			else: i = 0
		if out > m:
			m = out
	return m

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day07.input")) as f:
		DATA = f.read().strip()
	DATA = [int(x) for x in DATA.split(",")]
	TEST_DATA = [int(x) for x in TEST_DATA.split(",")]
	print(f"Part one: {calc_max_thrust(DATA.copy())}")
	print(f"Part two: {calc_max_thrust_feedback(DATA.copy())}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
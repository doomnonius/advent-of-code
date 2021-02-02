from day02 import Computer
import itertools, sys

def combos(inst):
	retVal = 0
	for x in itertools.product(range(0, 50), repeat=2):
		drone = Computer(inst.copy())
		drone.input_list = list(x)
		retVal += drone.run_codes()
	# return sum(Drone(inst).input_list(x).run_codes() for x in itertools.product(range(0, 50), repeat=2))
	return retVal

def hundreds(inst):
	attempts = {}
	row = 250
	while True:
		check_x = check_y = 0
		# print(f"Row: {row}")
		if row not in attempts.keys():
			attempts[row] = ""
		else:
			if row + 1 in attempts.keys():
				# print(f"check_y: {check_y}")
				return first_x * 10000 + row + 1
			else:
				# print(f"check_y: {check_y}")
				return first_x * 10000 + row
		hit = False
		for x in range(sys.maxsize):
			drone = Computer(inst.copy())
			drone.input_list = [x, row]
			last_x = check_x
			check_x += drone.run_codes()
			if check_x > 0 and not hit:
				hit = True
			if last_x == check_x and hit:
				# print(f"check_x: {check_x}")
				save = x
				break
		first_x = save - 100
		save_row = row
		for y in range(105):
			drone = Computer(inst.copy())
			drone.input_list = [first_x, row + y]
			if drone.run_codes() == 0 and check_y < 100:
				# print(f"check_y: {check_y}")
				if check_y < 100:
					row += 100 - check_y
				else: row += 1
				break
			else: check_y += 1
		if check_y > 100:
			# print(f"check_y: {check_y}")
			return first_x * 10000 + save_row
		if check_y == 100:
			# print(f"check_y: {check_y}")
			return first_x * 10000 + save_row
		
	

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day19.input")) as f:
		DATA = f.read().strip()
	DATA = [int(x) for x in DATA.split(",")]
	print(f"Part one: {combos(DATA)}")
	print(f"Part two: {hundreds(DATA)}") # not 10750671, too high; not 6711074, too low; not 6741081, too low; 
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
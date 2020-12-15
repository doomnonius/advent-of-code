def memory_game(stop_point: int, *numbers):
	nums = {}
	i = 0
	for x in numbers:
		if x in numbers[0:-1]:
			nums[x] = i
		i += 1
		last_num = x
	while i < stop_point:
		prev_num = last_num
		if last_num in nums.keys():
			diff = i-nums[last_num]-1
			last_num = diff 
		else:
			last_num = 0
		nums[prev_num] = i-1
		i += 1
	return last_num
	
TEST_DATA = """1,3,2"""

if __name__ == "__main__":
	import os, datetime, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day15.input")) as f:
		DATA = f.read().strip()
	DATA = [int(x) for x in DATA.split(",")]
	print(f"Part one: {memory_game(2020, *DATA)}")
	print(f"Part two: {memory_game(30000000, *DATA)}")
	# print(f"Timed: {timeit.timeit('memory_game(30000000, *DATA)', setup='from __main__ import DATA, memory_game', number=1)}")
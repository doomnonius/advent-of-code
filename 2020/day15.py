from typing import List, Dict

def memory_game(numbers: List[int], stop_point: int):
	nums = {}
	i = 0
	while i < len(numbers)-1:
		nums[numbers[i]] = i
		i += 1
	while i < stop_point:
		if numbers[i] in nums.keys() and nums[numbers[i]] != None: # if it exists:
			diff = i-nums[numbers[i]]
			numbers.append(diff) # next num is difference
			nums[numbers[i]] = i # update last occurence
		else: # if it doesn't:
			numbers.append(0) # append 0
			nums[numbers[i]] = i
			if 0 in nums.keys():
				if nums[0] == None:
					nums[0] = i # update last occurence
			else:
				nums[0] = None
		i += 1
	return numbers[-2]
	
TEST_DATA = """3,1,2"""

if __name__ == "__main__":
	import os, datetime
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day15.input")) as f:
		DATA = f.read().strip()
	DATA = [int(x) for x in DATA.split(",")]
	print(f"Part one: {memory_game(DATA, 2020)}")
	print(datetime.datetime.now())
	print(f"Part one: {memory_game(DATA, 30000000)}")
	print(datetime.datetime.now())
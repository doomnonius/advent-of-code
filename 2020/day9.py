from typing import List

def find_exception(numbers: List[int]):
	i = 0
	while True:
		if check_previous(numbers[i:i+25], x := numbers[i+25]) == False:
			return x
		i += 1

def check_previous(numbers: List[int], last: int):
	for x in numbers:
		for y in numbers:
			if x + y == last and x != y:
				return True
	return False

def find_contiguous(numbers: List[int], exception):
	i = 0
	while True:
		x = numbers[i]
		l = [x]
		j = i
		while x < exception:
			j += 1
			x += numbers[j]
			l.append(numbers[j]) # had this incorrectly as x
		if x == exception:
			return min(l) + max(l)
		i += 1



if __name__ == "__main__":
	import os
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day9.input")) as f:
		DATA = f.read().strip()
	NUMBERS = [int(x) for x in DATA.split("\n")]
	print(f"Part one: {find_exception(NUMBERS)}")
	print(f"Part two: {find_contiguous(NUMBERS, find_exception(NUMBERS))}") # not 8228775, nor 74114375 (too high)
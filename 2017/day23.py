from typing import List
import math


def part1(inp: List[str]) -> int:
	retVal = 0
	registers = {}
	l = len(inp)
	index = 0
	while 0 <= index < l:
		line = inp[index].split()
		if not isNumber(line[1]) and line[1] not in registers.keys(): registers[line[1]] = 0
		if len(line) == 3:
			if isNumber(line[2]):
				line[2] = int(line[2])
			else:
				if line[2] not in registers.keys(): registers[line[2]] = 0
				line[2] = registers[line[2]]
		if line[0] == "set":
			registers[line[1]] = line[2]
		elif line[0] == "sub":
			registers[line[1]] -= line[2]
		elif line[0] == "mul":
			registers[line[1]] *= line[2]
			retVal += 1
		elif line[0] == "jnz":
			if isNumber(line[1]):
				line[1] = int(line[1])
			else:
				line[1] = registers[line[1]]
			if line[1] != 0:
				index += line[2]
				continue
		index += 1
		# print(registers)
	return retVal


def part2(inp: List[str]) -> int:
	# h is counting *not* primes b/t 107900 and 124900 (inclusive) at increments of 17;
	retVal = 0
	low = 107900
	high = 124900
	for n in range(107900, 124901, 17):
		if not isPrime(n):
			retVal += 1
	return retVal


def isPrime(n: int) -> bool:
	if n == 2:
		return True
	if n % 2 == 0 or n <= 1:
		return False

	sqr = int(math.sqrt(n)) + 1

	for divisor in range(3, sqr, 2):
		if n % divisor == 0:
			return False
	
	return True

def isNumber(val: str) -> bool:
	try:
		int(val)
	except ValueError:
		return False
	return True


if __name__ == "__main__":
	import os, datetime
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day23.input")) as f:
		RAW_DATA = f.read().strip()
	DATA = RAW_DATA.split('\n')
	print(f"Part one: {part1(DATA)}")
	print(f"Part two: {part2(DATA)}") # not 1000, too high; not 94; not 906, too low; 
	# print(f"Time: {timeit.timeit('part1(DATA, 18)', setup='from __main__ import part1, DATA', number = 1)}")
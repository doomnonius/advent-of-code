def part1(val_a: int, val_b: int) -> int:
	retVal = 0
	for _ in range(40000000):
		val_a = genA(val_a)
		val_b = genB(val_b)
		if val_a%65536 == val_b%65536:
			retVal += 1
	return retVal


def part2(val_a: int, val_b: int) -> int:
	retVal = 0
	for _ in range(5000000):
		while (val_a := genA(val_a)) % 4 != 0:
			continue
		while (val_b := genB(val_b)) % 8 != 0:
			continue
		if val_a%65536== val_b%65536:
			retVal += 1
	return retVal


def genA(value: int) -> int:
	factor = 16807
	return (value * factor) % 2147483647	
	

def genB(value: int) -> int:
	factor = 48271
	return (value * factor) % 2147483647


if __name__ == "__main__":
	import timeit
	DATA_A = 512
	DATA_B = 191
	print(f"Part one: {part1(DATA_A, DATA_B)}")
	# print(f"Time: {timeit.timeit('part1(DATA_A, DATA_B)', setup='from __main__ import part1, DATA_A, DATA_B', number = 1)}") # initial: 39, modulo changes: 37, using generator: 40, drop the conversion to binary: 18.19, !!! linq: 1.177 !!!
	print(f"Part two: {part2(DATA_A, DATA_B)}")
	# print(f"Time: {timeit.timeit('part2(DATA_A, DATA_B)', setup='from __main__ import part2, DATA_A, DATA_B', number = 1)}") # initial: 15, module changes: 15, using generator: wrong answer, drop conversion to binary: 13.29, !!! linq: 1.167 !!!
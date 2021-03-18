

def part1(steps: int) -> int:
	buffer = [0]
	index = 0
	for i in range(1, 2018):
		index = (index + steps) % i + 1 # i just happens to equal the length of the list in this situation
		buffer.insert(index, i)
		# if i < 10:
		# 	print(buffer)
	assert len(buffer) == 2018, "Buffer is not correct size"
	# print(buffer)
	return buffer[(buffer.index(2017) + 1) % len(buffer)]


def part2(steps: int) -> int:
	index = 0
	retVal = 0
	for i in range(1, 50000000):
		index = (index + steps) % i + 1 # i just happens to equal the length of the list in this situation
		# if i % 1000000 == 0:
		# 	print(f"Progress: {i // 1000000}/50")
		if index == 1:
			retVal = i
	# print(buffer)
	return retVal


if __name__ == "__main__":
	import timeit
	DATA = 324
	print(f"Part one: {part1(DATA)}") # not 2016, too high
	# print(f"Time: {timeit.timeit('part1(DATA_A, DATA_B)', setup='from __main__ import part1, DATA_A, DATA_B', number = 1)}")
	print(f"Part two: {part2(DATA)}") # peter's answer revealed that you don't need to keep the list - 0 is always at index 0, so just keep track of whatever would be in index 1 if you were actually keeping a list
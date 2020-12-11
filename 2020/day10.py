from typing import Set, List
import timeit

def jolting(jolts: List):
	i = 1
	diffs = []
	solids = [0]
	while i < len(jolts):
		diffs.append(jolts[i] - jolts[i-1])
		if jolts[i] - jolts[i-1] == 3:
			solids.extend([jolts[i-1], J[i]])
		i += 1
	ones = diffs.count(1)
	threes = diffs.count(3)
	return ones * threes, solids

def variations(jolts: List, threes: List):
	for i in range(len(jolts)):
		if jolts[i] in threes:
			jolts[i] = str(jolts[i])
	i = 0
	subsection = []
	count = 1
	while i < len(jolts):
		if type(jolts[i]) == str:
			subsection.append(int(jolts[i]))
			if len(subsection) > 1:
				count *= len(possibilities(subsection))
				subsection = [int(jolts[i])]
		else:
			subsection.append(jolts[i])
		i += 1
	return count

def possibilities(subset: List):
	""" First and last will be solids. Return a list.
	"""
	i = 1
	reset = subset.copy()
	options = [reset]
	while i < len(subset): # if diff between any two is greater than 3, return empty list
		if subset[i] - subset[i-1] > 3:
			return []
		i += 1
	if len(subset) == 2:
		return options
	i = 1
	l = len(subset)-1
	while i < l:
		subset.remove(subset[i])
		recursed = possibilities(subset)
		for arrangement in recursed:
			if arrangement not in options:
				options += [arrangement]
		i += 1
		subset = reset.copy()
	return options # need to return all the unique options


if __name__ == "__main__":
	import os
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day10.input")) as f:
		DATA = f.read().strip()
	JOLTAGES = [int(x) for x in DATA.split("\n")]
	J = [0] + sorted(JOLTAGES) + [max(JOLTAGES)+3]
	# print(J)
	j = jolting(J)
	print(f"Part one: {j[0]}") # not 1890, too low -> 1984
	print(f"Part two: {variations(J, j[1])}") #  first try! -> 3543369523456
	print(f"{timeit.timeit('variations(J, j[1])', setup= 'from __main__ import variations, J, j', number=1000)}") #0.2640735 for 1000 executions
from typing import Set, List

def jolting(jolts: List):
	i = 1
	diffs = []
	solids = [0]
	while i < len(J):
		diffs.append(J[i] - J[i-1])
		if J[i] - J[i-1] == 3:
			solids.extend([J[i-1], J[i]])
		i += 1
	ones = diffs.count(1)
	threes = diffs.count(3)
	return ones * threes, solids

def variations(jolts: List, threes: List): # so the threes are the "solid" points
	for i in range(len(jolts)):
		if jolts[i] in threes:
			jolts[i] = str(jolts[i])
	i = 0
	sub = []
	c = 1
	while i < len(jolts):
		# find all arrangements where there is never a difference of more than 3
		if type(jolts[i]) == str:
			sub.append(int(jolts[i]))
			if len(sub) > 1:
				c *= len(possibilities(sub))
				print(c)
				sub = [int(jolts[i])]
		else:
			sub.append(jolts[i])
		i += 1
	return c

def possibilities(subset: List):
	""" First and last will be solids. Return a list?
	"""
	i = 1
	options = [subset]
	print(f"subset: {subset}")
	while i < len(subset): # if diff between any two is greater than 3, return empty list
		if subset[i] - subset[i-1] > 3:
			return []
		i += 1
	if len(subset) == 2:
		return options
	reset = subset.copy()
	i = 1
	l = len(subset)-1
	while i < l:
		print(f"subset: {subset}")
		subset.remove(subset[i])
		options.extend(possibilities(subset))
		i += 1
		subset = reset.copy()
	return options # need to return all the unique options


if __name__ == "__main__":
	import os
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day10.input")) as f:
		# DATA = f.read().strip()
		pass
	DATA = """16
10
15
5
1
11
7
19
6
12
4"""
	JOLTAGES = [int(x) for x in DATA.split("\n")]
	J = [0] + sorted(JOLTAGES) + [max(JOLTAGES)+3]
	# print(J)
	j = jolting(J)
	print(f"Part one: {j[0]}") # not 1890, too low
	print(f"Part two: {variations(J, j[1])}")
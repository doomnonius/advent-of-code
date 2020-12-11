def run_code(rules):
	a = 0
	visited = [] # we always see the first index
	i = 0
	while True:
		if i in visited:
			# print(f"Visited: {visited}, i: {i}")
			return a, False
		visited.append(i)
		if i >= len(rules):
			return a, True
		x = rules[i]
		ins = x[0:3]
		num = x[4:]
		if ins == "acc":
			a += int(num)
			i += 1
		elif ins == "jmp":
			i += int(num)
		elif ins == "nop":
			i += 1

def make_alternates(inst):
	x = 0
	r = []
	while x < len(inst):
		y = inst[x]
		if y[0:3] == "nop":
			new = inst.copy()
			new[x] = "jmp" + inst[x][3:]
			r.append(new)
		elif y[0:3] == "jmp":
			new = inst.copy()
			new[x] = "nop" + inst[x][3:]
			r.append(new)
		x += 1

	return r # a list of lists

if __name__ == "__main__":
	import os
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day8.input")) as f:
		DATA = f.read().strip()
	INSTRUCTIONS = DATA.split("\n")
	print(f"Part one: {run_code(INSTRUCTIONS)[0]}")
	print(f"Part two: {[answer[0] for x in make_alternates(INSTRUCTIONS) if (answer := run_code(x))[1] == True][0]}")
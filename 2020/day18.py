def operations_ooo(equation: str, two=False) -> str:
	l = len(equation)
	if "(" not in equation:
		equation.replace(")", '')
		if two: return operations_p2(equation)
		return operations_p1(equation)
	p_loc = equation.index("(")
	pc_loc = p_match(equation, p_loc)
	if pc_loc + 1 == l:
		equation = equation[0:p_loc] + operations_ooo(equation[p_loc+1:pc_loc], two)
	else:
		equation = equation[0:p_loc] + operations_ooo(equation[p_loc+1:pc_loc], two) + equation[pc_loc+1:]
	return(operations_ooo(equation, two))


def p_match(equation, loc) -> int:
	""" Returns the index of the matching parenthesis.
	"""
	open_c = 0
	close_c = 0
	index = 0
	for char in equation:
		if char == "(":
			open_c += 1
		elif char == ")":
			close_c += 1
			if open_c == close_c:
				return index
		index += 1


def operations_p1(equation: str) -> str:
	parts = equation.split()
	retVal = parts[0]
	i = 1
	while i < len(parts):
		retVal = str(eval(retVal + parts[i] + parts[i+1]))
		i += 2
	return retVal


def operations_p2(equation: str) -> str:
	parts = equation.split()
	i = 1
	while (l := len(parts)) > 1:
		if i >= l:
			i = 1
		if parts[i] == "+":
			parts[i-1] = str(eval(parts[i-1] + parts.pop(i) + parts.pop(i))) # pop the same index twice
		elif parts[i] == "*" and "+" not in parts:
			parts[i-1] = str(eval(parts[i-1] + parts.pop(i) + parts.pop(i))) # pop the same index twice
		else:
			i += 2
	return parts[0]


print(f"{operations_ooo('2 * 3 + (4 * 5)', True)}") # p2 should be: 46
print(f"{operations_ooo('9 + 9 + (2 + 3 * 8)', True)}") # p2 should be: 58
print(f"{operations_ooo('5 + (8 * 3 + 9 + 3 * 4 * 3)', True)}") # p2 should be: 1445

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day18.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	print(f"Part one: {sum(int(operations_ooo(EQ)) for EQ in DATA)}")
	print(f"Part two: {sum(int(operations_ooo(EQ, True)) for EQ in DATA)}") # not 5783053342291, too low
	print(f"Time: {timeit.timeit('sum(int(operations_ooo(EQ, True)) for EQ in DATA)', setup='from __main__ import operations_ooo, DATA', number = 1)}") # 0.02
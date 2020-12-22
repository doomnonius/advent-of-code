def operations_ooo(equation: str) -> str:
	# print(equation)
	l = len(equation)
	if "(" not in equation:
		equation.replace(")", '')
		return operations_p1(equation)
	p_loc = equation.index("(")
	pc_loc = p_match(equation, p_loc)
	# print(f"open: {p_loc}; close: {pc_loc}")
	if pc_loc + 1 == l:
		equation = equation[0:p_loc] + operations_ooo(equation[p_loc+1:pc_loc])
	else:
		equation = equation[0:p_loc] + operations_ooo(equation[p_loc+1:pc_loc]) + equation[pc_loc+1:]
	return(operations_ooo(equation))


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
	# print(parts)
	retVal = parts[0]
	i = 1
	while i < len(parts):
		retVal = str(eval(retVal + parts[i] + parts[i+1]))
		i += 2
	# print(f"retVal: {retVal}")
	return retVal


def operations_p2(equation: str) -> str:
	parts = equation.split()



# print(f"{operations_ooo('3 * 4 + 2 + 7 + (4 * (9 + 9 + 2 + 3 * 8) + 9 + (6 + 4) + 7) + 3')}")
# print(f"{operations_ooo('9 + 9 + 2 + 3 * 8')}")
# print(f"{operations_ooo('(7 + 2 + (2 * 3)) * ((8 + 3 * 4 + 3 + 9 + 4) + 5) + 8 * 7 + 5 * 5')}")

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day18.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	print(f"Part one: {sum(int(operations_ooo(EQ)) for EQ in DATA)}")
	# print(f"Part two: {}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
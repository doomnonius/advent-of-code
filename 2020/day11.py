

def permutate(rows):
	m = len(rows)
	rl = len(rows[0])
	c = 0
	for row in range(m):
		adj_rows = [rows[row]]
		if row > 0: adj_rows = [rows[row-1]] + adj_rows
		else: adj_rows = [None] + adj_rows
		if row < m-1: adj_rows.append(rows[row+1])
		else: adj_rows.append(None)
		print(adj_rows)
		for seat in range(rl):
			if rows[row][seat] == ".":
				continue
			elif rows[row][seat] == "L" and count_adj(adj_rows, seat, rl) == 0:
				rows[row][seat] = "#"
				c += 1
			elif rows[row][seat] == "#" and count_adj(adj_rows, seat, rl) > 3:
				rows[row][seat] = "L"
				c -= 1
			elif rows[row][seat] == "#":
				c += 1
	return rows, c

def count_adj(rows, seat, row_length):
	""" rows in order of: revious row, current row, next row.
	"""
	filled = []
	if seat == 0:
		low = 0
	else:
		low = seat-1
	if seat == row_length:
		high = row_length + 1
	else:
		high = seat+2
	print(f"high: {high}, low: {low}")
	if rows[0] == None: pass
	else:
		filled.append([x for x in range(low, high) if rows[0][x] == "#"])
	if seat != high-1 and rows[1][high-1] == "#":
		filled.append("#")
	if seat != low and rows[1][low] == "#":
		filled.append("#")
	if rows[2] == None: pass
	else:
		filled.append([x for x in range(low, high) if rows[2][x] == "#"])
	return len(filled)

if __name__ == "__main__":
	import os
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day10.input")) as f:
		# DATA = f.read().strip()
		pass
	DATA = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
	ROWS = DATA.split("\n")
	print(f"Part one: {permutate(ROWS)}")
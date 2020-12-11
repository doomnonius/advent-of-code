import timeit

def game_o_life(rows):
	"""This will run permutate until we stabilize
	"""
	t = 0
	while True:
		t += 1
		new_seating, count = permutate(rows)
		if rows == new_seating:
			return count
		rows = new_seating.copy()
		# print(new_seating)
		# print(f"Run: {t}")

def permutate(rows):
	height = len(rows)
	width = len(rows[0])
	count = 0
	new_seating = []
	new_row = ""
	for row in range(height):
		adj_rows = [rows[row]]
		if row > 0: adj_rows = [rows[row-1]] + adj_rows
		else: adj_rows = [None] + adj_rows
		if row < height-1: adj_rows.append(rows[row+1])
		else: adj_rows.append(None)
		# print(adj_rows)
		for seat in range(width):
			# print(f"Seat: {seat}")
			if rows[row][seat] == ".":
				new_row += "."
			elif rows[row][seat] == "L" and count_seen(rows, row, seat, width, height) == 0:
				new_row += "#"
				count += 1
			elif rows[row][seat] == "#" and count_seen(rows, row, seat, width, height) > 4:
				new_row += "L"
				count -= 1
			elif rows[row][seat] == "#":
				new_row += "#"
				count += 1
			elif rows[row][seat] == "L":
				new_row += "L"
		new_seating.append(new_row)
		new_row = ""
	return new_seating, count

def count_seen(rows, row, seat, row_length, height):
	count = 0
	# check up-left
	nav_row = row
	nav_seat = seat
	while nav_row > 0 and nav_seat > 0:
		nav_row -= 1
		nav_seat -= 1
		if (spot := rows[nav_row][nav_seat]) != ".":
			if spot == "#":
				count += 1
			break
	# check up
	nav_row = row
	nav_seat = seat
	while nav_row > 0:
		nav_row -= 1
		if (spot := rows[nav_row][nav_seat]) != ".":
			if spot == "#":
				count += 1
			break
	# check up-right
	nav_row = row
	nav_seat = seat
	while nav_row > 0 and nav_seat < row_length-1:
		nav_row -= 1
		nav_seat += 1
		if (spot := rows[nav_row][nav_seat]) != ".":
			if spot == "#":
				count += 1
			break
	# check left
	nav_row = row
	nav_seat = seat
	while nav_seat > 0:
		nav_seat -= 1
		if (spot := rows[nav_row][nav_seat]) != ".":
			if spot == "#":
				count += 1
			break
	# check right
	nav_row = row
	nav_seat = seat
	while nav_seat < row_length-1:
		nav_seat += 1
		if (spot := rows[nav_row][nav_seat]) != ".":
			if spot == "#":
				count += 1
			break
	# check down-left
	nav_row = row
	nav_seat = seat
	while nav_row < height-1 and nav_seat > 0:
		nav_row += 1
		nav_seat -= 1
		if (spot := rows[nav_row][nav_seat]) != ".":
			if spot == "#":
				count += 1
			break
	# check down
	nav_row = row
	nav_seat = seat
	while nav_row < height-1:
		nav_row += 1
		if (spot := rows[nav_row][nav_seat]) != ".":
			if spot == "#":
				count += 1
			break
	# check down-right
	nav_row = row
	nav_seat = seat
	while nav_row < height-1 and nav_seat < row_length-1:
		nav_row += 1
		nav_seat += 1
		if (spot := rows[nav_row][nav_seat]) != ".":
			if spot == "#":
				count += 1
			break
	# print(count)
	return count

def count_adj(rows, seat, row_length):
	""" rows in order of: revious row, current row, next row.
	"""
	filled = []
	if seat == 0:
		low = 0
	else:
		low = seat-1
	if seat == row_length-1:
		high = row_length
	else:
		high = seat+2
	# print(f"high: {high}, low: {low}")
	if rows[0] == None: pass
	else:
		filled.extend([x for x in range(low, high) if rows[0][x] == "#"])
	if seat != high-1 and rows[1][high-1] == "#":
		filled.append("#")
	if seat != low and rows[1][low] == "#":
		filled.append("#")
	if rows[2] == None: pass
	else:
		filled.extend([x for x in range(low, high) if rows[2][x] == "#"])
	# print(f"Seat: {seat}, num_adj_filled: {filled}")
	return len(filled)

if __name__ == "__main__":
	import os
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day11.input")) as f:
		DATA = f.read().strip()
	ROWS = DATA.split("\n")
	# print(f"Part one: {game_o_life(ROWS)}") # -> 2178
	print(f"Part two: {game_o_life(ROWS)}") # -> 1978
	print(f"{timeit.timeit('game_o_life(ROWS)', setup='from __main__ import game_o_life, ROWS', number=1)}") # -> 0.949
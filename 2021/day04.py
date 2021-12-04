from typing import List

def part1(picks: List[int], boards: List[List[int]]) -> int:
	for pick in picks:
		for board in boards:
			if pick in board:
				board[board.index(pick)] = -1
				if board.count(-1) >= 5:
					# check if those five form a row
					if row_complete(board):
						return sum(x for x in board if x > 0) * pick

def row_complete(board: List[int]) -> bool:
	# rows
	for row in range(5):
		low = row * 5
		if sum(board[low:low+5]) == -5:
			print(f"Row: {row}")
			return True
	# columns
	for column in range(5):
		if sum(board[column::5]) == -5:
			print(f"Column: {column}")
			return True
	return False


def part2(picks: List[int], boards: List[List[int]]) -> int:
	total = len(boards)
	solved = set()
	for pick in picks:
		for board in boards:
			if boards.index(board) not in solved and pick in board:
				board[board.index(pick)] = -1
				if board.count(-1) >= 5:
					# check if those five form a row
					if row_complete(board):
						solved.add(boards.index(board))
						if (total - len(solved)) == 0:
							print(f"Sum: {sum(x for x in board if x > 0)}, pick: {pick}")
							return sum(x for x in board if x > 0) * pick


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	file = os.path.splitext(__file__)[0][-5:]
	with open(os.path.join(FILE_DIR, file + ".input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n\n")
	PICKS = [int(x) for x in DATA[0].split(',')]
	BOARDS = DATA[1:]
	new_boards = []
	for board in BOARDS:
		board = board.replace("\n", " ")
		board = [int(x) for x in board.split()]
		new_boards.append(board)
	BOARDS = new_boards
	print(f"Part 1: {part1(PICKS, BOARDS)}")
	print(f"Part 2: {part2(PICKS, BOARDS)}")
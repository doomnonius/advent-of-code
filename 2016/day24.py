from typing import Dict, List, Set, Tuple
from day01 import Coord
import string, itertools


def part1(walls: Set[Coord], points: Dict[str, Coord]) -> int:
	full_list = ''.join([x for x in points.keys()])
	all_pairs = itertools.permutations(full_list, 2)
	pairs = {a:navigate(a[0], a[1], walls, points) for a in all_pairs}
	# print(f"Pairs calculated: {pairs}")
	all_points = ''.join([x for x in points.keys() if x != '0'])
	orders = ['0' + ''.join(a) for a in itertools.permutations(all_points, len(all_points))]
	return min(total_dist(x, pairs) for x in orders)
	

def total_dist(order: str, pairs: Dict[Tuple, int]) -> int:
	retVal = 0
	for x in range(len(order) - 1):
		retVal += pairs[(order[x], order[x+1])]
	return sum(pairs[(order[x], order[x+1])] for x in range(len(order) - 1))

def navigate(start: Coord, end: Coord, walls: Set[Coord], points: Dict[str, Coord]) -> int:
	# print("Starting pair.")
	loc = points[start]
	visited = []
	end = points[end]
	input_commands = {'N':1, 'S':2, 'W':3, 'E':4}
	next_command_free = {1:'W', 2:'E', 3:'S', 4:'N'}
	next_command_blocked = {1:'E', 2:'W', 3:'N', 4:'S'}
	coord_commands = {1:Coord(0, -1), 2:Coord(0, 1), 3:Coord(-1, 0), 4:Coord(1, 0)}
	last_command = input_commands['S']
	while True:
		if loc == end:
			# draw(walls, visited, loc)
			m = len(visited)
			break
		if loc in visited:
			visited = visited[0:visited.index(loc)]
		if loc + coord_commands[last_command] in walls:
			last_command = input_commands[next_command_blocked[last_command]]
		else:
			visited.append(loc)
			loc = loc + coord_commands[last_command]
			last_command = input_commands[next_command_free[last_command]]
	next_command_blocked = {1:'W', 2:'E', 3:'S', 4:'N'}
	next_command_free = {1:'E', 2:'W', 3:'N', 4:'S'}
	last_command = input_commands['S']
	visited = []
	loc = points[start]
	while True:
		# draw(walls, visited, loc)
		if loc == end:
			# print(f"Pair complete.")
			if m < len(visited):
				return m
			else:
				return len(visited)
		if loc in visited:
			visited = visited[0:visited.index(loc)]
		if loc + coord_commands[last_command] in walls:
			last_command = input_commands[next_command_blocked[last_command]]
		else:
			visited.append(loc)
			loc = loc + coord_commands[last_command]
			last_command = input_commands[next_command_free[last_command]]


def draw(walls: Set, traveled: List, loc = Coord):
	max_x = max(z.x for z in walls)
	max_y = max(z.y for z in walls)
	h = max_y
	w = max_x
	reg = []
	while h >= 0:
		row = []
		reg.append(row)
		while w >= 0:
			row.append(" ")
			w -= 1
		h -= 1
		w = max_x
	for coord in walls:
		x = coord.x
		y = coord.y
		reg[y][x] = "#"
	reg[loc.y][loc.x] = "O"
	for coord in traveled:
		x = coord.x
		y = coord.y
		reg[y][x] = "."
	# reg[39][31] = "X"
	# reg[4][7] = "X"
	for row in reg:
		for char in row:
			print(char, end='')
		print()


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day24.testinput")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	WALLS = set()
	POINTS = {}
	for row in range(len(DATA)):
		for column in range(len(DATA[row])):
			here = DATA[row][column] 
			if here == "#":
				WALLS.add(Coord(column, row))
			elif here in string.digits:
				POINTS[here] = Coord(column, row)
	print(f"Part one: {part1(WALLS, POINTS)}")
	# print(f"Part two: {}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
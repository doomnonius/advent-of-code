from day01 import Coord
from typing import List, Set


def part1(inp: int, target: Coord) -> int:
	steps = 0
	loc = Coord(1, 1)
	walls = set()
	open_space = set()
	visited = []
	current = Coord(0,0)
	input_commands = {'N':1, 'S':2, 'W':3, 'E':4}
	next_command_free = {1:'W', 2:'E', 3:'S', 4:'N'}
	next_command_blocked = {1:'E', 2:'W', 3:'N', 4:'S'}
	coord_commands = {1:Coord(0, -1), 2:Coord(0, 1), 3:Coord(-1, 0), 4:Coord(1, 0)}
	last_command = input_commands['S']
	while True:
		# print(loc)
		if loc != current:
			for n in loc.neighbors():
				if n not in walls and n not in open_space:
					x = n.x
					y = n.y
					form = (x**2) + (3*x) + (2*x*y) + y + (y**2) + inp
					if bin(form).count("1") % 2 and x >= 0 and y >= 0:
						walls.add(n)
					else:
						open_space.add(n)
			current = loc
		if loc in visited:
			visited = visited[0:visited.index(loc)]
		if loc + coord_commands[last_command] in walls or (loc + coord_commands[last_command]).x < 0 or (loc + coord_commands[last_command]).y < 0:
			last_command = input_commands[next_command_blocked[last_command]]
		else:
			steps += 1
			visited.append(loc)
			loc = loc + coord_commands[last_command]
			last_command = input_commands[next_command_free[last_command]]
		if loc == target:
			m = len(visited)
			print(m)
			break
	next_command_blocked = {1:'W', 2:'E', 3:'S', 4:'N'}
	next_command_free = {1:'E', 2:'W', 3:'N', 4:'S'}
	last_command = input_commands['S']
	visited = []
	loc = Coord(1, 1)
	while True:
		if loc != current:
			for n in loc.full_neighbors():
				if n not in walls and n not in open_space:
					x = n.x
					y = n.y
					form = (x**2) + (3*x) + (2*x*y) + y + (y**2) + inp
					if bin(form).count("1") % 2 and x >= 0 and y >= 0:
						walls.add(n)
					else:
						open_space.add(n)
			current = loc
		if loc in visited:
			visited = visited[0:visited.index(loc)]
		if loc + coord_commands[last_command] in walls or (loc + coord_commands[last_command]).x < 0 or (loc + coord_commands[last_command]).y < 0:
			last_command = input_commands[next_command_blocked[last_command]]
		else:
			steps += 1
			visited.append(loc)
			loc = loc + coord_commands[last_command]
			last_command = input_commands[next_command_free[last_command]]
		if loc == target:
			n = len(visited)
			print(n)
			break
	draw(walls, visited)
	return min(m, n)


def draw(walls: Set, traveled: List):
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
	reg[1][1] = "O"
	for coord in traveled:
		x = coord.x
		y = coord.y
		reg[y][x] = "."
	reg[39][31] = "X"
	# reg[4][7] = "X"
	for row in reg:
		for char in row:
			print(char, end='')
		print()


if __name__ == "__main__":
	import timeit
	DATA = 1364
	# DATA = 10
	TARGET = Coord(31, 39)
	# TARGET = Coord(7, 4)
	print(f"Part one: {part1(DATA, TARGET)}") # not 324, too high; not 102, too high; not 84; not 88; 102-16 isn't 88
	# print(f"Part two: {}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
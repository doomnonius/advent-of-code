from typing import List, Set
from day02 import Computer
from day10 import Coord

class RepairBot (Computer):
	def __init__(self, instructions):
		super().__init__(instructions)
		self.loc = Coord(1000, 1000)

	def input(self):
		if self.input_list:
			return self.input_list.pop(0)
		else:
			raise IndexError


def maze_traversal(inst: List[int]):
	walls = set()
	input_commands = {'N':1, 'S':2, 'W':3, 'E':4}
	next_command_free = {1:'W', 2:'E', 3:'S', 4:'N'}
	next_command_blocked = {1:'E', 2:'W', 3:'N', 4:'S'}
	coord_commands = {1:Coord(0, -1), 2:Coord(0, 1), 3:Coord(-1, 0), 4:Coord(1, 0)}
	drone = RepairBot(inst[:])
	last_command = input_commands['N']
	drone.input_list = [last_command]
	while drone.run_codes() != 2:
		# use a "follow the wall" formula
		if drone.out == 0:
			walls.add(coord_commands[last_command] + drone.loc)
			last_command = input_commands[next_command_blocked[last_command]]
		elif drone.out == 1:
			drone.loc = drone.loc + coord_commands[last_command]
			last_command = input_commands[next_command_free[last_command]]
		drone.input_list = [last_command]
	i = 0
	next_command_blocked = {1:'W', 2:'E', 3:'S', 4:'N'}
	next_command_free = {1:'E', 2:'W', 3:'N', 4:'S'}
	coord_commands = {1:Coord(0, -1), 2:Coord(0, 1), 3:Coord(-1, 0), 4:Coord(1, 0)}
	drone = RepairBot(inst[:])
	last_command = input_commands['N']
	drone.input_list = [last_command]
	traveled = []
	while drone.run_codes() != 2:
		# use a "follow the wall" formula
		if drone.out == 0:
			walls.add(coord_commands[last_command] + drone.loc)
			last_command = input_commands[next_command_blocked[last_command]]
		elif drone.out == 1:
			if drone.loc not in traveled:
				traveled.append(drone.loc)
			else:
				traveled = traveled[:traveled.index(drone.loc)+1]
			drone.loc = drone.loc + coord_commands[last_command]
			last_command = input_commands[next_command_free[last_command]]
		drone.input_list = [last_command]
	# draw(walls, drone.loc, traveled)
	return traveled, walls, drone.loc

def fill_oxygen(inst: List[int]):
	walls, o_loc = maze_traversal(inst)[1:]
	t = 0
	o_locs = {o_loc}
	filled = set()
	while len(o_locs) > 0:
		next_o_locs = set()
		for o in o_locs:
			for p in o.neighbors():
				if p not in walls and p not in filled and p not in o_locs:
					next_o_locs.add(p)
		filled.update(o_locs)
		o_locs = next_o_locs.copy()
		t += 1
	return t

# used this modified version of paint (from day 11) to draw the maze for troubleshooting
def draw(walls: Set, drone, traveled: Set):
	walls.add(drone)
	min_x = min(z.x for z in walls)
	min_y = min(z.y for z in walls)
	max_x = max(z.x for z in walls)
	max_y = max(z.y for z in walls)
	walls.remove(drone)
	h = max_y - min_y + 1
	w = max_x - min_x + 1
	reg = []
	while h > 0:
		row = []
		reg.append(row)
		while w > 0:
			row.append(" ")
			w -= 1
		h -= 1
		w = max_x - min_x + 3
	for coord in walls:
		x = coord.x - min_x
		y = coord.y - min_y
		reg[y][x] = "#"
	reg[drone.y-min_y][drone.x-min_x] = "O"
	for coord in traveled:
		x = coord.x - min_x
		y = coord.y - min_y
		reg[y][x] = "."
	reg[1000-min_y][1000-min_x] = "X"
	reg = reg[::-1]
	for row in reg:
		for char in row:
			print(char, end='')
		print()

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day15.input")) as f:
		DATA = f.read().strip()
	DATA =[int(x) for x in DATA.split(",")]
	print(f"Part one: {len(maze_traversal(DATA)[0])+1}") # not 25 (tried counting by hand); not 668, too high
	print(f"Part two: {fill_oxygen(DATA)}")
	print(f"Time: {timeit.timeit('fill_oxygen(DATA)', setup='from __main__ import fill_oxygen, DATA', number = 1)}")
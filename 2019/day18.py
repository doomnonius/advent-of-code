from typing import Dict, List, Set
from day15 import Coord
from math import factorial
import datetime

class MazeExplorer:
	def __init__(self, loc: Coord):
		self.loc = Coord(loc.x, loc.y)
		self.input_commands = {'N':1, 'S':2, 'W':3, 'E':4}
		self.next_command_free_l = {1:'W', 2:'E', 3:'S', 4:'N'}
		self.next_command_blocked_l = {1:'E', 2:'W', 3:'N', 4:'S'}
		self.next_command_free_r = self.next_command_blocked_l
		self.next_command_blocked_r = self.next_command_free_l
		self.coord_commands = {1:Coord(0, -1), 2:Coord(0, 1), 3:Coord(-1, 0), 4:Coord(1, 0)}
		self.last_command = self.input_commands['N']

	def explore_left(self, walls):
		#wall on left
		if self.loc + self.coord_commands[self.last_command] not in walls:
			self.loc = self.loc + self.coord_commands[self.last_command]
			self.last_command = self.input_commands[self.next_command_free_l[self.last_command]]
		else:
			self.last_command = self.input_commands[self.next_command_blocked_l[self.last_command]]
			self.loc = self.explore_left(walls)
		# print(f"L: {self.loc}")
		# draw(walls, self, {})
		return self.loc

	def explore_right(self, walls):
		#wall on right
		if self.loc + self.coord_commands[self.last_command] not in walls:
			self.loc = self.loc + self.coord_commands[self.last_command]
			self.last_command = self.input_commands[self.next_command_free_r[self.last_command]]
		else:
			self.last_command = self.input_commands[self.next_command_blocked_r[self.last_command]]
			self.loc = self.explore_right(walls)
		# print(f"R: {self.loc}")
		# draw(walls, self, {})
		return self.loc

def amazing_formula(key: str, keys: Dict, walls: Set, doors: Dict, start: Coord, progress: List[int]):
	# print(len(keys))
	# print(key)
	bot_l = MazeExplorer(start)
	bot_r = MazeExplorer(start)
	explored_l = []
	explored_r = []
	bad = False
	i = 0 # catch infinite loops if key is unreachable
	while bot_l.explore_left(walls) != keys[key]:
		if bot_l.loc not in explored_l:
			explored_l.append(bot_l.loc)
		else:
			explored_l = explored_l[:explored_l.index(bot_l.loc)+1]
		i += 1
		if i > 1000:
			# print(f"{key} cannot be reached at this time")
			# draw(walls, bot_r, {}, keys)
			bad = True
			return 100000000
	while bot_r.explore_right(walls) != keys[key] and not bad:
		if bot_r.loc not in explored_r:
			explored_r.append(bot_r.loc)
		else:
			explored_r = explored_r[:explored_r.index(bot_r.loc)+1]
	del keys[key]
	# also need to remove the associated door from walls
	try: 
		old_walls = walls.copy()
		walls.remove(doors[key.upper()])
		assert old_walls != walls, "They match..."
	except: pass # print("Removal failed")
	# draw(walls, bot_r, {})
	if len(keys) == 0:
		# print("Bottomed!")
		progress[0] -= 1
		if progress[0] % 1000 == 0:
			print(f"{progress[0] / factorial(16) * 100} remaining, {datetime.datetime.now()}")
		return min(len(explored_l), len(explored_r))
	else:
		return min(len(explored_l), len(explored_r)) + min(amazing_formula(k, keys.copy(), walls.copy(), doors, bot_l.loc, progress) for k in keys.keys())

def map_builder(map_data: List[str], debug=True):
	print(factorial(16))
	walls = set()
	keys = {}
	doors = {}
	start = Coord(0, 0)
	for row in range(len(map_data)):
		for char in range(len(map_data[row])):
			c = map_data[row][char]
			if c in "abcdefghijklmnopqrstuvwxyz":
				keys[c] = Coord(char, row)
			elif c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
				doors[c] = Coord(char, row)
			elif c == "#":
				walls.add(Coord(char, row))
			elif c == ".":
				pass
			elif c == "@":
				start = Coord(char, row)
			else:
				print(f"Forgot to account for this char: {c}")
	[walls.add(x) for x in doors.values()]
	# walls.update({start})
	if debug:
		print(keys)
		print(doors)

	return min(amazing_formula(k, keys.copy(), walls.copy(), doors, start, [factorial(16)]) for k in keys.keys())

# used this modified version of paint (from day 11) to draw the maze for troubleshooting
def draw(walls: Set, bot, traveled: Set, keys: Dict):
	# print(walls)
	max_x = max(z.x for z in walls)
	max_y = max(z.y for z in walls)
	h = max_y + 1
	w = max_x + 1
	reg = []
	while h > 0:
		row = []
		reg.append(row)
		while w > 0:
			row.append(" ")
			w -= 1
		h -= 1
		w = max_x + 1
	for coord in walls:
		x = coord.x
		y = coord.y
		reg[y][x] = "#"
	reg[bot.loc.y][bot.loc.x] = "O"
	for key in keys.keys():
		x = keys[key].x
		y = keys[key].y
		reg[y][x] = key
	# reg = reg[::-1]
	for row in reg:
		for char in row:
			print(char, end='')
		print()


TEST_DATA = """
#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################"""

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day18.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	TEST_DATA = TEST_DATA.split("\n")[1:]
	print(f"Part one: {map_builder(TEST_DATA)}")
	# print(f"Part two: {}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
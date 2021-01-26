from day02 import Computer
from day11 import Coord
from typing import List

class Ball:
	def __init__(self, location):
		self.loc = location
		self.prev = location


class Arcade (Computer):
	def __init__(self, instructions):
		super().__init__(instructions)
		self.wall = set()
		self.block = set()
		self.paddle = Coord(0, 0)
		self.ball = Ball(Coord(0, 0))
		self.joystick = 0
		self.score = 0


	def input(self):
		# self.draw()
		if self.ball.loc.x > self.paddle.x:
			return 1
		elif self.ball.loc.x < self.paddle.x:
			return -1
		else:
			return 0

	def draw(self):
		all_pieces = self.wall.copy(); all_pieces.update(self.block); all_pieces.add(self.paddle); all_pieces.add(self.ball.loc)
		max_x = max(z.x for z in all_pieces)
		max_y = max(z.y for z in all_pieces)
		self.screen = []
		while max_y >= 0:
			row = []
			self.screen.append(row)
			hold = max_x
			while max_x >= 0:
				row.append(" ")
				max_x -= 1
			max_y -= 1
			max_x = hold
		for z in self.wall:
			self.screen[z.y][z.x] = "|"
		for z in self.block:
			self.screen[z.y][z.x] = "X"
		for z in {self.paddle}:
			self.screen[z.y][z.x] = "="
		for z in {self.ball.loc}:
			self.screen[z.y][z.x] = "o"
		for z in {self.ball.prev}:
			if self.ball.prev != self.ball.loc:
				self.screen[z.y][z.x] = "."
		for row in self.screen:
			for char in row:
				print(char, end='')
			print()

def run_game(info: List[int]):
	game = Arcade(info)
	out = []
	i = 0
	while not game.done:
		o = game.run_codes()
		if i % 3 == 0:
			out.append(o)
			i += 1
			continue
		elif i % 3 == 1:
			out.append(o)
			i += 1
			continue
		else:
			out.append(o)
		if out[2] == 1: game.wall.add(Coord(out[0], out[1]))
		elif out[2] == 2: game.block.add(Coord(out[0], out[1]))
		elif out[2] == 3: game.paddle = Coord(out[0], out[1])
		elif out[2] == 4: game.ball.loc = Coord(out[0], out[1])
		out = []
		i += 1
	return game.block
		
def run_game2(info: List[int]):
	game = Arcade(info)
	game.replace(0, 2)
	out = []
	i = 0
	while not game.done:
		o = game.run_codes()
		if i % 3 == 0:
			out.append(o)
			i += 1
			continue
		elif i % 3 == 1:
			out.append(o)
			i += 1
			continue
		else:
			out.append(o)
		if out[0] == -1 and out[1] == 0:
			game.score = out[2]
			out = []
			i += 1
			continue
		if out[2] == 1:
			game.wall.add(Coord(out[0], out[1]))
		elif out[2] == 2:
			game.block.add(Coord(out[0], out[1]))
		elif out[2] == 3:
			game.paddle = Coord(out[0], out[1])
		elif out[2] == 4:
			game.ball.loc = (Coord(out[0], out[1]))
			if game.ball.loc in game.block:
				game.block.remove(game.ball.loc)
		out = []
		i += 1
	return game.score

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day13.input")) as f:
		DATA = f.read().strip()
	DATA = [int(x) for x in DATA.split(",")]
	print(f"Part one: {len(run_game(DATA))}")
	print(f"Part two: {run_game2(DATA)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
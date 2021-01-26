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
		if self.ball.loc.x > self.paddle.x:
			return 1
		elif self.ball.loc.x < self.paddle.x:
			return -1
		else:
			return 0

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
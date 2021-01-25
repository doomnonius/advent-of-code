from typing import NamedTuple, List, Dict, Tuple, Set
import datetime, sys
from functools import reduce
from math import gcd

class Vector(NamedTuple):
	x: int
	y: int
	z: int

	def __repr__(self):
		return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

	def calc_velocity(self, other):
		a = b = c = 0
		if self.x > other.x: a = -1
		elif self.x < other.x: a = 1
		if self.y > other.y: b = -1
		elif self.y < other.y: b = 1
		if self.z > other.z: c = -1
		elif self.z < other.z: c = 1
		return Vector(a, b, c)

def calc_energy(planet: Dict):
	loc = planet["loc"]
	vel = planet["vel"]
	potential_energy = abs(loc.x) + abs(loc.y) + abs(loc.z)
	kinetic_energy = abs(vel.x) + abs(vel.y) + abs(vel.z)
	return kinetic_energy * potential_energy

def tracking(planets: Dict, cycles: int):
	for planets, i in permutate(planets):
		if i == 1000:
			return sum(calc_energy(planets[planet]) for planet in planets.keys())

def find_repeat(planet_dict: Dict):
	# Math tricks from Peter's solution:
	# You can calculate each coordinate (ie x, y, and z) because they aren't dependent on each other
	# Therefore, you can calculate how long it takes each coord to loop back, then find LCM
	# His is WAAAY more elegant, but this'll do
	x_loc = []
	y_loc = []
	z_loc = []
	x_vel = []
	y_vel = []
	z_vel = []
	for planet in planet_dict.keys():
		x_loc.append(planet_dict[planet]["loc"].x)
		y_loc.append(planet_dict[planet]["loc"].y)
		z_loc.append(planet_dict[planet]["loc"].z)
	for planet in planet_dict.keys():
		x_vel.append(planet_dict[planet]["vel"].x)
		y_vel.append(planet_dict[planet]["vel"].y)
		z_vel.append(planet_dict[planet]["vel"].z)
	# print(x)
	# print(y)
	# print(z)
	for planets, i in permutate(planet_dict):
		if [planets[planet]["loc"].x for planet in planets] == x_loc and [planets[planet]["vel"].x for planet in planets] == x_vel:
			x_loc = i
		if [planets[planet]["loc"].y for planet in planets] == y_loc and [planets[planet]["vel"].y for planet in planets] == y_vel:
			y_loc = i
		if [planets[planet]["loc"].z for planet in planets] == z_loc and [planets[planet]["vel"].z for planet in planets] == z_vel:
			z_loc = i
		if type(x_loc) == int and type(y_loc) == int and type(z_loc) == int:
			print([x_loc, y_loc, z_loc])
			return reduce(lambda a, b: a * b // gcd(a, b), [x_loc, y_loc, z_loc])

def permutate(planets: Dict) -> Dict:
	for i in range(1, sys.maxsize):
		for planet in planets.keys():
			for other_planet in planets.keys():
				if planet != other_planet:
					planets[planet]["vel"] = planets[planet]["vel"] + (planets[planet]["loc"].calc_velocity(planets[other_planet]["loc"]))
		for planet in planets.keys():
			planets[planet]["loc"] = planets[planet]["loc"] + planets[planet]["vel"]
		yield planets, i


TEST_DATA_QUICK = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""

TEST_DATA_SLOW = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day12.input")) as f:
		DATA = f.read().strip()
	DATA = [vector.split(", ") for vector in DATA[1:-1].split(">\n<")]
	TEST_DATA = [vector.split(", ") for vector in TEST_DATA_QUICK[1:-1].split(">\n<")]
	POSITIONS = [Vector(int(v[0][2:]), int(v[1][2:]), int(v[2][2:])) for v in DATA]
	TEST_POSITIONS = [Vector(int(v[0][2:]), int(v[1][2:]), int(v[2][2:])) for v in TEST_DATA]
	PLANETS = {POSITIONS.index(x):{"loc":x, "vel":Vector(0, 0, 0)} for x in POSITIONS}
	TEST_PLANETS = {TEST_POSITIONS.index(x):{"loc":x, "vel":Vector(0, 0, 0)} for x in TEST_POSITIONS}
	print(f"Part one: {tracking(PLANETS, 1000)}")
	print(f"Part two: {find_repeat(PLANETS)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
from typing import NamedTuple, List, Dict

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

def calc_energy(planet):
	pass

def tracking(planets: List[Vector], cycles: int):
	planet_dict = {planets.index(x):{"location":x, "velocity":Vector(0, 0, 0)} for x in planets}
	while cycles > 0:
		permutate(planet_dict)
		cycles -= 1
	return sum(calc_energy(planet_dict[planet]) for planet in planet_dict.keys())

def permutate(planets: Dict) -> Dict:
	for planet in planets.keys():
		for other_planet in planets.keys():
			if planet != other_planet:
				planets[planet]["velocity"] = planets[planet]["velocity"] + (planets[planet]["location"].calc_velocity(planets[other_planet]["location"]))
	for planet in planets.keys():
		planets[planet]["location"] = planets[planet]["location"] + planets[planet]["velocity"]



TEST_DATA = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day12.input")) as f:
		DATA = f.read().strip()
	DATA = [vector.split(", ") for vector in DATA[1:-1].split(">\n<")]
	POSITIONS = [Vector(int(v[0][2:]), int(v[1][2:]), int(v[2][2:])) for v in DATA]
	print(f"Part one: {tracking(POSITIONS, 100)}")
	# print(f"Part two: {}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
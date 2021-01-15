from typing import Dict, List, Set
import statistics as stat

def create_planet_dict(data: List) -> Dict:
	planet_dict = {}
	for line in data:
		planet, moon = line.split(")")
		if moon not in planet_dict.keys():
			planet_dict[moon] = planet
	return planet_dict

		
def count_orbits(data: Dict) -> int:
	direct_orbits = {k:0 for k, v in data.items()}
	for k in data.keys():
		placeholder = k
		while placeholder in data.keys():
			direct_orbits[k] += 1
			placeholder = data[placeholder]
	return sum(direct_orbits.values())
			
def navigate_orbits(data: Dict) -> int:
	paths = {k:[v] for k,v in data.items()}
	for k in data.keys():
		placeholder = k
		while placeholder in data.keys():
			placeholder = data[placeholder]
			paths[k].append(placeholder)
	for planet in paths["YOU"]:
		if planet in paths["SAN"]:
			return paths["SAN"].index(planet) + paths["YOU"].index(planet) - 2

TEST_DATA = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day06.input")) as f:
		DATA = f.read().strip()
	DATA = create_planet_dict(DATA.split("\n"))
	TEST_DATA = create_planet_dict(TEST_DATA.split("\n"))
	print(f"Part one: {count_orbits(DATA)}")
	print(f"Part two: {navigate_orbits(DATA)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
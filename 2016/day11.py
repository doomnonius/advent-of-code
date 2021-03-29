from typing import Dict


def part1(inp: Dict) -> int:
	level = 1
	while validSetup(inp, level):
		travel(inp, level)


def travel(floors: Dict, floor: int) -> int:
	...


def validSetup(floors: Dict, floor: int) -> bool:
	for k in floors:
		if k == "E": continue
		all_items = floors[k].copy()
		if k == floor: all_items.update(floors["E"])
		for item in all_items:
			if item[2] == "M" and item[0:2] + "G" not in floors[k] and len([x for x in floors[k] if x[2] == "G"]) > 0:
				return False
	return True


if __name__ == "__main__":
	import timeit
	DATA = """The first floor contains a polonium generator, a thulium generator, a thulium-compatible microchip, a promethium generator, a ruthenium generator, a ruthenium-compatible microchip, a cobalt generator, and a cobalt-compatible microchip.
The second floor contains a polonium-compatible microchip and a promethium-compatible microchip.
The third floor contains nothing relevant.
The fourth floor contains nothing relevant."""
	DATA = {1: {"PoG", "ThG", "ThM", "PrG", "RuG", "RuM", "CoG", "CoM"}, 2: {"PoM", "PrM"}, 3: {}, 4: {}, "E": {}}
	TEST_DATA = {"E": {}, 1: {"HyM", "LiM"}, 2: {"HyG"}, 3: {"LiG"}, 4: {}}
	print(f"Part one: {part1(TEST_DATA)}") # not 25 (tried to solve mentally, forgot you can't run the elevator without holding anything), 
	# print(f"Part two: {}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
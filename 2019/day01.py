# advent of code day 1

"""Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
"""

def fuelCalc (w):
	""" Mass / 3, round down, subtract 2
	"""
	return w//3-2


def fuelCalc_v2(weight):
	fuel_req = weight//3-2
	if fuel_req <= 0:
		return 0
	return fuel_req + fuelCalc_v2(fuel_req)


if __name__ == "__main__":
	import os
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day01.input")) as f:
		DATA = f.read().strip()
	FUEL = [int(x) for x in DATA.split("\n")]
	print(f"Part one: {sum(fuelCalc(x) for x in FUEL)}")
	print(f"Part two: {sum(fuelCalc_v2(x) for x in FUEL)}") # not 5005960, too low -> 5006064
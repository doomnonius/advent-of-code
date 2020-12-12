
class Instruction:
	def __init__(self, instruction):
		self.letter = instruction[0]
		self.number = int(instruction[1:])

def manhattan(instructions):
	def move_waypoint(direct, number, location):
		if direct == "N":
			location[0] += number
		elif direct == "E":
			location[1] += number
		elif direct == "S":
			location[0] -= number
		elif direct == "W":
			location[1] -= number
		return location
	
	
	def move_ship(location, number, rise_run):
		return [location[0] + rise_run[0]*number, location[1] + rise_run[1]*number]

	start = [0,0]
	waypoint = [1,10]
	for x in instructions:
		if x.letter == "R":
			for i in range(x.number//90):
				waypoint = [-waypoint[1], waypoint[0]]
		elif x.letter == "L":
			for i in range(x.number//90):
				waypoint = [waypoint[1], -waypoint[0]]
		elif x.letter == "F":
			start = move_ship(start, x.number, waypoint)
		else:
			waypoint = move_waypoint(x.letter, x.number, waypoint)

	return abs(start[0]) + abs(start[1])



if __name__ == "__main__":
	import os
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day12.input")) as f:
		DATA = f.read().strip()
	INSTRUCTIONS = [Instruction(line) for line in DATA.split("\n")]
	# print(f"Part one: {manhattan(INSTRUCTIONS)}")
	print(f"Part two: {manhattan(INSTRUCTIONS)}") # not 19011, or 35353, or 35531, but is 63447
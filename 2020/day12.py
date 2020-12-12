
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
		location[0] += rise_run[0]*number
		location[1] += rise_run[1]*number
		return location

	ins = []
	start = [0,0]
	waypoint = [1,10]
	headings = ["N", "E", "S", "W"]
	heading = "E"
	for x in instructions:
		x = Instruction(x)
		ins.append(x)
	for x in ins:
		if x.letter in headings:
			waypoint = move_waypoint(x.letter, x.number, waypoint)
		elif x.letter == "R":
			for i in range(x.number//90):
				waypoint = [-waypoint[1], waypoint[0]]
			# print(f"waypoint: {waypoint}")
		elif x.letter == "L":
			for i in range(x.number//90):
				waypoint = [waypoint[1], -waypoint[0]]
			# print(f"waypoint: {waypoint}")
		elif x.letter == "F":
			start = move_ship(start, x.number, waypoint)
		# print(start)

	return abs(start[0]) + abs(start[1])



if __name__ == "__main__":
	import os
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day12.input")) as f:
		DATA = f.read().strip()
	TESTCASE = """F10
N3
F7
R90
F11"""
	INSTRUCTIONS = DATA.split("\n")
	# print(f"Part one: {manhattan(INSTRUCTIONS)}")
	print(f"Part two: {manhattan(INSTRUCTIONS)}") # not 19011, or 35353, or 35531

class Instruction:
    def __init__(self, instruction):
        self.letter = instruction[0]
        self.number = instruction[1:]

def manhattan(instructions):
    def move(direct, number, location):
        if direct == "N":
            location[0] += number
        elif direct == "E":
            location[1] += number
        elif direct == "S":
            location[0] -= number
        elif direct == "W":
            location[1] -= number
        return location
    
    ins = []
    start = [0,0]
    headings = ["N", "E", "S", "W"]
    heading = "E"
    for x in instructions:
        x = Instruction(x)
        ins.append(x)
    for x in ins:
        if x.letter in headings:
            start = move(x.letter, x.number, location)
        elif x.letter == "L":
            heading = headings[(headings.index(heading)-x.number/90)%len(headings)]
        elif x.letter == "R":
            heading = headings[(headings.index(heading)+x.number/90)%len(headings)]
        elif x.letter == "F":
            start = move(heading, x.number, start)

    return abs(start[0]) + abs(start[1])



if __name__ == "__main__":
	import os
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day12.input")) as f:
		DATA = f.read().strip()
	INSTRUCTIONS = DATA.split("\n")
    print(f"Part one: {manhattan(INSTRUCTIONS)}")
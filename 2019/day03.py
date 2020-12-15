"""
Brainstorming:
- make a list of every coordinate each wire touches, based on the directional input
- compare the lists, find the common coordinates
- calculate the taxicab distance for each coordinate set (for points p1,q1 and p2,q2 = abs(p1-q1) + abs(p2-q2))
"""
from typing import NamedTuple

class Wire(NamedTuple):
	directions: List

	def __add__(self, other):
		"""This will be the function that looks for overlap.
		"""

def place(wire):
	""" Returns a (long) coordinate list of all the corners
	"""
	y = 0
	x = 0
	result = [(x,y)]
	for z in wire:
		if z[0] == "R":
			x = x + z[1]
			result.append((y,x))
		elif z[0] == "L":
			x = x - z[1]
			result.append((y,x))
		elif z[0] == "U":
			y = y + z[1]
			result.append((y,x))
		elif z[0] == "D":
			y = y - z[1]
			result.append((y,x))
		else:
			return("Error")
	return result

def compare(L1, L2):
	""" Compares two wires to find their overlaps.
	If I compare each pair of adjacent coords in one wire against each pair in the other wire, I can evaluate if there is an overlap.
	"""
	cross = []
	z = 0
	while z < len(L2)-1:
		for i in range(0, len(L1)-1):
			a0, b0 = L1[i][0], L1[i][1]
			a1, b1 = L1[i+1][0], L1[i+1][1]
			x0, y0 = L2[z][0], L2[z][1]
			x1, y1 = L2[z+1][0], L2[z+1][1]
			# check which way they are perpendicular
			if (a0 == a1 and y0 == y1) and (b0 <= y0 <= b1 or b0 >= y0 >= b1) and (x0 <= a0 <= x1 or x0 >= a0 >= x1):
				cross.append((a0, y0, i, z))
			elif (b0 == b1 and x0 == x1) and (y0 <= b0 <= y1 or y0 >= b0 >= y1) and (a0 <= x0 <= a1 or a0 >= x0 >= a1):
				cross.append((x0, b0, i, z))
		z += 1
	return cross

def distance(L):
	""" Takes a list of cross points and calculates the taxicab distance for each.
	"""
	distance = []
	for x in L:
		distance.append(abs(x[0])+abs(x[1]))
	return distance
		
def steps(L):
	""" Takes a list of cross points and calculates the number of steps for each.
	"""
	steps = []
	for j in L:
		i = 0
		z = 0
		for x in range(0, j[2]):
			i += w1[x][1]
		for y in range(0, j[3]):
			z += w2[y][1]
		# figure out direction of line
		p0 = (j[0], j[1])
		p1 = place(w1)[j[2]]
		p2 = place(w2)[j[3]]
		if p0[0] == p1[0]:
			i += abs(p0[1]-p1[1])
			z += abs(p0[0]-p2[0])
		else:
			i += abs(p0[0]-p1[0])
			z += abs(p0[1]-p2[1])
		steps.append(i+z)
	return steps
			
# print(place(w1))
# print(place(w2))
# print(compare(place(w1), place(w2)))
print(steps(compare(place(w1), place(w2))))
print(min(steps(compare(place(w1), place(w2)))))


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day02.input")) as f:
		DATA = f.read().strip()
	WIRES = DATA.split("\n")
	print(f"Part one: {}")
	print(f"Part two: {}")
	print(f"Time: {timeit.timeit('test_codes(BACKUP)', setup='from __main__ import test_codes, BACKUP', number = 1)}")
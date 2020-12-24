import math

class Image:
	def __init__(self, data):
		self.lines = data.split("\n")
		self.id = int(self.lines[0].split(" ")[1][0:4])
		self.top = self.lines[1]
		self.top_count = self.top.count("#")
		self.bottom = self.lines[10]
		self.bottom_count = self.bottom.count("#")
		self.left = "".join([x[0] for x in self.lines[1:11]])
		self.left_count = self.left.count("#")
		self.right = "".join([x[9] for x in self.lines[1:11]])
		self.right_count = self.right.count("#")

	def rotate_edges(self, turns=1):
		save = self.top
		self.top = self.right
		self.right = self.bottom
		self.bottom = self.left
		self.left = save
		return(self)

	def __repr__(self):
		return f"Top: {self.top}\nBottom: {self.bottom}\nLeft: {self.left}\nRight: {self.right}"




if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day20.input")) as f:
		DATA = f.read().strip()
	IMAGES = [Image(x) for x in DATA.split("\n\n")]
	SQUARE_SIZE = int(math.sqrt(len(IMAGES)))
	print(IMAGES[0])
	IMAGES[0].rotate_edges()
	print(IMAGES[0])
	print(f"Part one: {SQUARE_SIZE}")
	# print(f"Part two: {}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
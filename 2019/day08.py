def count_zeroes(data, size):
	layer_size = size[0] * size[1]
	layer_count = len(data)//layer_size
	mini = layer_size
	retVal = 0
	for x in range(layer_count):
		layer = data[x*layer_size:(x+1)*layer_size]
		# print(layer.count("0"), layer.count("1") * layer.count("2"))
		c = layer.count("0")
		if c < mini:
			mini = c
			retVal = layer.count("1") * layer.count("2")
	return retVal

def print_message(data, size):
	pixels = []
	layer_size = size[0] * size[1]
	layer_count = len(data)//layer_size
	print(layer_count)
	for l in range(layer_count):
		x = y = 0
		layer = data[l*layer_size:(l+1)*layer_size]
		i = 0
		while y < size[1]:
			if l == 0:
				row = []
				pixels.append(row)
			while x < size[0]:
				if l == 0:
					row.append([])
				# print(not pixels[y][x], l)
				if not pixels[y][x]:
					if layer[i] == '0':
						pixels[y][x].append(' ')
					elif layer[i] == '1':
						pixels[y][x].append('X')
				i += 1
				x += 1
			y += 1
			x = 0
	retVal = '\n'
	# print(pixels)
	for row in pixels:
		for char in row:
			retVal += char[0]
		retVal += '\n'
	return retVal

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day08.input")) as f:
		DATA = f.read().strip()
	SIZE = (25, 6)
	TEST_DATA = "0222112222120000"
	TEST_SIZE = (2, 2)
	print(f"Part one: {count_zeroes(DATA, SIZE)}") # not 2160; 
	print(f"Part two: {print_message(DATA, SIZE)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
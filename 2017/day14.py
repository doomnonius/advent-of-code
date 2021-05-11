import day10
from typing import Set
from day03 import Coord

def part1(inp: str) -> int:
	i = 0
	full_table = []
	while i < 128:
		binary = f'{int(day10.part2(inp + "-" + str(i)), 16):0>128b}'
		assert len(binary) == 128, "Binary too short" 
		full_table.append(binary)
		i += 1
	assert len(full_table) == 128, "Table too short"
	return full_table

def part2(inp: str) -> int:
	
	def neighbors(x: int, y: int) -> Set[Coord]:
		retVal = []
		if x > 0:
			retVal.append(Coord(x-1, y))
		if x < 127:
			retVal.append(Coord(x+1, y))
		if y > 0:
			retVal.append(Coord(x, y-1))
		if y < 127:
			retVal.append(Coord(x, y+1))
		return retVal
	

	grid = part1(inp)
	grouped = []
	groups = 0
	x = y = 0
	while x < 128:
		while y < 128:
			if grid[y][x] == "1":
				point = Coord(x, y)
			else:
				y += 1
				continue
			if point not in grouped:
				groups += 1
			else:
				y += 1
				continue
			edges = [point]
			group = [point]
			while True:
				new_edges = []
				for p in group:
					try:
						new_edges.extend([z for z in neighbors(p.x, p.y) if grid[z.y][z.x] == "1" and z not in group and z not in new_edges])
					except IndexError:
						print(new_edges)
						return
				if not new_edges:
					break
				edges = new_edges.copy()
				group.extend(edges)
			grouped.extend(group)
			y += 1
		x += 1
		y = 0
	assert sum(x.count('1') for x in grid) == len(grouped), "Not all items were grouped"
	return groups
	

if __name__ == "__main__":
	import timeit
	DATA = "uugsqrei"
	print(f"Part one: {sum(x.count('1') for x in part1(DATA))}")
	print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('part2(DATA)', setup='from __main__ import part2, DATA', number = 10)}")
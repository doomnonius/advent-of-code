import hashlib, itertools
from day01 import Coord

def part1(inp: str, loc = Coord(0, 0)) -> str:
	print(inp, loc)
	move = {"U": Coord(0, -1), "D": Coord(0, 1), "L": Coord(-1, 0), "R": Coord(1, 0)}
	dirs = {"U": 0, "D": 1, "L": 2, "R": 3}
	key = inp
	hsh = hashlib.md5(key.encode('utf-8')).hexdigest()[0:4]
	valid_locs = [Coord(x, y) for x, y in itertools.product(list(range(4)), repeat=2)]
	options = set()
	if sum(hsh[dirs[k]] in ['b', 'c', 'd', 'e', 'f'] for k in dirs) > 0:
		next_locs = {loc + move[k]: k for k in move if loc + move[k] in valid_locs}
	else:
		return False
	if len(inp) > 600:
		return False
	if Coord(3, 3) in next_locs.keys():
		return inp + next_locs[Coord(3, 3)]
	for next_loc in next_locs:
		n = part1(inp+next_locs[next_loc], next_loc)
		if not n:
			continue
		options.add(n)
	if options:
		return min(options, key=len)
	else:
		return False



if __name__ == "__main__":
	import timeit
	DATA = "pslxynzg"
	DATA = "ulqzkmiv"
	print(f"Part one: {part1(DATA)}")
	# print(f"Part two: {part1(DATA)}")
	# print(f"Time: {timeit.timeit('part1(DATA, LENGTH2)', setup='from __main__ import DATA, LENGTH2, part1', number = 1)}")
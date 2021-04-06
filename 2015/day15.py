from typing import List


class Ingredient:
	def __init__(self, data: str) -> None:
		split = data.split()
		self.cap = int(split[2][:-1])
		self.dur = int(split[4][:-1])
		self.fla = int(split[6][:-1])
		self.tex = int(split[8][:-1])
		self.cal = int(split[10])


def part1(inp: List[Ingredient], cal_limit = None) -> int:
	m = 0
	for a in range(100):
		for b in range(100):
			for c in range(100):
				for d in range(100):
					if a+b+c+d == 100:
						counts = [a, b, c, d]
						cap = dur = fla = tex = cal = 0
						for ing in range(len(inp)):
							cap += (inp[ing].cap * counts[ing])
							dur += (inp[ing].dur * counts[ing])
							fla += (inp[ing].fla * counts[ing])
							tex += (inp[ing].tex * counts[ing])
							cal += (inp[ing].cal * counts[ing])
						score = cap * dur * fla * tex
						if (cal_limit and cal != cal_limit) or cap < 0 or dur < 0 or fla < 0 or tex < 0:
							score = 0
						if score > m: m = score
	return m

TEST_DATA = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3""".split('\n')

if __name__ == "__main__":
	import timeit
	DATA = """Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9
Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1
Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8""".split("\n")
	print(f"Part one: {part1([Ingredient(x) for x in DATA], 0)}") # not 225000000, too high; 
	print(f"Part two: {part1([Ingredient(x) for x in DATA], 500)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
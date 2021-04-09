class Char:
	def __init__(self, info: str) -> None:
		split = info.split('\n')
		self.hp = int(split[0].split()[2])
		self.dam = int(split[1].split()[1])
		self.arm = int(split[2].split()[1])
		self.shield = 0
		self.point = 0
		self.recharge = 0

class Spell:
	def __init__(self, mc: int) -> None:
		...


BOSS = """Hit Points: 55
Armor: 0
Damage: 8"""
SELF = """Hit Points: 100
Damage: 0
Armor: 0"""


if __name__ == "__main__":
	import timeit
	BOSS = Char(BOSS)
	SELF = Char(SELF)
	print(f"Part one: {part1(BOSS, SELF)}")
	print(f"Part two: {part2(BOSS, SELF)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
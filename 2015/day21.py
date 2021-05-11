from typing import List


class Char:
	def __init__(self, info: str) -> None:
		split = info.split('\n')
		self.hp = int(split[0].split()[2])
		self.dam = int(split[1].split()[1])
		self.arm = int(split[2].split()[1])


class Item:
	def __init__(self, info: str) -> None:
		self.cost, self.dam, self.arm = [int(x) for x in info.split()[1:]]
		self.name = info.split()[0]
		
	def __repr__(self) -> str:
		return f"{self.name}"


def part1(boss: Char, you: Char, weapons: List[Item], armor: List[Item], rings: List[Item]) -> int:
	m = 1000
	la = len(armor)
	lr = len(rings)
	loadout = []
	debug = True
	for w in range(len(weapons)):
		cost = weapons[w].cost
		you.dam += weapons[w].dam
		loadout.append(weapons[w])
		for a in range(la + 1):
			if a < la:
				cost += armor[a].cost
				if cost > m:
					cost -= armor[a].cost
					continue
				you.arm += armor[a].arm
				loadout.append(armor[a])
			for r1 in range(lr + 1):
				if r1 < lr:
					cost += rings[r1].cost
					if cost > m:
						cost -= rings[r1].cost
						continue
					you.dam += rings[r1].dam
					you.arm += rings[r1].arm
					loadout.append(rings[r1])
				for r2 in range(lr + 1):
					if r2 < lr and r2 != r1:
						cost += rings[r2].cost
						if cost > m:
							cost -= rings[r2].cost
							continue
						you.dam += rings[r2].dam
						you.arm += rings[r2].arm
						loadout.append(rings[r2])
					if battle(you, boss):
						m = cost
					if r2 < lr and r2 != r1: 
						cost -= rings[r2].cost
						you.dam -= rings[r2].dam
						you.arm -= rings[r2].arm
						loadout = loadout[:-1]
				if r1 < lr:
					cost -= rings[r1].cost
					you.dam -= rings[r1].dam
					you.arm -= rings[r1].arm
					loadout = loadout[:-1]
			if a < la:
				cost -= armor[a].cost
				you.arm -= armor[a].arm
				loadout = loadout[:-1]
		cost -= weapons[w].cost
		you.dam -= weapons[w].dam
		loadout = []
	return m


def part2(boss: Char, you: Char, weapons: List[Item], armor: List[Item], rings: List[Item]) -> int:
	m = 0
	la = len(armor)
	lr = len(rings)
	loadout = []
	debug = True
	for w in range(len(weapons)):
		cost = weapons[w].cost
		you.dam += weapons[w].dam
		loadout.append(weapons[w])
		for a in range(la + 1):
			if a < la:
				cost += armor[a].cost
				you.arm += armor[a].arm
				loadout.append(armor[a])
			for r1 in range(lr + 1):
				if r1 < lr:
					cost += rings[r1].cost
					you.dam += rings[r1].dam
					you.arm += rings[r1].arm
					loadout.append(rings[r1])
				for r2 in range(lr + 1):
					if r2 < lr and r2 != r1:
						cost += rings[r2].cost
						you.dam += rings[r2].dam
						you.arm += rings[r2].arm
						loadout.append(rings[r2])
					if not battle(you, boss) and cost > m:
						m = cost
						if m == 201: print(loadout)
					if r2 < lr and r2 != r1: 
						cost -= rings[r2].cost
						you.dam -= rings[r2].dam
						you.arm -= rings[r2].arm
						loadout = loadout[:-1]
				if r1 < lr:
					cost -= rings[r1].cost
					you.dam -= rings[r1].dam
					you.arm -= rings[r1].arm
					loadout = loadout[:-1]
			if a < la:
				cost -= armor[a].cost
				you.arm -= armor[a].arm
				loadout = loadout[:-1]
		cost -= weapons[w].cost
		you.dam -= weapons[w].dam
		loadout = []
	return m


def battle(you: Char, boss: Char) -> bool:
	you_max = you.hp
	boss_max = boss.hp
	while (you.hp > 0) and (boss.hp > 0):
		boss.hp -= max((you.dam - boss.arm), 1)
		you.hp -= max((boss.dam - you.arm), 1)
	if boss.hp <= 0:
		you.hp = you_max
		boss.hp = boss_max
		return True
	else:
		you.hp = you_max
		boss.hp = boss_max
		return False


BOSS = """Hit Points: 103
Damage: 9
Armor: 2"""
SELF = """Hit Points: 100
Damage: 0
Armor: 0"""
WEAPONS = """Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0"""
ARMOR = """Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5"""
RINGS = """Damage+1    25     1       0
Damage+2    50     2       0
Damage+3   100     3       0
Defense+1   20     0       1
Defense+2   40     0       2
Defense+3   80     0       3"""

if __name__ == "__main__":
	import timeit
	BOSS = Char(BOSS)
	SELF = Char(SELF)
	WEAPONS = [Item(x) for x in WEAPONS.split('\n')]
	ARMOR = [Item(x) for x in ARMOR.split('\n')]
	RINGS = [Item(x) for x in RINGS.split('\n')]
	print(f"Part one: {part1(BOSS, SELF, WEAPONS, ARMOR, RINGS)}") # not 142, too high; 
	print(f"Part two: {part2(BOSS, SELF, WEAPONS, ARMOR, RINGS)}") # not 150, too low; not 159, too low; not 163, too low; 
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
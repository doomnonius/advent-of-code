from typing import Dict, List

TEST_DATA = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2"""


class Bot:
	def __init__(self, ident: str, val: List[int]) -> None:
		self.id = int(ident)
		self.vals = val

	def addRule(self, type_low: str, low: str, type_high: str, high: str) -> None:
		if type_low == "bot":
			self.low = int(low)
		else:
			self.low = low
		if type_high == "bot":
			self.high = int(high)
		else:
			self.high = high

	def __repr__(self) -> str:
		return f"{self.vals}"

	def check(self) -> bool:
		if 17 in self.vals and 61 in self.vals:
			return True
		return False


class Output:
	def __init__(self, ident: str) -> None:
		self.id = ident
		self.vals = []

	def __repr__(self) -> str:
		return f"{self.vals}"


def part1(inp: List[str]) -> Bot:
	bots = {}
	for line in inp:
		split = line.split()
		if split[0] == "bot" and (ident := int(split[1])) in bots:
			bots[ident].addRule(split[5], split[6], split[-2], split[-1])
			if split[5] == 'output':
				bots[split[6]] = Output(split[6])
			if split[-2] == 'output':
				bots[split[-1]] = Output(split[-1])
		elif split[0] == "bot" and (ident := int(split[1])) not in bots:
			bots[ident] = Bot(ident, [])
			bots[ident].addRule(split[5], split[6], split[-2], split[-1])
			if split[5] == 'output':
				bots[split[6]] = Output(split[6])
			if split[-2] == 'output':
				bots[split[-1]] = Output(split[-1])
		elif split[0] == "value" and (ident := int(split[-1])) not in bots:
			bots[ident] = Bot(split[-1], [int(split[1])])
		else:
			bots[ident].vals.append(int(split[1]))
	while max(len(bots[x].vals) for x in bots if type(bots[x]) == Bot) >= 2:
		for bot in bots:
			if type(bots[bot]) != Bot:
				continue
			splitList(bots[bot], bots)
	print(f"Part two: {bots['1'].vals[0] * bots['2'].vals[0] * bots['0'].vals[0]}")


def splitList(bot: Bot, bots: Dict) -> int:
	bot.vals.sort()
	if bot.check():
		print(f"Part one: {bot.id}")
	if len(bot.vals) == 2:
		if (len(bots[bot.high].vals) < 2 or type(bot.high) == str) and (len(bots[bot.low].vals) < 2 or type(bot.low) == str):
			bots[bot.high].vals.append(bot.vals.pop())
			bots[bot.low].vals.append(bot.vals.pop())
		else:
			splitList(bots[bot.high], bots)
			splitList(bots[bot.low], bots)
		if len(bots[bot.high].vals) == 2 and type(bot.high) == int:
			bots[bot.high].check()
			splitList(bots[bot.high], bots)
		if len(bots[bot.low].vals) == 2 and type(bot.low) == int:
			bots[bot.low].check()
			splitList(bots[bot.low], bots)
	elif len(bot.vals) > 2:
		assert 0 == 1, f"ERROR: {type(bot)} - {bot.vals}"


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day10.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	part1(DATA)
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
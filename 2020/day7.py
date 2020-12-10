import re
from typing import Dict, List

class Bag:
	def __init__(self, rule):
		base_pat = r'(\w+ \w+) bags contain\s?(\d?) (\w+ \w+) bags?'
		commas = rule.count(",")
		i = 0
		while i < commas:
			base_pat += (r", (\d) (\w+ \w+) bags?")
			i += 1
		colors = re.match(base_pat, rule)
		if colors == None: # ie no other bags
			self.color = re.match(r'(\w+ \w+) bags contain\s', rule).group(1)
			self.holds = {}
		else:
			self.color = colors.group(1)
			self.holds = {colors.group(3):colors.group(2)}
			i = 0
			while i < 2*commas:
				self.holds[colors.group(i+5)] = int(colors.group(i+4))
				i += 2
		self.unknown_contains = self.holds.copy()

# x = Bag("faded blue bags contain no other bags.")
# print(x.color)
# print(x.holds)

# I lifted these next two straight from Clint's solution
def build_reversed_bag_hash(bash_hash: Dict[str, Bag]):
	reversed_hash = {}
	for color in bags_hash.keys():
		reversed_hash[color] = [x.color for x in bags_hash.values() if color in x.holds.keys()]
	return reversed_hash

def get_all_containing_bags(reversed_bag_hash: Dict[str, List[str]], to_find: str):
	current_set = {to_find}
	while True:
		start_set = current_set.copy()
		for color in start_set:
			current_set.update(reversed_bag_hash[color])
		if start_set == current_set:
			return current_set - {to_find}

if __name__ == "__main__":
	import os
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day7.input")) as f:
		DATA = f.read().strip()
	RULES = DATA.split("\n")
	bags = [Bag(x) for x in RULES]
	bags_hash = {x.color: x for x in bags}
	reversed_hash = build_reversed_bag_hash(bags_hash)
	part_one_bags = get_all_containing_bags(reversed_hash, 'shiny gold')
	
	print(f"Part one: {len(part_one_bags)} bags can contain shiny gold.")
	# print(f"Part two: {}")
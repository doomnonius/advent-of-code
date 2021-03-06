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
		self.color = colors.group(1)
		if colors.group(3) == "no other":
			self.holds = {}
		else:
			self.holds = {colors.group(3):int(colors.group(2))}
			i = 0
			while i < 2*commas:
				self.holds[colors.group(i+5)] = int(colors.group(i+4))
				i += 2
		self.value = len(self.holds)

def count_bags(bags_hash: Dict[str, Bag], to_find: str):
	current_set = bags_hash[to_find].holds
	r = 0
	if current_set == {}:
		return 0 # had this incorrectly as 1
	for x in current_set.keys():
		r += current_set[x] + (count_bags(bags_hash, x) * current_set[x]) # had this incorrectly with adding current_set[x]
	return r
	
# I lifted these next two straight from Clint's solution
def build_reversed_bag_hash(bags_hash: Dict[str, Bag]):
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
	print(f"Part two: {count_bags(bags_hash, 'shiny gold')}") #43315 too low -> corrected algorithm based on eg in problem
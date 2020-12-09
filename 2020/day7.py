import re

class Bag:
	def __init__(self, rule):
		base_pat = r'(\w+\s\w+)\sbags\scontain\s?(\d?)\s(\w+\s\w+)\sbags?'
		commas = rule.count(",")
		i = 0
		while i < commas:
			base_pat += (r",\s?(\d?)\s(\w+\s\w+)\sbags?")
			i += 1
		colors = re.match(base_pat, rule)
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

def check_bag(rules, color=None):
	""" Checks for shiny gold.
	"""
	for x in rules:
		if "shiny gold" in x.holds:
			return x.color
		elif "no other" in x.holds:
			continue
		else:
			for y in x.holds:
				next_rule = [z for z in rules if z.color == y]
				if check_bag(rules, next_rule[0]) == None:
					continue

if __name__ == "__main__":
	import os
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day7.input")) as f:
		DATA = f.read().strip()
	RULES = DATA.split("\n")
	x = []
	r = 0
	for r in RULES:
		x.append(Bag(r))
	
	# print(f"Part one: {sum(z for y in x if )}")
	# print(f"Part two: {}")
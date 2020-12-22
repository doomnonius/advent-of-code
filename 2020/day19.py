import re, itertools
from typing import Dict, List
# first thing to do is break down the rules
# then convert them all to regex expressions
class Rule:
	def __init__(self, inp: str): # 109: 128 16 | 90 68 # '128: "b"'
		pattern = r"(\d+): \"?(\w+)\"? ?(\d{0,3})( \| (\d+) (\d{0,3}))?"
		match = re.match(pattern, inp)
		if match:
			self.id = int(match.group(1))
			self.pattern = None
			if 'b' in match.group(2) or 'a' in match.group(2):
				self.base = True
			else: self.base = False
			if not self.base: self.group1 = [int(match.group(2)), int(match.group(3))]
			else: self.group1 = match.group(2)
			self.either = not (not match.group(4))
			if self.either:
				self.group2 = [int(match.group(5)), int(match.group(6))]
			else: self.group2 = []
		else:
			raise Exception(f"Failed to parse line: {inp}")

def rule_to_regex(rules_hash: Dict[int, List[List]], rule):
	string = r""
	for pair in rules_hash[rule]:
		if type(pair) != str and pair: # ie not an empty list
			for sub_rule in pair:
				string += itertools.combinations([rule_to_regex(rules_hash, sub_rule)])
		else:
			return string
	


def match_rule(message: str, rule: int, rules: Dict) -> str:
	pat = rule_to_regex(rule, rules)
	print(pat)
	return message


TEST_DATA="""0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day19.input")) as f:
		DATA = f.read().strip()
	RULES, MESSAGES = TEST_DATA.split("\n\n")
	RULES = {y.id: [y.group1, y.group2] for y in [Rule(x) for x in RULES.split("\n")]}
	print(RULES)
	MESSAGES = MESSAGES.split("\n")
	print(f"Part one: {len([match_rule(message, 0, RULES) for message in MESSAGES])}")
	# print(f"Part two: {}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
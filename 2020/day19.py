import re
from typing import Dict, List
# first thing to do is break down the rules
# then convert them all to regex expressions

def build_rule(rules_dict, current_rule, depth=0):
	sections = []
	for section in rules_dict[current_rule]:
		section_regex = ""
		for label in section:
			if '"' in label: # this catches the letters
				section_regex += label[1]
			else:
				if label == current_rule:
					if depth < 5:
						section_regex += build_rule(rules_dict, label, depth=depth+1)
				else:
					section_regex += build_rule(rules_dict, label, depth=depth)
		sections.append(section_regex)
	regex_str = f"{'|'.join(sections)}" if len(sections) > 1 else sections[0]
	print(regex_str)
	return regex_str if len(regex_str) == 1 else f"({regex_str})"

def parse_messages(rules_dict, messages):
	starting_rule = build_rule(rules_dict, "0")
	regex = re.compile(f"^{starting_rule}$")
	print(regex)
	return sum(1 for m in messages if regex.match(m))

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
	RULES, MESSAGES = DATA.split("\n\n")
	# RULES = {y.id: [y.group1, y.group2] for y in [Rule(x) for x in RULES.split("\n")]}
	RULES: Dict[str, List[List[str]]] = {
		num: [section.split() for section in right.split("|")]
		for line in RULES.split("\n")
		for num, right in [line.split(": ")]
	}
	MESSAGES = MESSAGES.split("\n")
	print(f"Part one: {parse_messages(RULES, MESSAGES)}")
	# RULES['8'] = [['42'], ['42', '8']]
	# RULES['11'] = [['42', '31'], ['42', '11', '31']]
	# print(f"Part two: {parse_messages(RULES, MESSAGES)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
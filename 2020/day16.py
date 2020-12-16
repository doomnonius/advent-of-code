import re, math

class Rule:
	def __init__(self, rule):
		pattern = r"(.+): (\d+)-(\d+) or (\d+)-(\d+)"
		r = re.match(pattern, rule)
		self.field = r.group(1)
		self.permitted = set(range(int(r.group(2)), int(r.group(3))+1))
		self.permitted.update(range(int(r.group(4)), int(r.group(5))+1))

def check_tickets(nearby, rules):
	count = 0
	invalid = []
	all_rules = set()
	for rule in rules:
		all_rules.update(rule.permitted)
	for ticket in nearby:
		for number in ticket:
			if int(number) not in all_rules:
				count += int(number)
				invalid.append(ticket)
				continue
	return count, invalid

def remove_tickets(nearby, rules):
	invalid = check_tickets(nearby, rules)[1]
	for ticket in invalid:
		nearby.remove(ticket)
	return nearby

def name_rows(tickets, rules, mine):
	potentials = []
	rows = {rule.field:[] for rule in rules}
	for i in range(len(tickets[0])):
		check = set()
		for ticket in tickets:
			check.add(int(ticket[i]))
		for rule in rules:
			potentials.append((i, rule.field))
			for number in check:
				if number not in rule.permitted:
					potentials.remove((i, rule.field))
					break
	for potent in potentials:
		rows[potent[1]].append(potent[0])
	assigned = []
	discovered = {}
	while len(discovered) < 6:
		for k,v in rows.items():
			for value in v:
				if value in assigned:
					v.remove(value)
			if len(v) == 1:
				assigned.append(v[0])
				if "departure" in k:
					discovered.update({k: v[0]})
	return math.prod(int(mine[v]) for v in discovered.values())


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day16.input")) as f:
		DATA = f.read().strip()
	RULES, MINE, NEARBY = DATA.split("\n\n")
	RULES = [Rule(x) for x in RULES.split("\n")]
	MINE = MINE.split("\n")[1].split(",")
	NEARBY = [x.split(",") for x in NEARBY.split("\n")[1:]]
	print(f"Part one: {check_tickets(NEARBY, RULES)[0]}") # not 670425, too high; -> 29019
	print(f"Part two: {name_rows(remove_tickets(NEARBY, RULES), RULES, MINE)}")
	print(f"Time: {timeit.timeit('name_rows(remove_tickets(NEARBY, RULES), RULES, MINE)', setup='from __main__ import name_rows, remove_tickets, NEARBY, RULES, MINE', number=1)}") #0.004
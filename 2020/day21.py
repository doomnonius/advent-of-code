import re

def process(data):
	pattern = r"(.+) \(contains (.+)\)"
	known = {}
	all_ingredients = set()
	for line in data:
		found = re.search(pattern, line)
		unknown = set(found.group(1).split())
		for allergen in found.group(2).replace(",", "").split():
			if allergen not in known.keys():
				known[allergen] = []
			known[allergen].append(unknown)
		for ingredient in unknown:
			all_ingredients.add(ingredient)
	for allergen in known.keys():
		known[allergen] = set.intersection(*known[allergen])
	while sum(len(known[a]) for a in known.keys())/len(known.keys()) > 1:
		for a in known.keys():
			if len(known[a]) == 1:
				kn = list(known.keys())
				kn.remove(a)
				for al in kn:
					known[al] -= known[a]
	bad_ingredients = set.union(*[known[a] for a in known.keys()])
	safe_ingredients = all_ingredients-bad_ingredients
	safe_count = 0
	for ingredient in safe_ingredients:
		for line in data:
			if ingredient in line.split():
				safe_count += 1
	return safe_count, known

def canonical(D):
	l = list(D.keys())
	l.sort()
	retVal = ''
	for allergen in l:
		retVal += str(D[allergen])[2:-2] + ","
	return retVal[0:-1]




					
		
TEST_DATA = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day21.input")) as f:
		RAW_DATA = f.read().strip()
	DATA = RAW_DATA.split("\n")
	print(f"Part one: {process(DATA)[0]}") # not 2460, too high; not 85; 2320 also too high; not 2275; 
	print(f"Part two: {canonical(process(DATA)[1])}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
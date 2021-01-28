from typing import Dict, List, Set
from math import ceil
import datetime

class Recipe:
	def __init__(self, line):
		r = line.split(" => ")
		self.ingredients = {k:int(v) for v, k in [t.split() for t in r[0].split(", ")]}
		self.p_count, self.product = r[1].split()
		self.p_count = int(self.p_count)
		self.build = {}
	
	def __repr__(self):
		return f"{self.p_count} {self.product}: {self.ingredients}"

def build_full_list(recipes: Dict, prod: str, retVal: Dict, leftovers: Dict) -> Dict:
	if prod == "ORE": return retVal, leftovers
	recipe = recipes[prod]
	if recipe.product not in leftovers.keys():
		leftovers[prod] = 0
	try:
		cycles = ceil((retVal[prod] - leftovers[prod]) / recipe.p_count)
		leftovers[prod] = (cycles * recipe.p_count) - (retVal[prod] - leftovers[prod])
		retVal[prod] = 0
	except:
		cycles = 1
	for ing in recipe.ingredients.keys():
		if ing not in retVal.keys():
			retVal[ing] = recipe.ingredients[ing] * cycles
		else:
			retVal[ing] += recipe.ingredients[ing] * cycles
		build_full_list(recipes, ing, retVal, leftovers)
	return retVal, leftovers

def reverse_hash(recipes: Dict, prod: str) -> int:
	req, leftovers = build_full_list(recipes, prod, {}, {})
	o_count = 1000000000000 - req['ORE']
	f_count = 0
	# for recipe in recipes:
	# 	x = build_full_list(recipes, recipe.product, {}, {}, {})
	# 	x[2].pop(recipe.product, None)
	# 	builds[recipe.product] = [x[2], x[0]["ORE"]]
	while o_count > 0:
		new_req, leftovers = build_full_list(recipes, prod, {}, leftovers)
		f_count += 1
		o_count -= new_req['ORE']
		# if r[1]:
		# 	f_count += 1
		if f_count % 1000 == 0:
			print(f"f_count: {f_count}, {datetime.datetime.now()}")
	return f_count


TEST_DATA1 = """157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"""

TEST_DATA2 = """171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX"""

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day14.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	RECIPES = {Recipe(x).product:Recipe(x) for x in DATA}
	TEST_DATA1 = TEST_DATA1.split("\n")
	TEST_DATA2 = TEST_DATA2.split("\n")
	TEST_RECIPES1 = {Recipe(x).product:Recipe(x) for x in TEST_DATA1}
	TEST_RECIPES2 = {Recipe(x).product:Recipe(x) for x in TEST_DATA2}
	# print(TEST_RECIPES)
	print(f"Test one: {build_full_list(TEST_RECIPES2, 'FUEL', {}, {})[0]['ORE']}")
	print(f"Part one: {build_full_list(RECIPES, 'FUEL', {}, {})[0]['ORE']}")
	# print(f"Test two: {reverse_hash(TEST_RECIPES2, 'FUEL')}")
	print(f"Part two: {reverse_hash(RECIPES, 'FUEL')}")
	print(f"Time: {timeit.timeit('build_full_list(RECIPES, z, {}, {})', setup='from __main__ import build_full_list, RECIPES, z', number = 1000)}")
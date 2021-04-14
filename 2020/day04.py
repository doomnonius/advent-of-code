import re
from typing import List


def part2(inp: List[str]) -> int:
	c = 0
	for x in inp:
		r = x.replace("\n", " ")
		pairs = r.split(" ")
		D = {"byr":'', "iyr":'', "eyr":'', "hgt":'', "hcl":'', "ecl":'', "pid":'', "cid":None}
		for pair in pairs:
			k, v = pair.split(":")
			if k in D: D[k] = v
		
		# check byr
		byr = D["byr"]
		if len(byr) != 4: continue
		try:
			if not (1920 <= int(byr) <= 2002): continue
		except:
			continue

		# check iyr
		iyr = D["iyr"]
		if len(iyr) != 4: continue
		try:
			if not (2010 <= int(iyr) <= 2020): continue
		except:
			continue

		# check eyr
		eyr = D["eyr"]
		if len(eyr) != 4: continue
		try:
			if not (2020 <= int(eyr) <= 2030): continue
		except:
			continue

		# check hgt
		hgt = D['hgt']
		pat = r"(\d+)(.+)"
		if hgt == '':
			continue
		x = re.search(pat, hgt)
		if x.group(2) == "in":
			try:
				# print(int(x.group(1)))
				if not (59 <= int(x.group(1)) <= 76): continue
			except:
				continue
		elif x.group(2) == "cm":
			try:
				if not (150 <= int(x.group(1)) <= 193): continue
			except:
				continue
		else:
			continue

		# check hcl
		hcl = D["hcl"]
		if hcl == '' or len(hcl) != 7 or hcl[0] != "#":
			continue
		try:
			for char in hcl[1:]:
				if char not in ("0123456789abcdef"):
					continue
		except:
			continue

		# check ecl
		if D["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
			continue

		# check pid
		pid = D["pid"]
		try:
			int(pid)
		except:
			continue
		if len(pid) != 9:
			continue

		# don't check cid

		# if we made it all the way here, increase the count
		c += 1
		
	return c

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day04.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n\n")
	# overwrote initial part 1
	print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
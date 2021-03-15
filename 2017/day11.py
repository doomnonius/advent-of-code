from typing import List

def part1(inp: List[str]) -> int:
	count = {"ne": 0, "nw": 0, "n": 0, "s": 0, "se": 0, "sw": 0}
	for direct in inp:
		count[direct] += 1
	if count["ne"] >= count["sw"]:
		count["ne"] -= count["sw"]
		count["sw"] = 0
	else:
		count["sw"] -= count["ne"]
		count["ne"] = 0
	if count["nw"] >= count["se"]:
		count["nw"] -= count["se"]
		count["se"] = 0
	else:
		count["se"] -= count["nw"]
		count["nw"] = 0
	if count["n"] >= count["s"]:
		count["n"] -= count["s"]
		count["s"] = 0
	else:
		count["s"] -= count["n"]
		count["n"] = 0
	if count["nw"] > 0 and count["ne"] > 0:
		m = min(count["nw"], count["ne"])
		count["n"] += m
		count["ne"] -= m
		count["nw"] -= m
	if count["sw"] > 0 and count["se"] > 0:
		m = min(count["sw"], count["se"])
		count["s"] += m
		count["se"] -= m
		count["sw"] -= m
	return sum(count[x] for x in count.keys())

def part2(inp: List[str]) -> int:
	i = 720
	l = len(inp)
	m = 0
	while i < l:
		r = part1(inp[:i])
		if r > m:
			m = r
		i += 1
	return m


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day11.input")) as f:
		RAW_DATA = f.read().strip()
	DATA = RAW_DATA.split(",")
	print(f"Part one: {part1(DATA)}")
	print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
import re, json

find_num = re.compile(r'-{0,1}[0-9]+')


def part1(inp: str) -> int:
	return sum(int(x.group(0)) for x in find_num.finditer(inp))


def part2(inp: str) -> int:
	x = json.loads(inp)
	return sum(int(x.group(0)) for x in find_num.finditer(json.dumps(recursiveCheck(x))))


def recursiveCheck(inp: json, s = 0) -> int:
	if type(inp) == list:
		for i in range(len(inp)):
			obj = inp[i]
			typ = type(obj)
			if typ == dict and 'red' in obj.values():
				inp[i] = 0
			if typ == list or typ == dict:
				inp[i] = recursiveCheck(inp[i])
	elif type(inp) == dict:
		for k in inp.keys():
			obj = inp[k]
			typ = type(obj)
			if typ == dict and 'red' in obj.values():
				inp[k] = 0
			if typ == list or typ == dict:
				inp[k] = recursiveCheck(inp[k])
	return inp


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day12.input")) as f:
		DATA = f.read().strip()
	# print(len(DATA))
	print(f"Part one: {part1(DATA)}")
	print(f"Part two: {part2(DATA)}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
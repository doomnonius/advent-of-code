import re, string

chars = string.ascii_lowercase
valid_chars = 'abcdefghjkmnpqrstuvwxyz'
two_pairs = re.compile(r"([a-hj-km-np-z])\1.*([a-hj-km-np-z])\2")
valid_triples = [x for x in [chars[a] + chars[a+1] + chars[a+2] for a in range(len(chars)-2)] if 'i' not in x and 'l' not in x and 'o' not in x]
# print(all_triples)

def part1(inp: str) -> str:
	for c1 in [x for x in valid_chars if x >= inp[0]]:
		for c2 in [x for x in valid_chars if x >= inp[1]]:
			for c3 in [x for x in valid_chars if x >= inp[2]]:
				for c4 in valid_chars:
					for c5 in valid_chars:
						for c6 in valid_chars:
							for c7 in valid_chars:
								for c8 in valid_chars:
									opt = c1+c2+c3+c4+c5+c6+c7+c8
									if checkValid(opt) and opt > inp:
										return opt


def part2(inp: str) -> str:
	for c1 in [x for x in valid_chars if x >= inp[0]]:
		for c2 in [x for x in valid_chars if x >= inp[1]]:
			for c3 in [x for x in valid_chars if x > inp[2]]:
				for c4 in valid_chars:
					for c5 in valid_chars:
						for c6 in valid_chars:
							for c7 in valid_chars:
								for c8 in valid_chars:
									opt = c1+c2+c3+c4+c5+c6+c7+c8
									if checkValid(opt) and opt > inp:
										return opt


def checkValid(inp: str) -> bool:
	if sum(1 for x in two_pairs.finditer(inp)) and 'i' not in inp and 'l' not in inp and 'o' not in inp:
		for x in valid_triples:
			if x in inp:
				return True



if __name__ == "__main__":
	import timeit
	DATA = "vzbxkghb"
	print(f"Part one: {part1(DATA)}") # vzbxxyzz (calced by hand at first)
	print(f"Part two: {part2(part1(DATA))}") # not vzbaabcc; solved by hand, really... don't think this algo will necessarily work for any other input
	# print(f"Time: {timeit.timeit('part1(DATA, 50)', setup='from __main__ import part1, DATA', number = 1)}")
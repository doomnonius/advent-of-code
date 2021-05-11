from typing import List


def part1(inp: List[str], password: str) -> str:
	password = list(password)
	for line in inp:
		split = line.split()
		command = split[0]
		if command == "swap":
			if split[1] == "position":
				a = int(split[2])
				b = int(split[-1])
			else:
				a = password.index(split[2])
				b = password.index(split[-1])
			password[a], password[b] = password[b], password[a]
		elif command == "rotate":
			if split[1] == "left":
				count = int(split[2])
				password = password[count:] + password[:count]
			elif split[1] == "right":
				count = int(split[2])
				password = password[-count:] + password[:-count]
			else:
				password = basedRotate(password, split)
		elif command == "reverse":
			a = int(split[2])
			b = int(split[-1])
			password[a:b+1] = password[a:b+1][::-1]
		else:
			a = password.pop(int(split[2]))
			password.insert(int(split[-1]), a)
	return ''.join(password)


def basedRotate(password: List[str], split: List[str]) -> List[str]:
	i = password.index(split[-1])
	count = 1 + i
	if i >= 4:
		count += 1
	count %= len(password)
	return password[-count:] + password[:-count]


def undoBasedRotate(password: List[str], split: List[str]) -> List[str]:
	i = password.index(split[-1])
	if i % 2 == 1:
		count = i // 2 + 1
		return password[count:] + password[:count]
	elif i == 2:
		count = 2
	elif i == 4:
		count = 1
	elif i == 6:
		count = 0
	elif i == 0:
		count = 7
	return password[-count:] + password[:-count]


def part2(inp: List[str], password: str) -> str:
	inp = inp[::-1]
	password = list(password)
	for line in inp:
		split = line.split()
		command = split[0]
		if command == "swap": # same in reverse
			if split[1] == "position":
				a = int(split[2])
				b = int(split[-1])
			else:
				a = password.index(split[2])
				b = password.index(split[-1])
			password[a], password[b] = password[b], password[a]
		elif command == "rotate":
			if split[1] == "right": # swapped r/l
				count = int(split[2])
				password = password[count:] + password[:count]
			elif split[1] == "left": # swapped r/l
				count = int(split[2])
				password = password[-count:] + password[:-count]
			else: # swapped to rotate l instead
				password = undoBasedRotate(password, split)
		elif command == "reverse": # no changes needed
			a = int(split[2])
			b = int(split[-1])
			password[a:b+1] = password[a:b+1][::-1]
		else: # switch which part of split is popped and which is inserted
			a = password.pop(int(split[-1]))
			password.insert(int(split[2]), a)
	return ''.join(password)

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day21.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	PASS = "abcdefgh"
	PASS2 = "fbgdceah"
	print(f"Part one: {part1(DATA, PASS)}")
	print(f"Part two: {part2(DATA, PASS2)}") # not hefbgacd
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
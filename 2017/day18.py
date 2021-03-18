from typing import List, Dict

def part1(inp: List[str]) -> int:
	last_played = 0
	registers = {}
	l = len(inp)
	index = 0
	while 0 <= index < l:
		line = inp[index].split()
		if not isNumber(line[1]) and line[1] not in registers.keys(): registers[line[1]] = 0
		if len(line) == 3:
			if isNumber(line[2]):
				line[2] = int(line[2])
			else:
				if line[2] not in registers.keys(): registers[line[2]] = 0
				line[2] = registers[line[2]]
		if line[0] == "snd":
			last_played = snd(line[1], registers)
		elif line[0] == "set":
			registers[line[1]] = line[2]
		elif line[0] == "add":
			registers[line[1]] += line[2]
		elif line[0] == "mul":
			registers[line[1]] *= line[2]
		elif line[0] == "mod":
			registers[line[1]] %= line[2]
		elif line[0] == "rcv":
			if registers[line[1]] != 0:
				return last_played
		elif line[0] == "jgz":
			if registers[line[1]] > 0:
				index += line[2]
				continue
		index += 1
	

def snd(val: str, registers: Dict) -> int:
	if isNumber(val):
		return int(val)
	else:
		if val not in registers.keys(): registers[val] = 0
		return registers[val]

def isNumber(val: str) -> bool:
	try:
		int(val)
	except ValueError:
		return False
	return True

def part2(inp: List[str]) -> int:
	registers0 = {'p': 0, 'in': [], 'on': True}
	registers1 = {'p': 1, 'in': [], 'on': True}
	l = len(inp)
	index0 = 0
	index1 = 0
	retVal = 0
	while registers0['on'] or registers1['on']:
		while 0 <= index0 < l:
			line = inp[index0].split()
			if not isNumber(line[1]) and line[1] not in registers0.keys(): registers0[line[1]] = 0
			if len(line) == 3:
				if isNumber(line[2]):
					line[2] = int(line[2])
				else:
					if line[2] not in registers0.keys(): registers0[line[2]] = 0
					line[2] = registers0[line[2]]
			if line[0] == "snd":
				registers1['in'].append(snd(line[1], registers0))
				registers1['on'] = True
			elif line[0] == "set":
				registers0[line[1]] = line[2]
			elif line[0] == "add":
				registers0[line[1]] += line[2]
			elif line[0] == "mul":
				registers0[line[1]] *= line[2]
			elif line[0] == "mod":
				registers0[line[1]] %= line[2]
			elif line[0] == "rcv":
				if registers0['in']:
					registers0[line[1]] = registers0['in'].pop(0)
				else:
					registers0['on'] = False
					break
			elif line[0] == "jgz":
				if not isNumber(line[1]) and registers0[line[1]] > 0:
					index0 += line[2]
					continue
				elif isNumber(line[1]) and int(line[1]) > 0:
					index0 += line[2]
					continue
			index0 += 1
			# print(f"0: {registers0}\n1: {registers1}")
		while 0 <= index1 < l:
			line = inp[index1].split()
			if not isNumber(line[1]) and line[1] not in registers1.keys(): registers1[line[1]] = 0
			if len(line) == 3:
				if isNumber(line[2]):
					line[2] = int(line[2])
				else:
					if line[2] not in registers1.keys(): registers1[line[2]] = 0
					line[2] = registers1[line[2]]
			if line[0] == "snd":
				registers0['in'].append(snd(line[1], registers1))
				registers0['on'] = True
				retVal += 1
			elif line[0] == "set":
				registers1[line[1]] = line[2]
			elif line[0] == "add":
				registers1[line[1]] += line[2]
			elif line[0] == "mul":
				registers1[line[1]] *= line[2]
			elif line[0] == "mod":
				registers1[line[1]] %= line[2]
			elif line[0] == "rcv":
				if registers1['in']:
					registers1[line[1]] = registers1['in'].pop(0)
				else:
					registers1['on'] = False
					break
			elif line[0] == "jgz":
				if not isNumber(line[1]) and registers1[line[1]] > 0:
					index1 += line[2]
					continue
				elif isNumber(line[1]) and int(line[1]) > 0:
					index1 += line[2]
					continue
			index1 += 1
			# print(f"0: {registers0}\n1: {registers1}")
	return retVal



if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day18.input")) as f:
		RAW_DATA = f.read().strip()
	DATA = RAW_DATA.split("\n")
	print(f"Part one: {part1(DATA)}")
	print(f"Part two: {part2(DATA)}") # not 127, too low; used 'and' instead of 'or' in line 58
	# print(f"Time: {timeit.timeit('part2(DATA)', setup='from __main__ import part2, DATA', number = 10)}")
from typing import List
from copy import deepcopy

def part1(inp) -> int:
    l = len(inp.split()[0])
    items = len(inp.split())
    inp = inp.replace("\n", "")
    gamma = ''
    epsilon = ''
    for pos in range(l):
        pointer = pos
        hit = 0
        miss = 0
        while pointer < len(inp):
            pointer += l
            if int(inp[pointer]):
                hit += 1
            else:
                miss += 1
            if (hit == items//2):
                gamma += '1'
                epsilon += '0'
                break
            if (miss == items//2):
                gamma += '0'
                epsilon +='1'
                break
    return int(gamma, 2) * int(epsilon, 2)


def part2(inp: List[str], l) -> int:
    o = oxygen(inp, l)
    return  o * co2(inp, l)


def oxygen(inp: List[str], l) -> int:
    for spin in range(l):
        newInp = []
        check = (sum(int(item[spin]) for item in inp) >= len(inp)/2)
        for item in inp:
            if int(item[spin]) == check:
                newInp.append(item)
        inp = newInp
        if len(inp) == 1:
            return int(inp[0], 2)


def co2(inp: List[str], l) -> int:
    for spin in range(l):
        newInp = []
        check = (sum(int(item[spin]) for item in inp) >= len(inp)/2)
        for item in inp:
            if int(item[spin]) != check:
                newInp.append(item)
        inp = newInp
        print(inp)
        if len(inp) == 1:
            return int(inp[0], 2)


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	file = os.path.splitext(__file__)[0][-5:]
	with open(os.path.join(FILE_DIR, file + ".input")) as f:
		DATA = f.read().strip()
	print(f"Part 1: {part1(DATA)}")
	print(f"Part 2: {part2(DATA.split(), len(DATA.split()[0]))}") # not 1809756
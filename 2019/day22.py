from typing import List
import re

def shuffle(instructions: List, size: int, repeat = 0) -> List:
	deck = list(range(size)) # memory errors if too large
	pat = r'[-\d]{1,}'
	for inst in instructions:
		if inst == "deal into new stack":
			deck = deck[::-1]
		elif inst[0] == "d":
			inc = int(re.search(pat, inst).group())
			new_deck = deck.copy()
			i = 0
			for card in deck:
				new_deck[i] = card
				i = (i + inc)%size
			deck = new_deck
		else:
			cut = int(re.search(pat, inst).group())
			deck = deck[cut:] + deck[:cut]
	return deck



if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day22.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	print(f"Part one: {shuffle(DATA, 10007).index(2019)}")
	print(f"Part two: {shuffle(DATA, 119315717514047)[2020]}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
from typing import List
import string


class Room:
	def __init__(self, data) -> None:
		split, check = data.split("[")
		self.given_check = check[:-1]
		split = split.split("-")
		self.id = int(split[-1])
		self.name = ''.join(split[:-1])
		self.actual_check = calc_checksum(self.name)
		self.decrypted = decrypt(split[:-1], self.id%26)

	def __repr__(self) -> str:
		return f"{self.id}: {self.name}, {self.given_check}"


def decrypt(inp: List[str], rotate) -> str:
	lower = list(string.ascii_lowercase)
	retVal = ''
	for word in inp:
		for char in word:
			retVal += lower[(lower.index(char) + rotate) % 26]
		retVal += ' '
	return retVal


def calc_checksum(ident: str) -> str:
	retVal = ''
	chars = {}
	for char in ident:
		if char not in chars:
			chars[char] = 0
		chars[char] += 1
	most = []
	while len(retVal) < 5:
		if len(most) == 0:
			most = [x for x in chars.keys() if chars[x] == max(y for y in chars.values())]
			most.sort(reverse=True)
		retVal += most.pop()
		del chars[retVal[-1]]
	return retVal


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day04.input")) as f:
		RAW_DATA = f.read().strip()
	DATA = [Room(x) for x in RAW_DATA.split("\n")]
	# print(DATA)
	decrypt("qzmt-zixmtkozy-ivhz".split("-"), 343)
	print(f"Part one: {sum(x.id for x in DATA if x.given_check == x.actual_check)}") # not 115135, too low
	print(f"Part two: {[x.id for x in DATA if 'north' in x.decrypted][0]}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
def play_game(d1, d2):
	while len(d1) > 0 or len(d2) > 0:
		



if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day\\.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n\n")
	DECK1 = DATA[0].split("\n")
	DECK2 = DATA[1].split("\n")
	print(f"Part one: {DATA}")
	# print(f"Part two: {}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
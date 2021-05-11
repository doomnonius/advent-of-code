def play_game(d1, d2):
	turns = 0
	while len(d1) > 0 and len(d2) > 0:
		if (w := d1.pop(0)) > (l := d2.pop(0)):
			d1.append(w)
			d1.append(l)
		else:
			d2.append(l)
			d2.append(w)
		turns += 1
	retVal = [x for x in [d1, d2] if len(x) != 0][0]
	# print(retVal)
	return retVal

def play_recursively(d1, d2):
	configurations = [(d1[0:], d2[0:])]
	turns = 0
	while len(d1) > 0 and len(d2) > 0:
		if turns > 0 and (d1, d2) in configurations: # this rule isn't working properly
			return 1, d1
		configurations.append((d1[0:], d2[0:]))
		card1 = d1.pop(0)
		card2 = d2.pop(0)
		# print(d1)
		# print(d2)
		# print(f"Card 1: {card1}, {len(d1)}; Card 2: {card2}, {len(d2)}")
		if card1 <= len(d1) and card2 <= len(d2):
			# print("RECURSING!")
			winner = play_recursively(d1[0:card1], d2[0:card2])[0]
		elif card1 > card2:
			winner = 1
		else:
			winner = 2
		if winner == 1:
			d1.append(card1)
			d1.append(card2)
		else:
			d2.append(card2)
			d2.append(card1)
		turns += 1
	# print(turns)
	if len(d1) == 0: return 2, d2
	else: return 1, d1

def score_deck(deck):
	deck = deck[::-1]
	return sum((mult+1)*card for mult, card in enumerate(deck))

TEST_DATA = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day22.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n\n")
	DECK1 = [int(x) for x in DATA[0].split("\n")[1:]]
	DECK2 = [int(x) for x in DATA[1].split("\n")[1:]]
	part2 = play_recursively(DECK1.copy(), DECK2.copy())[1]
	print(part2)
	print(f"Part one: {score_deck(play_game(DECK1.copy(), DECK2.copy()))}") # 32187 is too high?!?!; forgot that string comparisons are dif than int
	print(f"Part two: {score_deck(part2)}") # not 32286, too low; 
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
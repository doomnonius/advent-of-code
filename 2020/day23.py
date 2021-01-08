def move_cups(order, moves):
	l = len(order)+1
	while moves > 0:
		# print(order)
		removed = order[1:4] + [0]
		insert_at = (order[0] - 1) % l
		while insert_at in removed:
			insert_at = (insert_at - 1) % l
		insert_ind = order.index(insert_at) + 1
		removed.remove(0)
		order = order[4:insert_ind] + removed + order[insert_ind:] + [order[0]]
		moves -= 1
	retVal = ''
	while order[0] != 1:
		order = order[1:] + [order[0]]
	for x in order[1:]:
		retVal += str(x)
	return retVal

def many_cups(order, moves):
	order += list(range(10,1000001))
	order = order[::-1]
	l = len(order)+1
	currCup = l-2
	while moves > 0:
		# print(len(order))
		if moves % 10000 == 0:
			print(f"Moves: {moves}; {moves/100000}% remaining")
			order = order[currCup+1:] + order[0:currCup+1]
			currCup = l-2
		removed = [order.pop(currCup - 1), order.pop(currCup - 2), order.pop(currCup - 3)]
		insert_at = (order[currCup-3] - 1) % l # list is now shorter, so active is now at c-3
		while insert_at in removed or insert_at == 0:
			insert_at = (insert_at - 1) % l
		insert_ind = order.index(insert_at) - 1
		for num in removed:
			order.insert(insert_ind, num)
		moves -= 1
		currCup -= 1
	ind_1 = order.index(1)
	return order[(ind_1 - 1)%(l-1)] * order[(ind_1 - 2)%(l-1)]

TEST_DATA = """389125467"""

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day23.input")) as f:
		DATA = f.read().strip()
	DATA = [int(x) for x in list(DATA)]
	TEST_DATA = [int(x) for x in list(TEST_DATA)]
	print(f"Part one: {move_cups(DATA, 100)}")
	x = [1, 3, 4, 2, 5] + list(range(5, 100001))
	print(f"Time: {timeit.timeit('x[0:2] + x[3:5] + [x[2]] + x[5:]', setup='from __main__ import x', number = 1000)}")
	print(f"Time: {timeit.timeit('z = [x.pop(4), x.pop(3)]; [x.insert(2, y) for y in z]', setup='from __main__ import x', number = 1000)}")
	print(f"Part two: {many_cups(TEST_DATA, 10000000)}")
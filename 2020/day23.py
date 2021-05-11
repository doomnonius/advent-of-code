from typing import Dict, Optional, Tuple


class Cup:
	def __init__(self, value: int, max_val: int, cup_cache: Dict[int, "Cup"]) -> None:
		self.next: Optional["Cup"] = None
		self.value = value
		self.max_val = max_val
		self.cup_cache = cup_cache

	
	def __repr__(self) -> str:
		return f"Cup({self.value}, n={self.next and self.next.value})"


	@staticmethod
	def load_input(seq: str) -> "Cup":
		cup_cache = {}
		cur_cup = first_cup = Cup(int(seq[0]), 9, cup_cache)
		cup_cache[first_cup.value] = first_cup
		for c in seq[1:]:
			new_cup = Cup(int(c), 9, cup_cache)
			cup_cache[new_cup.value] = new_cup
			cur_cup.next = new_cup
			cur_cup = new_cup
		cur_cup.next = first_cup
		return first_cup


	@staticmethod
	def load_input_p2(seq: str) -> "Cup":
		cup_cache = {}
		cur_cup = first_cup = Cup(int(seq[0]), 1000000, cup_cache)
		cup_cache[first_cup.value] = first_cup
		for c in seq[1:]:
			new_cup = Cup(int(c), 1000000, cup_cache)
			cup_cache[new_cup.value] = new_cup
			cur_cup.next = new_cup
			cur_cup = new_cup
		for i in range(10, 1000000 + 1):
			new_cup = Cup(i, 1000000, cup_cache)
			cup_cache[new_cup.value] = new_cup
			cur_cup.next = new_cup
			cur_cup = new_cup
		cur_cup.next = first_cup
		return first_cup

	
	def yank_3(self) -> "Cup":
		held_cups = self.next
		last_cup = held_cups.next.next
		self.next = last_cup.next
		last_cup.next = None
		return held_cups


	def place_3(self, held_cups: "Cup") -> "Cup":
		last_cup = held_cups.next.next
		last_cup.next = self.next
		self.next = held_cups
	

	def find_num(self, num: int) -> "Cup":
		if num < 1:
			num = self.max_val
		return self.cup_cache[num]

	
	def is_cup_in_next_3(self, cup: "Cup") -> bool:
		if cup is self:
			return True
		if cup is self.next:
			return True
		if cup is self.next.next:
			return True
		return False


	def run_round(self) -> "Cup":
		held_cups = self.yank_3()
		dest_cup = self.find_num(self.value - 1)
		while held_cups.is_cup_in_next_3(dest_cup):
			dest_cup = self.find_num(dest_cup.value - 1)
		dest_cup.place_3(held_cups)
		return self.next
	

	def state_to_str(self) -> str:
		one_cup = self.find_num(1)
		retVal = ""
		next_cup = one_cup.next
		while next_cup is not one_cup:
			retVal += str(next_cup.value)
			next_cup = next_cup.next
		return retVal

	
	def get_p2_nums(self) -> Tuple[int, int]:
		one_cup = self.find_num(1)
		return one_cup.next.value, one_cup.next.next.value


def move_cups(order, moves):
	l = len(order)+1
	while moves > 0:
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

# def many_cups(order, moves):
# 	order += list(range(10,1000001))
# 	order = order[::-1]
# 	l = len(order)+1
# 	currCup = l-2
# 	while moves > 0:
# 		if moves % 10000 == 0:
# 			print(f"Moves: {moves}; {moves/100000}% remaining")
# 			order = order[currCup+1:] + order[0:currCup+1]
# 			currCup = l-2
# 		removed = [order.pop(currCup - 1), order.pop(currCup - 2), order.pop(currCup - 3)]
# 		insert_at = (order[currCup-3] - 1) % l # list is now shorter, so active is now at c-3
# 		while insert_at in removed or insert_at == 0:
# 			insert_at = (insert_at - 1) % l
# 		insert_ind = order.index(insert_at) - 1
# 		for num in removed:
# 			order.insert(insert_ind, num)
# 		moves -= 1
# 		currCup -= 1
# 	ind_1 = order.index(1)
# 	return order[(ind_1 - 1)%(l-1)] * order[(ind_1 - 2)%(l-1)]


def part2(input_str: str, rng: int) -> int:
	cur_cup = Cup.load_input_p2(input_str)
	for _move in range(rng):
		cur_cup = cur_cup.run_round()
	n2, n3 = cur_cup.get_p2_nums()
	return n2 * n3


TEST_DATA = "389125467"

if __name__ == "__main__":
	import timeit
	RAW_DATA = "716892543"
	DATA = [int(x) for x in list(RAW_DATA)]
	TEST_DATA = [int(x) for x in list(TEST_DATA)]
	print(f"Part one: {move_cups(DATA, 100)}")
	print(f"Part two: {part2(RAW_DATA, 10000000)}")
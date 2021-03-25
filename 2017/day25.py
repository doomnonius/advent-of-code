from typing import List


def part1(steps: int, state: int) -> List[int]:
	i = 0
	slots = set()
	while steps > 0:
		if state == 0: # A
			if i in slots:
				i -= 1
				state = 4
			else:
				slots.add(i)
				i += 1
				state = 1
		elif state == 1: # B
			if i in slots:
				i += 1
				state = 5
			else:
				slots.add(i)
				i += 1
				state = 2
		elif state == 2: # C
			if i in slots:
				slots.remove(i)
				i += 1
				state = 1
			else:
				slots.add(i)
				i -= 1
				state = 3
		elif state == 3: # D
			if i in slots:
				slots.remove(i)
				i -= 1
				state = 2
			else:
				slots.add(i)
				i += 1
				state = 4
		elif state == 4: # E
			if i in slots:
				slots.remove(i)
				i += 1
				state = 3
			else:
				slots.add(i)
				i -= 1
				state = 0
		elif state == 5: # F
			if i in slots:
				i += 1
				state = 2
			else:
				slots.add(i)
				i += 1
				state = 0
		
		steps -= 1
	return slots





if __name__ == "__main__":
	import timeit
	STEPS = 12459852
	INITIAL_STATE = 0
	print(f"Part one: {len(part1(STEPS, INITIAL_STATE))}")
	# print(f"Part two: {part2(DATA)}")
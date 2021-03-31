def part1(inp: int) -> int:
	elves = list(range(1,inp+1))
	last_odd = False
	while len(elves) != 1:
		if len(elves) % 2 == 0:
			last_odd = False
		else:
			last_odd = True
		elves = elves[::2]
		if last_odd and len(elves) > 1:
			elves = elves[1:]
	return elves[0]


def part2(inp: int) -> int:
	elves = list(range(1, inp+1))
	i = 0
	l = len(elves)
	while l > 1:
		half = l // 2
		steal = (i + half) % l
		del elves[steal]
		l -= 1
		if steal > i:
			i += 1
		i %= l # because if we stole something from earlier in the circle, the circle shifts so the same index is the next person in line. We just need to verify that we haven't exceeded the length of the list
	return elves[0]


def find_largest_power(n: int, base: int) -> int:
    for i in range(99999):
        if base ** i > n:
            return base ** (i - 1)


def guess_number(n: int) -> int:
    largest_power = find_largest_power(n, 3)
    guess = n - largest_power
    if guess == 0:
        return n
    elif guess > largest_power:
        return largest_power + (guess - largest_power) * 2
    return guess


if __name__ == "__main__":
	import timeit
	DATA = 3012210
	print(f"Part one: {part1(DATA)}") # not 1506105, too low (tried solving mentally); not 3012209, too high; not 2097121, too high
	# print(f"Part two: {guess_number(DATA)}") # stolen wholesale from Peter; the code is understandable, the math is not
	print(f"Part two: {part2(DATA)}") # not 31682, too low (and took ~1 hour to find)
	# print(f"Time: {timeit.timeit('part1(DATA, LENGTH2)', setup='from __main__ import DATA, LENGTH2, part1', number = 1)}")
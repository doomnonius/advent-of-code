def test_range(r):
	rule_1 = test_increase(r)
	return test_adjacent(rule_1), test_adjacent_v2(rule_1)

def test_increase(r):
	low = r[0]
	high = r[1]
	hits = []
	x = 0
	while low < high:
		while x < 5:
			d1 = low//(10**(5-x))%10
			d2 = low//(10**(4-x))%10
			if d1 > d2:
				low += (10**(4-x)*(d1-d2))//10**(4-x)
				x = 0
				continue
			x += 1
		if low < high: hits.append(low)
		low += 1
		x = 0
	return hits

def test_adjacent(numbers):
	count = 0
	hit = False
	for x in numbers:
		x = str(x)
		for i in range(len(x)-1):
			if x[i] == x[i+1]:
				hit = True
		if hit:
			count += 1
			hit = False
	return count

def test_adjacent_v2(numbers):
	hits = 0
	hit = True
	for x in numbers:
		x = str(x)
		for char in x:
			if x.count(char) > 2:
				hit = False
		if not hit:
			hits += 1
			hit = True
	return hits




if __name__ == "__main__":
	import timeit
	DATA = [int(x) for x in "307237-769058".split('-')]
	print(f"Part one: {test_range(DATA)[0]}") # not 442, too low; nor 695, also low; -> 889, was skipping 333333-336999
	print(f"Part two: {test_range(DATA)[1]}") # not 540, too low; 
	print(f"Time: {timeit.timeit('test_range(DATA)', setup='from __main__ import test_range, DATA', number = 1)}")
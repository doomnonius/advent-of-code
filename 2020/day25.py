import sys

def transform(value, subject, loops):
	while loops > 0:
		value = value * subject
		value = value % 20201227
		loops -= 1
	return value

def yield_transform(value, subject):
	for i in range(sys.maxsize):
		yield i, value
		value *= subject
		value %= 20201227

def find_match(k1, k2, value, subject):
	keys = {k1, k2}
	loops = {k1: 0, k2: 0}
	# print(f"keys: {keys}")
	# print(f"loops: {loops}")
	for i, val in yield_transform(value, subject):
		if val in keys:
			keys.remove(val)
			loops[val] = i
		if not keys:
			break
	# while len(keys) > 0:
	# 	if (ret := transform(value, subject, x)) in keys:
	# 		keys.remove(ret)
	# 		loops[ret] = x
	# 		print("Hit!")
	# 	x += 1
		if i % 100000 == 0:
			print(val)
	assert((retVal := transform(value, k2, loops[k1])) == transform(value, k1, loops[k2]))
	print(loops)
	return retVal

				


if __name__ == "__main__":
	import timeit
	# KEY1 = 17807724
	# KEY2 = 5764801
	KEY1 = 13316116
	KEY2 = 13651422
	value = 1
	subject = 7
	print(f"Part one: {find_match(KEY1, KEY2, value, subject)}")
	# print(f"Part two: {}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
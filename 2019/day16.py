import datetime

def phasing(message, loops):
	level = 1
	next_message = ''
	l = len(message) # * 10000 in p2
	while loops > 0:
		while level <= l:
			ind = level - 1
			pos = True
			next_char = 0
			while ind < l:
				if pos:
					this_level = level
					while this_level > 0 and ind < l:
						next_char += int(message[ind])
						# if level <= 2: print(message[ind], end='')
						this_level -= 1
						ind += 1
					ind += level # because that's how many 0s there will be
				else:
					this_level = level
					while this_level > 0  and ind < l:
						next_char -= int(message[ind])
						# if level <= 2: print(message[ind], end='')
						this_level -= 1
						ind += 1
					ind += level
				pos = not pos
			next_message += str(abs(next_char)%10)
			# if level <= 2: print(next_char)
			level += 1
			ind = level - 1
		level = 1
		loops -= 1
		# print(next_message)
		message = next_message
		next_message = ''
		l = len(message)
	return message[0:8]

def phasing2(message, loops):
	level = 1
	next_message = ''
	l = len(message) * 10000
	while loops > 0:
		print(f"{loops}: {datetime.datetime.now()}")
		while level <= l:
			# if level % 1000 == 0: print(f"{level}: {datetime.datetime.now()}")
			ind = level - 1
			pos = True
			next_char = 0
			while ind < l:
				if pos:
					this_level = level
					while this_level > 0 and ind < l:
						next_char += int(message[ind%(l//10000)])
						# if level <= 2: print(message[ind], end='')
						this_level -= 1
						ind += 1
					ind += level # because that's how many 0s there will be
				else:
					this_level = level
					while this_level > 0  and ind < l:
						next_char -= int(message[ind%(l//10000)])
						# if level <= 2: print(message[ind], end='')
						this_level -= 1
						ind += 1
					ind += level
				pos = not pos
			next_message += str(abs(next_char)%10)
			# if level <= 2: print(next_char)
			level += 1
			ind = level - 1
		level = 1
		loops -= 1
		# print(next_message)
		message = next_message
		next_message = ''
		l = len(message)
	offset = int(message[0:7])
	return message[offset:offset+8]

def magic_logic(message):
	num_items = len(message)
	ret_list = message[:]
	for i in range(num_items - 2, -1, -1):
		ret_list[i] = (message[i] + ret_list[i + 1]) % 10
	return ret_list

def conversion_test1(message):
	l = len(message)
	m = int(message)
	c = 0
	while l > 0:
		l -= 1
		c += (m // 10**(l)) % 10 * (10**l)
	assert m == c
	return c


def conversion_test2(message):
	l = len(message)
	c = ''
	for char in message:
		c += str(int(char))
	assert message == c, c
	return c


TEST_DATA = "12345678"

if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day16.input")) as f:
		DATA = f.read().strip()
	# print(len(DATA))
	print(f"Part one: {phasing(DATA, 100)}")
	DATA = [int(x) for x in DATA]
	
	offset = int("".join(str(i) for i in DATA[:7]))
	DATA = DATA * 10_000
	assert offset > (len(DATA) // 2)
	DATA = DATA[offset:]

	for _ in range(100):
		# Wrote phasing2 myself, ~10min per phase on work pc
		# No idea if it would work properly, suspect it wouldn't actually
		# Ended up using magic logic Peter found on reddit, need to look into why it works
		# https://www.reddit.com/r/adventofcode/comments/ebai4g/2019_day_16_solutions/fb3lts9/
		DATA = magic_logic(DATA)
	print("".join((str(i) for i in DATA[:8])))
	# print(f"Part two: {phasing2(TEST_DATA, 100)}")
	# print(f"Time: {timeit.timeit('conversion_test1(DATA)', setup='from __main__ import conversion_test1, DATA', number = 1000)}")
	# print(f"Time: {timeit.timeit('conversion_test2(DATA)', setup='from __main__ import conversion_test2, DATA', number = 1000)}")
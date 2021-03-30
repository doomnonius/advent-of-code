import hashlib


def part1(inp: str, stretch: int) -> str:
	count = 0
	potentials = {}
	definites = {}
	i = 0
	retVal = []
	debug = False
	stretched = 0
	while count < 64:
		key = inp + str(i)
		hsh = hashlib.md5(key.encode('utf-8')).hexdigest()
		while stretched < stretch:
			hsh = hashlib.md5(hsh.encode('utf-8')).hexdigest()
			stretched += 1
		stretched = 0
		l = len(hsh)
		j = 0
		# print("Check1")
		for k in range(l - 2):
			# if i == 10840: debug = False
			char = hsh[k]
			# if i == 10839: debug = True
			if consecutive(hsh[:k+3], char, 3, debug):
				# print(f"{key}: {hsh}")
				try:
					potentials[i].append(char) # equals the character that there are 3 in a row of
				except KeyError:
					potentials[i] = [char]
				j += 1
				break
		old = set()
		for k in potentials:
			if i - k > 1000:
				old.add(k)
			if k not in old and k != i:
				for char in potentials[k]:
					if hsh.count(char) > 4 and consecutive(hsh, char, 5):
						# print(f"Hit: {hsh} @ {i} matches {k} on character '{char}'")
						definites[k] = k
						old.add(k)
						# print(f"{k} moved to definites.")
						break
		for o in old:
			# if o not in definites.keys(): print(f"{o} expired.")
			del potentials[o]
		try:
			m = min(k for k in potentials)
		except:
			m = 0
		for d in [k for k in definites]:
			if d < m:
				count += 1
				retVal.append(definites[d])
				# print(f"{d} added. Count: {count}")
				del definites[d]
		i += 1
	# print(len(retVal))
	return retVal[63]


def consecutive(inp: str, char: str, count: int, debug = False) -> bool:
	if debug: print(inp)
	l = len(inp)
	i = 0
	target = count - 1
	while i < l - target:
		if inp[i] != char:
			i += 1
			continue
		hits = 0
		for x in range(1, count):
			if inp[i+x] != char:
				i += x
				break
			else:
				hits += 1
				if hits == target:
					return True
	return False


if __name__ == "__main__":
	import timeit
	DATA = "ihaygndm"
	# DATA = "abc"
	# print(hashlib.md5('ihaygndm10839'.encode('utf-8')).hexdigest())
	# print(hashlib.md5('abc201'.encode('utf-8')).hexdigest())
	print(f"Part one: {part1(DATA, 0)}") # not 20465, too high; not 20388, too high; mistake in the consecutive forumula
	print(f"Part two: {part1(DATA, 2016)}") # not 19982, too high; 
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
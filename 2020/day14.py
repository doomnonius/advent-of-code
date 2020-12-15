import re
from typing import List, Dict

class Instruction:
	def __init__(self, line):
		line = line.replace(' ', '')
		line_data = line.split("=")
		self.command = line_data[0]
		if self.command == "mask":
			self.value = line_data[1]
			self.address = None
		else:
			pattern = r"mem\[(\d+)\]"
			address = re.match(pattern, self.command)
			self.value = "{0:b}".format(int(line_data[1])).zfill(36)
			self.address = address.group(1)


def run_program_p1(data: List):
	mask = ""
	addresses = {}
	for instruction in data:
		if instruction.command == "mask":
			mask = instruction.value
		else:
			addresses[instruction.address] = apply_mask_p1(mask, instruction.value)
	return sum(int(x, 2) for x in addresses.values())
			

def apply_mask_p1(mask, value):
	for i in range(len(mask)):
		if mask[i] != 'X':
			value = value[0:i] + mask[i] + value[i+1:]
	return value


def run_program_p2(data: List):
	mask = ""
	mask_count = 0
	addresses = {}
	for instruction in data:
		if instruction.command == "mask":
			mask = instruction.value
			mask_count += 1
		else:
			address = apply_mask_p2(mask, "{0:b}".format(int(instruction.address)).zfill(36))
			for add in arrangements(address):
				addresses[int(add, 2)] = instruction.value
	return sum(int(x, 2) for x in addresses.values())


def apply_mask_p2(mask, address):
	for i in range(len(mask)):
		if mask[i] == '1':
			address = address[0:i] + '1' + address[i+1:]
		elif mask[i] == 'X':
			address = address[0:i] + 'X' + address[i+1:]
	return address


def recurse(poss_count, addresses):
		middle = poss_count//2
		first = addresses[0:middle]
		second = addresses[middle:]
		if poss_count == 1:
			return addresses
		for i in range(len(first)):
			first[i].append("0")
		for y in second:
			y.append("1")
		retVal = recurse(middle, addresses[0:middle]) + recurse(middle, addresses[middle:])
		return retVal

def arrangements(address):
	poss_count = 2**address.count("X")
	blanks = []
	while len(blanks) < poss_count:
		blanks.append([])
	addresses = []
	variations = recurse(poss_count, blanks)
	for x in variations:
		placeholder = address
		for i in range(len(address)):
			if address[i] == "X":
				address = address[0:i] + x.pop() + address[i+1:]
		addresses.append(address)
		address = placeholder
	return addresses


# this was my O 2**n solution
def fork_address(address):
	if "X" not in address:
		return [address]
	addresses = []
	for i in range(len(address)):
		if address[i] == "X":
			addresses += fork_address(address[0:i] + '1' + address[i+1:])
			addresses += fork_address(address[0:i] + '0' + address[i+1:])
	return addresses
	

TEST_DATA_P1 = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

TEST_DATA_P2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""

if __name__ == "__main__":
	import os, datetime
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day14.input")) as f:
		DATA = f.read().strip()
	INST = [Instruction(x) for x in DATA.split("\n")]
	print(f"Part one: {run_program_p1(INST)}")
	print(datetime.datetime.now())
	print(f"Part two: {run_program_p2(INST)}") # not 462259518543
	print(datetime.datetime.now())
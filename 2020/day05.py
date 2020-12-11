import os

def read_ticket(t):
	""" Takes a ticket and returns the seat ID (Row * 8 + Column).
	"""
	b = 64
	r = c = 0
	for char in t[0:7]:
		if char == "B":
			r += b
		b //= 2
	
	b = 4
	for char in t[7:]:
		if char == "R":
			c += b
		b //= 2

	return (r * 8) + c
		
# print(read_ticket("BFFFBBFRRR"))


if __name__ == "__main__":
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(FILE_DIR + "\\day5.input") as f:
		DATA = f.read().strip()
	TICKETS = DATA.split("\n")
	IDS = [read_ticket(p) for p in TICKETS]
	[print(p) for p in range(min(IDS), max(IDS)) if p not in IDS]
	# print(min(read_ticket(p) for p in TICKETS))
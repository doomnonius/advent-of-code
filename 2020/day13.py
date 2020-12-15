
class Bus:
	def __init__(self, number, position):
		self.id = int(number)
		self.departures = (self.id*(100000000000000//self.id))+position

	def next_time(self):
		self.departures += self.id

def next_bus(arrival, buses):
	all_nearest = {}
	for bus in buses:
		if type(bus.id) == str:
			continue
		next_dep = 0
		while next_dep < arrival:
			next_dep += bus.id
		all_nearest[next_dep] = bus.id
	minimum = min(all_nearest.keys())
	return (minimum-arrival)*all_nearest[minimum]
			
def subsequent_departures(buses, num_buses: int):
	deps = {bus.departures for bus in buses}
	counter = 1
	if max(deps) > 100000000000000 + (1000000000 * counter):
		print(f"{counter} billion")
		print(datetime.datetime.now())
		counter += 1
	while len(deps) > 1:
		# I don't know how I am going to do this, but I want to find the smallest one and increment that one
		# What I currently have going on is just incrementing all of them
		for bus in buses:
			if bus.departures < max(deps):
				bus.next_time()
	return sum(deps) - (num_buses - 1)
	

TEST_DATA = """939
7,13,x,x,59,x,31,19"""

if __name__ == "__main__":
	import os, datetime
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day13.input")) as f:
		DATA = f.read().strip()
	DATA = DATA.split("\n")
	ARRIVAL, SCHEDULE = int(DATA[0]), DATA[1]
	BUSES = []
	SCHED = SCHEDULE.split(",")
	for i in range(L := len(SCHED)):
		# print(f"{i}")
		if SCHED[i] != 'x':
			BUSES.append(Bus(SCHED[i], L-1-i))
	print(f"Part one: {next_bus(ARRIVAL, BUSES)}")
	print(datetime.datetime.now())
	print(f"Part two: {subsequent_departures(BUSES, L)}")
	print(datetime.datetime.now())
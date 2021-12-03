
def part1() -> int:


    return


def part2() -> int:


    return


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	file = os.path.splitext(__file__)[0][-5:]
	with open(os.path.join(FILE_DIR, file + ".input")) as f:
		DATA = f.read().strip()
	DATA = [x.split() for x in DATA.split("\n")]
	print(f"Part 1: {part1(DATA)}")
	#print(f"Part 2: {part2(DATA)}")
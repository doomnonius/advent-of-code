from typing import List

def find_exception(numbers: List[int]):
	


if __name__ == "__main__":
	import os
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day9.input")) as f:
		DATA = f.read().strip()
	NUMBERS = [int(x) for x in DATA.split("\n")]
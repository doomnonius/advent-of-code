from typing import List

def part1(nums: List[int]) -> int:
    return





def part2(nums: List[int]) -> int:
    return




if __name__ == "__main__":
	import os, timeit
	from pathlib import Path
	INPUT_FILE = Path(__file__).with_suffix(".input")
	DATA = INPUT_FILE.read_text().strip()
	DATA = [int(x) for x in DATA.split()] # example code
	print(f"Part 1: {part1(DATA)}")
	print(f"Part 2: {part2(DATA)}")
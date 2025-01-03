from typing import List, NamedTuple

class Coord3d(NamedTuple):
    x: int
    y: int
    z: int

    def up(self):
        return Coord3d(self.x, self.y, self.z + 1)

    def down(self):
        return Coord3d(self.x, self.y, self.z - 1)
    
class Block:
    def __init__(self, start: Coord3d, end: Coord3d) -> None:
        self.blocks = []


def part1(nums: List[int]) -> int:
    return





def part2(nums: List[int]) -> int:
    return




if __name__ == "__main__":
    from datetime import datetime
    from pathlib import Path
    test = False
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    RAW_DATA = INPUT_FILE.read_text().strip().split("\n")
    DATA = [int(x) for x in DATA.split()] # example code
    print(f"Part 1: {part1(DATA)}")
    print(f"Part 2: {part2(DATA)}")
    
from typing import List
from helpers import Chunk

def part1(nums: List[int], t = False) -> int:
    r = 0
    id = 0
    i = 0
    d = dict()
    e = [int(x) for x in nums[1::2]]
    for c in nums[0::2]:
        d[id] = int(c)
        id += 1
    # if t: print(f"d: {d}")
    for k in d.keys():
        # if t: print(f"key: {k}")
        while d[k] > 0:
            r += (k * i)
            # if t: print(f"r: {r}")
            d[k] -= 1
            i += 1
        try: empty = e.pop(0)
        except IndexError: empty = 0
        # if t: print(f"empty: {empty}")
        while empty > 0:
            try: top = max([k for k in d.keys() if d[k] > 0])
            except: top = 0
            # if t: print(f"top: {top}")
            r += (top * i)
            # if t: print(f"r: {r}")
            d[top] -= 1
            i += 1
            empty -= 1
    return r





def part2(nums: List[int]) -> int:
    return




def process_data(data: str) -> List[str]:
    return data.strip()

if __name__ == "__main__":
    from datetime import datetime
    from pathlib import Path
    from helpers import import_files
    TEST_FILE, INPUT_FILE = import_files(Path(__file__))
    TEST_DATA = process_data(TEST_FILE)
    DATA = process_data(INPUT_FILE)
    test_1a = 1928
    test_2a = 2858
    p1 = part1(TEST_DATA, True)
    if test_1a: assert p1 == test_1a, f"Part 1: {p1} is the wrong answer"
    p1 = part1(DATA)
    print(f"Part 1: {p1}")
    p2 = part2(TEST_DATA)
    if test_2a: assert p2 == test_2a, f"Part 2: {p2} is the wrong answer"
    p2 = part2(DATA)
    print(f"Part 2: {p2}")
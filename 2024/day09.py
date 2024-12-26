from typing import List
from helpers import Chunk, Space

def part1(nums: List[int], t = False) -> int:
    chunks: List[Chunk] = []
    other_chunks: List[Chunk] = []
    spaces: List[Space] = []
    id = 0
    pos = 0
    i = 0
    while i < len(nums):
        l = int(nums[i])
        chunks.append(Chunk(id, pos, l))
        id += 1
        try:
            e = int(nums[i+1])
        except:
            break
        pos += l
        spaces.append(Space(pos, e))
        pos += e
        i += 2
    for s in spaces:
        for x in s.fill(chunks, t):
            other_chunks.append(x)
    return sum(c.value() for c in chunks) + sum(c.value() for c in other_chunks)

def part2(nums: List[int], t = False) -> int:
    chunks: List[Chunk] = []
    other_chunks: List[Chunk] = []
    spaces: List[Space] = []
    id = 0
    pos = 0
    i = 0
    while i < len(nums):
        l = int(nums[i])
        chunks.append(Chunk(id, pos, l))
        id += 1
        try:
            e = int(nums[i+1])
        except:
            break
        pos += l
        spaces.append(Space(pos, e))
        pos += e
        i += 2
    while chunks:
        c = chunks.pop()
        if t: print(f"{c.id}: {c.start}, {c}")
        c.fill(spaces, t)
        if t: print(f"{c.id}: {c.start}, {c}")
        other_chunks.append(c)
    return sum(c.value() for c in chunks) + sum(c.value() for c in other_chunks)


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
    p1 = part1(TEST_DATA)
    if test_1a: assert p1 == test_1a, f"Part 1: {p1} is the wrong answer"
    p1 = part1(DATA)
    print(f"Part 1: {p1}")
    p2 = part2(TEST_DATA)
    if test_2a: assert p2 == test_2a, f"Part 2: {p2} is the wrong answer"
    p2 = part2(DATA)
    print(f"Part 2: {p2}")
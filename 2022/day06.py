from typing import List

def part1(inp: str) -> int:
    i = 4
    while i < len(inp):
        if len(set(inp[i-4:i])) == 4:
            return i
        i += 1
        
def part2(inp: str) -> int:
    i = 14
    while i < len(inp):
        if len(set(inp[i-14:i])) == 14:
            return i
        i += 1

if __name__ == "__main__":
    import os, timeit
    FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    file = os.path.splitext(__file__)[0][-5:]
    with open(os.path.join(FILE_DIR, file + ".input")) as f:
        DATA = str(f.read().strip())
    print(f"Part 1: {part1(DATA)}")
    print(f"Part 2: {part2(DATA)}")
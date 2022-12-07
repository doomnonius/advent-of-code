from typing import List
import string

def part1(commands: List[str], p1: bool = True) -> int:
    dir_sizes = {}
    curr_dirs = []
    dirs = 0
    for c in commands:
        if c.startswith("$ c"):
            if c[5] != ".":
                dir_sizes[dirs] = 0
                curr_dirs.append(dirs)
                dirs += 1
            else:
                curr_dirs.pop()
        elif c[0] in string.digits:
            for x in curr_dirs:
                dir_sizes[x] += int(c.split()[0])
    if p1: return sum(x for x in dir_sizes.values() if x < 100000)
    avail = 70000000 - dir_sizes[0]
    needed = 30000000 - avail
    return min([x for x in dir_sizes.values() if x > needed])

if __name__ == "__main__":
    import os, timeit
    FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    file = os.path.splitext(__file__)[0][-5:]
    with open(os.path.join(FILE_DIR, file + ".input")) as f:
        DATA = f.read().strip()
    DATA = DATA.split('\n')
    print(f"Part 1: {part1(DATA)}") # not 1074121
    print(f"Part 2: {part1(DATA, False)}")
    print(f"Time: {timeit.timeit('part1(DATA, False)', setup='from __main__ import part1, DATA', number = 1000)/1000}")
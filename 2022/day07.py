from typing import List
import string

def part1(commands: List[str], test: bool = False, p1: bool = True) -> int:
    dir_sizes = {}
    curr_dirs = []
    dirs = 0
    for c in commands:
        if c.startswith("$ cd "):
            if test: print(f"cd line: {c[5:]}")
            if c[5] != ".":
                dir_sizes[dirs] = 0
                curr_dirs.append(dirs)
                dirs += 1
                if test: print(curr_dirs)
            else:
                curr_dirs.pop()
                if test: print(curr_dirs)
        elif c[0] in string.digits:
            if test: print("File line")
            for x in curr_dirs:
                dir_sizes[x] += int(c.split()[0])
    if test: print(dir_sizes)
    if p1: return sum(x for x in dir_sizes.values() if x < 100000)
    avail = 70000000 - dir_sizes[0]
    needed = 30000000 - avail
    return min([x for x in dir_sizes.values() if x > needed])

if __name__ == "__main__":
    import os, timeit
    test = False
    FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    file = os.path.splitext(__file__)[0][-5:]
    if test:
        with open(os.path.join(FILE_DIR, file + ".testinput")) as f:
            DATA = f.read().strip()
    else:
        with open(os.path.join(FILE_DIR, file + ".input")) as f:
            DATA = f.read().strip()
    DATA = DATA.split('\n') # example code
    # print(DATA)
    print(f"Part 1: {part1(DATA, test)}") # not 1074121
    print(f"Part 2: {part1(DATA, test, False)}")
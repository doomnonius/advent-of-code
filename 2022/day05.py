from typing import List
import re

def part1(ins: List[re.Match], start: dict[int:List[str]]) -> str:
    for l in ins:
        i, cycles, source, dest = 0, int(l.group("cycles")), int(l.group("source")), int(l.group("dest"))
        while i < cycles:
            start[dest].append(start[source].pop())
            i += 1
    tops = [x[-1] for x in start.values()]
    r = ''
    for x in tops:
        r += x
    return r

def part2(ins: List[re.Match], start: dict[int:List[str]]) -> str:
    for l in ins:
        cycles, source, dest = int(l.group("cycles")), int(l.group("source")), int(l.group("dest"))
        start[dest] += start[source][-cycles:]
        start[source] = start[source][0:-cycles]
    tops = [x[-1] for x in start.values()]
    r = ''
    for x in tops:
        r += x
    return r

if __name__ == "__main__":
    import os, timeit
    FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    file = os.path.splitext(__file__)[0][-5:]
    with open(os.path.join(FILE_DIR, file + "_ins.input")) as f:
        INSTRUCTIONS = f.read().strip()
    pattern = r"move (?P<cycles>\d+) from (?P<source>\d+) to (?P<dest>\d+)" # move 4 from 2 to 1
    # print(INSTRUCTIONS.split("\n"))
    INSTRUCTIONS = [re.match(pattern, x) for x in INSTRUCTIONS.split("\n")] # example code
    # print(INSTRUCTIONS)
    with open(os.path.join(FILE_DIR, file + "_crates.input")) as g:
        CRATES = g.read().split("\n")
    LAYOUT = {x: [] for x in range(1,10)}
    LAYOUT_COPY = {x: [] for x in range(1,10)}
    for row in CRATES:
        i = 0
        while i < len(row):
            pattern = r"\[(?P<box>[A-Z])\]"
            hit = re.match(pattern, row[i:i+4])
            if hit:
                LAYOUT[i//4+1].insert(0,hit.group('box'))
                LAYOUT_COPY[i//4+1].insert(0,hit.group('box'))
                # print(hit.group('box'))
            i += 4
    print(LAYOUT)
    print(f"Part 1: {part1(INSTRUCTIONS, LAYOUT)}")
    print(f"Part 2: {part2(INSTRUCTIONS, LAYOUT_COPY)}") # not FPBZGTNRG b/c LAYOUT was set to result from last part and not default values
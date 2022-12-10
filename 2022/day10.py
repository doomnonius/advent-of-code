from typing import List, Set, Tuple

def increase(cycles: int, t: int, x: int) -> Tuple[int, int, int]:
    cycles += 1
    if not (cycles - 20) % 40:
        if test: print(f"cycle: {cycles}, adding {cycles * x} to {t}")
        t += (cycles * x)
    return (cycles, t, x)

def part1(comms: List) -> int:
    cycles = 0
    x = 1
    retVal = 0
    for c in comms:
        if len(c) > 1:
            inc = int(c[1])
            cycles, retVal, x = increase(cycles, retVal, x)
            if test and cycles > 200: print(f"x just increased to {x}")
            cycles, retVal, x = increase(cycles, retVal, x)
            x += inc
        else:
            cycles, retVal, x = increase(cycles, retVal, x)
    return retVal

def draw(sprite: int, c: int):
    if (c % 40) - 1 in [sprite, sprite-1, sprite+1]:
        return '#'
    return '.'

def part2(comms: List) -> int:
    cycles = 0
    x = 1
    retVal = 0
    drawn = []
    for c in comms:
        if len(c) > 1:
            inc = int(c[1])
            cycles, retVal, x = increase(cycles, retVal, x)
            drawn.append(draw(x, cycles))
            # if test and cycles > 200: print(f"x just increased to {x}")
            cycles, retVal, x = increase(cycles, retVal, x)
            drawn.append(draw(x, cycles))
            x += inc
        else:
            cycles, retVal, x = increase(cycles, retVal, x)
            drawn.append(draw(x, cycles))
    i = 0
    while(i) < len(drawn):
        if not i % 40: print()
        print(drawn[i], end='')
        i += 1

if __name__ == "__main__":
    import os, timeit
    from pathlib import Path
    test = False
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    DATA = INPUT_FILE.read_text().strip().split('\n')
    DATA = [x.split() for x in DATA]
    print(f"Part 1: {part1(DATA)}")
    print(f"Part 2:")
    {part2(DATA)}
from typing import List

def part1(inp: str) -> int:
    r = 0
    for c in inp:
        r += ord(c)
        r *= 17
        r %= 256
    return r

def part2(data: List[str]) -> int:
    boxes = {x:{} for x in range(256)}
    for inst in data:
        if "-" in inst:
            label, lens = inst.split("-")
            remove = True
        else:
            label, lens = inst.split("=")
            remove = False
        box = part1(label)
        if not remove:
            boxes[box][label] = lens
        else:
            if label in boxes[box]:
                del(boxes[box][label])
    focus = 0
    for box in boxes:
        pos = 1
        for lens in boxes[box]:
            focus += (box + 1) * pos * int(boxes[box][lens])
            pos += 1
    return focus

if __name__ == "__main__":
    from datetime import datetime
    from pathlib import Path
    test = False
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    DATA = INPUT_FILE.read_text().strip().split(",")
    print(f"Part 1: {sum(part1(x) for x in DATA)}")
    print(f"Part 2: {part2(DATA)}")
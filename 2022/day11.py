from typing import List, Dict
import re, math

class Monkey:
    def __init__(self, inp): # parse the lines here
        pat = r"Monkey (?P<id>\d+):\n +Starting items: (?P<items>(?:\d+\, ){0,10}\d+)\n +Operation: new = old (?P<op_sign>.) (?P<op_num>\w+)\n +Test: divisible by (?P<mod>\d+)\n +If true: throw to monkey (?P<if_true>\d+)\n +If false: throw to monkey (?P<if_false>\d+)"
        m = re.search(pat, inp)
        self.id = m.group("id")
        self.items = [int(x) for x in m.group("items").split(", ")]
        self.op_sign = m.group("op_sign")
        self.op_num = m.group("op_num")
        self.mod = int(m.group("mod"))
        self.true = int(m.group("if_true"))
        self.false = int(m.group("if_false"))
        self.checked = 0

    def __repr__(self):
        return f"{(self.id, self.items)}"

def part1(inp: Dict[int, Monkey], c: int, worry: bool = False) -> int:
    # if worry: lcm = math.lcm(*(m.mod for m in inp.values()))
    if worry: all_mods = math.prod(m.mod for m in inp.values())
    while c:
        for m in inp.values():
            for item in m.items:
                m.checked += 1
                try:
                    op_num = int(m.op_num)
                except:
                    op_num = item
                if m.op_sign == "*":
                    item = item * op_num
                else:
                    item = item + op_num
                if not worry: item = item // 3
                # else: m.items[i] %= lcm
                else: item = item % all_mods
                if not item % m.mod: # (ab)using that 0 == False
                    inp[m.true].items.append(item)
                else:
                    inp[m.false].items.append(item)
            m.items = []
        c -= 1
        # if test: print(f"{({m.id:m.items for m in inp.values()})}")
        # if worry: print(f"c: {c}")
    checks = [m.checked for m in inp.values()]
    checks.sort()
    print(checks)
    return checks[-2] * checks[-1]





def part2(nums: List[int]) -> int:
    return




if __name__ == "__main__":
    import os, timeit
    from pathlib import Path
    test = True
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    DATA = INPUT_FILE.read_text().strip().split('\n\n')
    MONKEYS = {x:Monkey(DATA[x]) for x in range(len(DATA))}
    print(MONKEYS)
    print(f"Part 1: {part1(MONKEYS, 20)}")
    print(f"Part 2: {part1(MONKEYS, 10000, True)}")
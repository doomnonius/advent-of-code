from typing import List, Tuple, Set, Dict, NamedTuple
import re

class Part(NamedTuple):
    x: int
    m: int
    a: int
    s: int

    def total(self):
        return self.x + self.m + self.a + self.s

class Rule:
    def __init__(self, data: str):
        self.rules: List[Tuple[str, str]] = []
        rules = data.split(",")
        for rule in rules:
            if ":" in rule:
                e, out = rule.split(":")
                self.rules.append((e, out))
            else:
                self.rules.append(("True", rule[:-1]))

    def run(self, part: Part) -> str:
        x, m, a, s = part.x, part.m, part.a, part.s
        for rule in self.rules:
            if eval(rule[0]):
                return rule[1]

def part1(parts: Set[Part], rules: Dict[str, Rule]) -> int:
    retVal = 0
    curr = "in"
    for p in parts:
        while curr not in "AR":
            curr = rules[curr].run(p)
        if curr == "A":
            retVal += p.total()
        curr = "in"
    return retVal

def part2(rules: Dict[str, Rule]) -> int:
    
    def find_next(path: str, rule: str):
        rule_forks = rules[rule].rules
        for r in rule_forks:
            if r[1] == "A":
                if r[0] == "True": #and r[1] == "A":
                    paths.append(path)
                else:
                    path += "," + r[0]
                    paths.append(path)
                    path += "!"
            elif r[1] == "R":
                if r[0] != "True":
                    path += "," + r[0] + "!"
            else:
                if r[0] != "True":
                    path += "," + r[0]
                    stack.append((path, r[1]))
                    path += "!"
                else:
                    stack.append((path, r[1]))

    paths = []
    stack = [("", "in")]
    while stack:
        curr_path, curr_rule = stack.pop(0)
        find_next(curr_path, curr_rule)
    comp_d : {">":"<", "<":">"}
    retVal = 0
    for p in paths:
        x = [1, 4000]
        m = [1, 4000]
        a = [1, 4000]
        s = [1, 4000]
        for cond in p[1:].split(","):
            letter = cond[0]
            comp = cond[1]
            flipped = (cond[-1] == "!")
            if flipped:
                num = int(cond[2:-1])
            else:
                num = int(cond[2:])
            if not flipped:
                if comp == "<":
                    num -= 1
                    # if eval(f"num < {letter}[1]")
                    exec(f"{letter}[1] = {num}")
                else:
                    num += 1
                    exec(f"{letter}[0] = {num}")
            if flipped:
                if comp == ">":
                    exec(f"{letter}[1] = {num}")
                else:
                    exec(f"{letter}[0] = {num}")
        retVal += (x[1] - x[0] + 1) * (m[1] - m[0] + 1) * (a[1] - a[0] + 1) * (s[1] - s[0] + 1)
    return retVal

def process_data(inp: str) -> Tuple[Set[Part], Dict[str, Rule]]:
    raw_rules, raw_parts = inp.split("\n\n")
    part_search = r"{x=(?P<x>\d+),m=(?P<m>\d+),a=(?P<a>\d+),s=(?P<s>\d+)}"
    parts = set()
    for line in raw_parts.split("\n"):
        m = re.match(part_search, line)
        parts.add(Part(int(m.group('x')),int(m.group('m')),int(m.group('a')),int(m.group('s'))))
    test = raw_rules.split("\n")[0]
    rules = {x[0:x.index("{")]:Rule(x[x.index("{")+1:]) for x in raw_rules.split("\n")}
    return parts, rules



if __name__ == "__main__":
    from datetime import datetime
    from pathlib import Path
    test = False
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    PARTS, RULES = process_data(INPUT_FILE.read_text().strip())
    print(f"Part 1: {part1(PARTS, RULES)}")
    print(f"Part 2: {part2(RULES)}")
from typing import List, Tuple, Dict, Set

class Page:
    def __init__(self, n):
        self.number = n
        self.before: Set = set()
        self.after: Set = set()
        self.value = 0

    def __eq__(self, value):
        if self.number == value:
            return True
        return False
    
    def __hash__(self):
        return hash(self.number)

def part1(nums: Tuple[Dict[int,Page],List[List[int]]]) -> Tuple[int,List[List[int]]]:
    r = 0
    invalid = []
    rules = nums[0]
    prints = nums[1]
    for p in prints:
        valid = True
        for i in range(len(p)):
            before = p[:i]
            after = p[i+1:]
            if p[i] not in rules.keys():
                pass
            for x in before:
                if x not in rules[p[i]].after:
                    continue
                else: valid = False
            for x in after:
                if x not in rules[p[i]].before:
                    continue
                else: valid = False
        if valid: r += p[len(p)//2]
        else: invalid.append(p)
    return (r, invalid)

def part2(nums: Tuple[Dict[int,Page],List[List[int]]]) -> int:
    r = 0
    rules = nums[0]
    prints = nums[1]
    for p in prints:
        for i in range(len(p)):
            others = p[:i] + p[i+1:]
            rules[p[i]].value = sum(1 for o in others if o in rules[p[i]].after)
        p = sorted(p, key=lambda x: rules[x].value)
        r += p[len(p)//2]
    return r


def process_data(data: str) -> Tuple[Dict[int,Page],List[List[int]]]:
    rule_dict: Dict[int, Page] = dict()
    rules, lines = data.strip().split("\n\n")
    for r in rules.split("\n"):
        f,s = (int(x) for x in r.split("|"))
        if f not in rule_dict.keys():
            rule_dict[f] = Page(f)
        if s not in rule_dict.keys():
            rule_dict[s] = Page(s)
        rule_dict[s].before.add(rule_dict[f])
        rule_dict[f].after.add(rule_dict[s])
    prints = []
    for line in lines.split("\n"):
        prints.append([int(x) for x in line.split(",")])
    return (rule_dict,prints)

if __name__ == "__main__":
    from datetime import datetime
    from pathlib import Path
    from helpers import import_files
    TEST_FILE, INPUT_FILE = import_files(Path(__file__))
    TEST_DATA = process_data(TEST_FILE)
    DATA = process_data(INPUT_FILE)
    test_1a = 143
    test_2a = 123
    p1, TEST_INVALID = part1(TEST_DATA)
    if test_1a: assert p1 == test_1a, f"Part 1: {p1} is the wrong answer"
    p1, INVALID = part1(DATA)
    print(f"Part 1: {p1}")
    p2 = part2((TEST_DATA[0], TEST_INVALID))
    if test_2a: assert p2 == test_2a, f"Part 2: {p2} is the wrong answer"
    p2 = part2((DATA[0], INVALID))
    print(f"Part 2: {p2}")
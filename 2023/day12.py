from typing import List, Tuple
import re
from functools import reduce

def fresh_part1(data: Tuple[str, str]) -> int:
    r = 0
    springs, counts = data
    counts = [int(x) for x in counts.split(",")]

def new_part1(springs: str, counts: List[int], test: bool = False) -> int:

    stack: List[Tuple[str, int, int]] = []
    
    l = len(springs)
    srch = r"^\.*"
    for i in counts:
        srch += r"#{" + f"{i}" + r"}\.+"
    srch = srch[0:-1] + "*$"
    stack.append(("",0,0))
    while stack:
        i = len(stack[0][0])
        if i == l:
            break
        path, group_num, group_size = stack.pop(0)
        # if test: print(f"processing ('{path}', {group_num}, {group_size})")
        # find the "fixed points" and then find the possibilities for the samller sections and multiply
        if springs[i] == "?":
            if group_size:
                """ if we're in a group, we either need to continue adding hashes if not full size yet
                or close the group if at full size
                """
                # if test: print("in group_size fork")
                if group_num < len(counts):
                    if group_size < counts[group_num]:
                        stack.append((path + "#",group_num,group_size+1))
                    elif group_size == counts[group_num]:
                        stack.append((path + ".",group_num+1,0))
                else: #if we've maxed out group num, only add "."
                    stack.append((path + ".",group_num,0))
            else:
                # if test: print("in not group_size fork")
                stack.append((path+".",group_num,group_size))
                stack.append((path+"#",group_num,group_size+1))
        elif springs[i] == "#": # springs = "#" or "."
            if group_num < len(counts) and group_size < counts[group_num]:
                stack.append((path+"#",group_num,group_size+1))
        elif springs[i] == ".":
            if group_num < len(counts) and group_size == counts[group_num]:
                stack.append((path+".",group_num+1,0))
            else:
                stack.append((path+".",group_num,0))
        # if test: print(f"{springs}, {counts}: {stack}")
    # if test: print(f"{springs}, {counts}: returning {[x[0] for x in stack if re.match(srch, x[0])]}")
    if test: print("finished a row")
    return len([x[0] for x in stack if re.match(srch, x[0])])



def part2(springs: str, counts: List[int], test: bool = False) -> int:
    print(springs)
    new_springs = springs + "?" + springs + "?" + springs + "?" + springs + "?" + springs
    print(new_springs)
    new_counts = counts.copy()
    for x in range(4):
        new_counts.extend(counts)
    fixed_srch_a = r"#{" + f"{max(counts)}" + "}"
    fixed_srch_b = r"[?#]{" + f"{max(counts)}," + "}"
    initial_matches = re.finditer(fixed_srch_a, new_springs)
    count = 0
    matches = []
    spr_start = c_start = 0
    sections = [i for i in range(len(new_counts)) if new_counts[i] == max(counts)]
    section_options = []
    i = 0
    for m in initial_matches:
        count += 1
        matches.append(m)
    if not count:
        initial_matches = re.finditer(fixed_srch_b, new_springs)
        for m in initial_matches:
            matches.append(m)
    for m in matches:
        # print(m.start(0))
        # print(m.end(0))
        if len(springs) == m.end(0): #if len(matches) == 1:
            break
        sub_spring = new_springs[spr_start:m.end(0)]
        sub_count = new_counts[c_start:sections[i]+1]
        if test: print(sub_spring, sub_count)
        res = new_part1(sub_spring, sub_count)
        # assert res > 0, f"received 0 for {sub_spring, sub_count}!"
        # if i set up the forking solution I'm think of, I will actually need to
        # be able to have 0 as a response in case some combination leads to an end failure
        if test: print(res)
        section_options.append(res)
        spr_start = m.end(0)+1
        c_start = sections[i]+1
        i += 1
    sub_spring = new_springs[spr_start:]
    sub_count = new_counts[c_start:]
    if test: print(sub_spring, sub_count)
    res = new_part1(sub_spring, sub_count)
    if test: print(res)
    section_options.append(res)
    if test: print(f"{section_options}: {reduce(lambda x,y: x*y, section_options)}")
    if test: print(new_springs, new_counts)
    return reduce(lambda x,y: x*y, section_options) #new_part1(new_springs, new_counts, True)




if __name__ == "__main__":
    from datetime import datetime
    from pathlib import Path
    test = True
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    RAW_DATA = INPUT_FILE.read_text().strip().split("\n")
    # start = datetime.now()
    # print(f"Part 1: {sum(part1(x.split()) for x in DATA)}")
    # print(f"total time: {datetime.now()-start}")
    start = datetime.now()
    DATA = []
    for x in RAW_DATA:
        springs, counts = x.split()
        counts = [int(x) for x in counts.split(",")]
        DATA.append((springs, counts))
    print(f"Part 1: {sum(new_part1(x[0], x[1]) for x in DATA)}")
    print(f"total time: {datetime.now()-start}")
    print(f"Part 2: {sum(part2(x[0], x[1], test) for x in DATA)}")
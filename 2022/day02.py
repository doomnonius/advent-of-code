from typing import List

def part1(inp: List[str]) -> int:
    opp = 0
    me = 1 
    score = 0
    opp_table = ["A", "B", "C"]
    my_table = ["X", "Y", "Z"]
    while opp < len(inp):
        score += my_table.index(inp[me]) + 1
        opp_throw = opp_table.index(inp[opp])
        my_throw = my_table.index(inp[me])
        if opp_throw == my_throw:
            score += 3
        elif (opp_throw < my_throw and not (my_throw == 2 and opp_throw == 0)) or (opp_throw == 2 and my_throw == 0):
            score += 6
        else:
            score += 0
        opp += 2
        me += 2
    return score

def part2(inp: List[str]) -> int:
    opp = 0
    me = 1
    score = 0
    table = ["A","B","C"]
    while opp < len(inp):
        if inp[me] == "X":
            pts = table.index(inp[opp])
            if pts < 1: pts = 3
            score += pts
        elif inp[me] == "Y":
            score += 3 + table.index(inp[opp]) + 1
        else:
            pts = table.index(inp[opp]) + 2
            if pts > 3: pts = 1
            score += 6 + pts
        opp += 2
        me += 2
    return score

if __name__ == "__main__":
    import os, timeit
    FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    file = os.path.splitext(__file__)[0][-5:]
    with open(os.path.join(FILE_DIR, file + ".input")) as f:
        DATA = f.read().strip()
    DATA = [x.split() for x in DATA.split("\n\n")][0] # example code
    # print (DATA)
    print(f"Part 1: {part1(DATA)}")
    print(f"Part 2: {part2(DATA)}")
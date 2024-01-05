from datetime import datetime
from typing import List, Dict

def part2(rocks: List[str], cycles: int = 0) -> int:
    
    height = len(rocks)
    width = len(rocks[0])
        
    def weight_v(r: Dict[int, Dict[int, int]]) -> int:
        weight = 0
        for col in r:
            for key in r[col]:
                for i in range(r[col][key]):
                    weight += height - (key + i + 1)
        return weight
    
    def weight_h(r: Dict[int, Dict[int,int]]) -> int:
        weight = 0
        for col in r:
            weight += sum(x for x in r[col].values()) * (height-col)
        return weight
    
    vert = {x:{-1:0} for x in range(len(rocks))}
    hori = {x:{-1:0} for x in range(len(rocks[0]))}
    for row in range(len(rocks)):
        for col in range(len(rocks[row])):
            if rocks[row][col] == "#":
                hori[row][col] = 0
    for col in range(len(rocks[0])):
        curr_key = -1
        for row in range(len(rocks)):
            if rocks[row][col] == "#":
                vert[col][row] = 0
                curr_key = row
            elif rocks[row][col] == "O":
                vert[col][curr_key] += 1
    history = set()
    loop_check = []
    loop_start = 0
    while cycles:
        cycles -= 1
        # at this point, we're already titled north, so tilt west
        for col in vert:
            for solid in vert[col]:
                s = solid + 1
                if not vert[col][solid]:
                    continue
                for i in range(vert[col][solid]):
                    n = max(x for x in hori[s] if x <= col)
                    hori[s][n] += 1 # largest key in hori[s] less than col
                    s += 1
                vert[col][solid] = 0
        # now we want to tilt south
        for col in hori:
            for solid in hori[col]:
                s = solid + 1
                if not hori[col][solid]:
                    continue
                for i in range(hori[col][solid]):
                    n = max(x for x in vert[s] if x <= col)
                    vert[s][n] += 1
                    s += 1
                hori[col][solid] = 0
        # now we tilt east - remember to assume we're at the maximum, work from big to small
        for col in vert:
            s = height - 1
            for solid in list(vert[col].keys())[::-1]:
                if not vert[col][solid]:
                    s = solid - 1
                    continue
                for i in range(vert[col][solid]):
                    n = max(x for x in hori[s] if x <= col)
                    hori[s][n] += 1
                    s -= 1
                vert[col][solid] = 0
                s = solid - 1
        # then we record our weight
        w = weight_h(hori)
        if w in history:
            # print(f"on cycle {cycles}, weight {w} repeats")
            if cycles != loop_start - 1:
                loop_check = []
            loop_check.append(w)
            loop_start = cycles
            l = len(loop_check)
            if not l % 2 and l > 4:
                if loop_check[0:l//2] == loop_check[l//2:]:
                    # print(loop_check)
                    loop_length = l // 2
                    at = cycles % loop_length
                    print(loop_start - loop_length)
                    # print(at)
                    return(loop_check[at-1])
        else:
            history.add(w)
        # then we tilt north
        for col in hori:
            s = width - 1
            for solid in list(hori[col].keys())[::-1]:
                if not hori[col][solid]:
                    s = solid - 1
                    continue
                for i in range(hori[col][solid]):
                    n = max(x for x in vert[s] if x <= col)
                    vert[s][n] += 1
                    s -= 1
                hori[col][solid] = 0
                s = solid - 1
    return weight_v(vert)



if __name__ == "__main__":
    from pathlib import Path
    test = False
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    RAW_DATA = INPUT_FILE.read_text().strip()
    DATA = [x for x in RAW_DATA.split("\n")]
    print(f"Part 1: {part2(DATA)}")
    print(f"Part 2: {part2(DATA, 1000000000)}")
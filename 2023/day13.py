from typing import List, Tuple, Dict
from functools import reduce

def distance(x: str, y: str) -> Tuple[int, int]:
    d = 0
    a = 0
    for i in range(min(len(x), len(y))):
        if x[i] != y[i]:
            d += 1
            a = i
    return d, a

class Field:
    def __init__(self, data: str, m: bool = True):
        self.rows = data.split("\n")
        self.near_miss: List[Tuple[int, int]] = []
        if m: self.match()
        
    def match(self, old_hori: int = 1000000, old_vert: int = 1000000, new: bool = False, pr: bool = False):
        vert_poss = set()
        hori_poss = set()
        poss = set()
        for i in range(len(self.rows)):
            # check vert
            row: str = self.rows[i]
            for j in range(1,len(row)):
                if not i:
                    left = row[0:j][::-1]
                    right = row[j:]
                    d, c = distance(right, left)
                    if not d:
                        poss.add(j)
                    if d == 1:
                        self.near_miss.append((i, c, left, right))
                    vert_poss = poss.copy()
                else:
                    for p in poss:
                        left = row[0:p][::-1]
                        right = row[p:]
                        d, c = distance(right, left)
                        if d:
                            if p in vert_poss: vert_poss.remove(p)
                            if d == 1:
                                self.near_miss.append((i, c, left, right))
                    poss = vert_poss.copy()
                if new and old_vert in vert_poss:
                    vert_poss.remove(old_vert)
        if vert_poss: self.vert = max(vert_poss)
        else: self.vert = 0
        for i in range(len(self.rows)-1):
            d, c = distance(self.rows[i], self.rows[i+1])
            if d == 1:
                self.near_miss.append((i, i+1, c, self.rows[i], self.rows[i+1]))
            if not d:
                hori_poss.add(i)
                a = i-1
                b = i+2
                while a >= 0 and b < len(self.rows):
                    d, c = distance(self.rows[a], self.rows[b])
                    if d:
                        hori_poss.remove(i)
                        if d == 1:
                            self.near_miss.append((a, b, c, self.rows[a], self.rows[b]))
                        break
                    a -= 1
                    b += 1
            if new and old_hori in hori_poss:
                hori_poss.remove(old_hori)
            if hori_poss and new: break
        if hori_poss: self.hori = (max(hori_poss) + 1) * 100
        else: self.hori = 0

    def p2(self):
        opp = {"#" : ".", "." : "#"}
        alts = set()
        for m in self.near_miss:
            if len(m) == 4:
                left = m[2]
                right = m[3]
                row = m[0]
                i = m[1]
                i2 = 0
                if i < len(left)-1:
                    switch_left = left[0:i] + opp[left[i]] + left[i+1:]
                else:
                    switch_left = left[0:i] + opp[left[i]]
                alts.add((row, switch_left[::-1] + right))
                if i < len(right)-1:
                    switch_right = right[0:i] + opp[right[i]] + right[i+1:]
                else:
                    switch_right = right[0:i] + opp[right[i]]
                alts.add((row, left[::-1] + switch_right))
            else:
                top = m[3]
                bottom = m[4]
                row_t = m[0]
                row_b = m[1]
                i = m[2]
                alts.add((row_t, bottom))
                alts.add((row_b, top))
        backup = self.rows.copy()
        old_vert = self.vert
        old_hori = (self.hori//100)-1
        found = False
        for a in alts:
            row = a[0]
            replace = a[1]
            self.rows[row] = replace
            self.match(old_hori, old_vert, True)
            if not self.hori and not self.vert:
                self.vert, self.hori = old_vert, old_hori
            elif (self.hori or self.vert) and (self.vert != old_vert or self.hori != old_hori):
                if self.vert == old_vert and self.hori != old_hori: self.vert = 0
                if self.hori == old_hori and self.vert != old_vert: self.hori = 0
                found = True
                break
            self.rows = backup.copy()
        return self


if __name__ == "__main__":
    from datetime import datetime
    from pathlib import Path
    test = False
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    DATA = INPUT_FILE.read_text().strip()
    DATA = [Field(x, True) for x in DATA.split("\n\n")]
    print(f"Part 1: {sum(x.vert + x.hori for x in DATA)}")
    DATA = [x.p2() for x in DATA]
    print(f"Part 2: {sum(x.vert + x.hori for x in DATA)}") # not 40021, too high
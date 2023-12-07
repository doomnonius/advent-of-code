from typing import List
import functools

v = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
values = {k:v.index(k) for k in v}
vj = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
valuesj = {k:vj.index(k) for k in vj}

class Hand:
    def __init__(self, string:str):
        self.hand, value = string.split()
        self.value = int(value)
        self.strength = sorted([self.hand.count(k) for k in values], reverse=True)[0:5]
        self.opt_str = []
        j = self.hand.count("J")
        if not j:
            self.opt_str = self.strength
        else:
            s = sorted([self.hand.count(k) for k in vj[1:]], reverse = True)[0:5]
            self.opt_str = [s[0] + j]
            self.opt_str.extend(s[1:5])


    def __repr__(self):
        return self.hand
    
    def wins_tie(self, other, joke:bool = False):
        comp = 0
        if joke:
            while valuesj[self.hand[comp]] == valuesj[other.hand[comp]]:
                comp += 1
            if valuesj[self.hand[comp]] > valuesj[other.hand[comp]]:
                return 1
            return -1
        while values[self.hand[comp]] == values[other.hand[comp]]:
            comp += 1
        if values[self.hand[comp]] > values[other.hand[comp]]:
            return 1
        return -1
    
    def wins(self, other, joke:bool = False):
        comp = 0
        if joke:
            while self.opt_str[comp] == other.opt_str[comp]:
                comp += 1
                if comp == len(self.opt_str):
                    return self.wins_tie(other, True)
            if self.opt_str[comp] > other.opt_str[comp]:
                return 1
            elif self.opt_str[comp] < other.opt_str[comp]:
                return -1
        while self.strength[comp] == other.strength[comp]:
            comp += 1
            if comp == len(self.strength):
                return self.wins_tie(other)
        if self.strength[comp] > other.strength[comp]:
            return 1
        elif self.strength[comp] < other.strength[comp]:
            return -1

def compare(hand1:Hand, hand2:Hand) -> int:
    return hand1.wins(hand2)

def comparej(hand1:Hand, hand2:Hand) -> int:
    return hand1.wins(hand2, True)

def part1(hands: List[Hand], joker:bool = False) -> int:
    if not joker: hands.sort(key=functools.cmp_to_key(compare))
    else: hands.sort(key=functools.cmp_to_key(comparej))
    r = 0
    mult = 1
    for h in hands:
        r += (mult * h.value)
        mult += 1
    return r

if __name__ == "__main__":
    import os, timeit
    from pathlib import Path
    INPUT_FILE = Path(__file__).with_suffix(".input")
    RAW_DATA = INPUT_FILE.read_text().strip()
    DATA = [Hand(x) for x in RAW_DATA.split("\n")] # example code
    print(f"Part 1: {part1(DATA)}")
    print(f"Part 2: {part1(DATA, True)}")
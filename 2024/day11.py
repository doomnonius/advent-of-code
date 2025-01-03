from typing import List, Dict, Tuple

class Rock:
    def __init__(self, n, d=0):
        self.data = n
        self.left = None
        self.right = None
        self.depth = d
    
    def blink(self, rocks: Dict) -> Tuple:
        if not self.data:
            self.left = Rock(1, self.depth + 1)
            return
        l = len(str(self.data))
        if l % 2 == 0:
            self.left = Rock(int(self.data//(10 ** (l/2))), self.depth + 1)
            self.right = Rock(int(self.data - self.left.data * (10 ** (l/2))), self.depth + 1)
            return
        self.left = Rock(self.data * 2024, self.depth + 1)
        return (x for x in [self.left, self.right] if x)
    
    def leng(self):
        pass
    
    def __hash__(self):
        return hash(self.data)
    

def part1(rocks: List[Rock], w=25, t=False) -> int:
    seen: Dict[int, Rock] = dict()
    r = 0
    for r in rocks:
        seen[r.data] = r
        c = w
        while c > 0:
            for r in rocks:
                for s in r.blink(seen):
                    seen[s.data] = s
            c -= 1
        r += r.leng()
    return r


def process_data(data: str) -> List[Rock]:
    nums = [Rock(int(x)) for x in data.strip().split()]
    return nums

if __name__ == "__main__":
    from datetime import datetime
    from pathlib import Path
    from helpers import import_files
    TEST_FILE, INPUT_FILE = import_files(Path(__file__))
    TEST_DATA = process_data(TEST_FILE)
    DATA = process_data(INPUT_FILE)
    test_1a = 55312
    test_2a = 0
    p1 = part1(TEST_DATA)
    if test_1a: assert p1 == test_1a, f"Part 1: {p1} is the wrong answer"
    p1 = part1(DATA)
    print(f"Part 1: {p1}")
    p2 = part1(DATA, 75)
    print(f"Part 2: {p2}")
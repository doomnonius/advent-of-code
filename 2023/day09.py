from typing import List

class Sequence:
    def __init__(self, inp:str) -> None:
        self.ords = [[int(x) for x in inp.split()]]
        while {x for x in self.ords[-1]} != {0}:
            self.ords.append([self.ords[-1][i+1]-self.ords[-1][i] for i in range(len(self.ords[-1])-1)])
        for i in range(len(self.ords)-1,0,-1):
            next = self.ords[i-1]
            next.append(self.ords[i][-1] + next[-1])
        # print(self.ords[0])
    
    def extra_backwards(self) -> int:
        ords_b = [x[::-1] for x in self.ords]
        # for x in ords_b:
            # print(x)
        for i in range(len(ords_b)-1,0,-1):
            next = ords_b[i-1]
            next.append(next[-1] - ords_b[i][-1])
        # print(ords_b[0])
        return ords_b[0][-1]
         

def part1(data: List[Sequence]) -> int:
    return sum(x.ords[0][-1] for x in data)





def part2(data: List[Sequence]) -> int:
    return sum(x.extra_backwards() for x in data)




if __name__ == "__main__":
    import os, timeit
    from pathlib import Path
    test = False
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    DATA = INPUT_FILE.read_text().strip()
    DATA = [Sequence(x) for x in DATA.split("\n")] # example code
    print(f"Part 1: {part1(DATA)}") # 546681361 to low
    print(f"Part 2: {part2(DATA)}")
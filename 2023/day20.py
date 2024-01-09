from typing import List, Tuple, Dict
from day08 import lcm

class Node:
    def __init__(self, data: str):
        self.inputs = {}
        self.state = False
        if data[0] == "%":
            self.type = 0 # flip-flop
            self.name = data[1:3]
        elif data[0] == "&":
            self.type = 1 # converter
            self.name = data[1:3]
        else:
            self.type = 2 # broadcaster
            self.name = "ro"
        self.outputs = data[data.index(">") + 2:].split(", ")
        # print(self.outputs)

    def run(self, wave: int, source: str) -> List[Tuple[int, str]]:
        if self.type == 0:
            if wave:
                return []
            self.state = not self.state
            if not self.state:
                return [(0, x, self.name) for x in self.outputs]
            else:
                return [(1, x, self.name) for x in self.outputs]
        elif self.type == 1:
            self.inputs[source] = wave
            if sum(v for v in self.inputs.values()) == len(self.inputs):
                return [(0, x, self.name) for x in self.outputs]
            else:
                return [(1, x, self.name) for x in self.outputs]
        else:
            return [(wave, x, self.name) for x in self.outputs]

        

def part1(data: Dict[str,Node], runs: int) -> int:
    lows = 0
    highs = 0
    final_node = [x for x in data.values() if "rx" in x.outputs][0].name
    data["sources"] = {x:[] for x in data[final_node].inputs}
    c = 0
    count = 0
    while count < runs:
        stack = [(0, "ro", "button")]
        while stack:
            # print(stack)
            wave, dest, source = stack.pop(0)
            if wave:
                highs += 1
            else:
                lows += 1
            c += 1
            if dest not in data:
                continue
            if source in data["sources"] and wave:
                data["sources"][source].append(count)
            for x in data[dest].run(wave, source):
                stack.append(x)
        count += 1
    print(data["sources"])
    return lows * highs


def part2(data: Dict[str,Node]) -> int:
    hits = 1000
    target = 4
    while True:
        hits += 1
        stack = [(0, "ro", "button")]
        while stack:
            # print(stack)
            wave, dest, source = stack.pop(0)
            if dest not in data:
                if not wave:
                    return hits
                else:
                    continue
            if source in data["sources"] and wave:
                data["sources"][source].append(hits)
            for x in data[dest].run(wave, source):
                stack.append(x)
        if sum(len(x) for x in data["sources"].values()) == target:
            a, b, c, d = (x[0] for x in data["sources"].values())
            return lcm(lcm(a, b), lcm(c, d))


if __name__ == "__main__":
    from datetime import datetime
    from pathlib import Path
    test = False
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    RAW_DATA = INPUT_FILE.read_text().strip().split("\n")
    DATA = {x[1:3]:Node(x) for x in RAW_DATA} # example code
    for node in DATA.values():
        for out in node.outputs:
            if out in DATA:
                DATA[out].inputs[node.name] = 0
        # if out in DATA: print(DATA[out].inputs)
    print(f"Part 1: {part1(DATA, 1000)}") # not 66621, too low
    print(f"Part 2: {part2(DATA)}")
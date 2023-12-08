from typing import List
from math import gcd

class Node:
    def __init__(self, inp: str) -> None:
        # print(inp)
        self.id, forks = inp.split(" = ")
        self.left, self.right = forks[1:-1].split(", ")

    def __hash__(self):
        return hash((self.id))
        
        

def part1(steps: str, nodes: List[Node]) -> int:
    node_dict = {x.id:x for x in nodes}
    current_node = node_dict["AAA"]
    count = 0
    while True:
        for i in range(len(steps)):
            if steps[i] == "L":
                current_node = node_dict[current_node.left]
            else:
                current_node = node_dict[current_node.right]
            count += 1
            if current_node.id == "ZZZ":
                return count

def lcm(x: int, y: int) -> int:
    if gcd(x, y) > 1:
        return (x * y) // gcd(x, y)
    else:
        return (x * y)

def part2(steps: str, nodes: List[Node]) -> int:
    # needs optimization: idea is the "bus solution", find each individual loop, calculate LCM, ???, profit
    node_dict = {x.id:x for x in nodes}
    starting_nodes = [x for x in nodes if x.id[-1] == "A"]
    z_map = {x:[] for x in starting_nodes}
    count = 0
    for x in starting_nodes:
        next_node = x
        zs = z_map[x]
        while count < 100000:
            for i in range(len(steps)):
                if steps[i] == "L":
                    next_node = node_dict[next_node.left]
                else:
                    next_node = node_dict[next_node.right]
                count += 1
                if next_node.id[-1] == "Z":
                    zs.append(count)
        count = 0
    stops = [min(x) for x in z_map.values()]
    r = stops[0]
    for i in range(1,len(stops)):
        l = lcm(r, stops[i])
        r = l
    return r






if __name__ == "__main__":
    from pathlib import Path
    test = False
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    DATA = INPUT_FILE.read_text().strip()
    STEPS, NODES = DATA.split("\n\n")
    NODES = [Node(x) for x in NODES.split("\n")]
    print(f"Part 1: {part1(STEPS, NODES)}") # not 3523, too low
    print(f"Part 2: {part2(STEPS, NODES)}")
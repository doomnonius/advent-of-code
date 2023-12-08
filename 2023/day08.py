from typing import List, Dict

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

def part2(steps: str, nodes: List[Node]) -> int:
    # needs optimization
    node_dict = {x.id:x for x in nodes}
    current_nodes = [x for x in nodes if x.id[-1] == "A"]
    count = 0
    while True:
        for i in range(len(steps)):
            next_nodes = []
            for node in current_nodes:
                if steps[i] == "L":
                    next_nodes.append(node_dict[node.left])
                else:
                    next_nodes.append(node_dict[node.right])
            count += 1
            assert len(current_nodes) == len(next_nodes)
            current_nodes = next_nodes
            check = {k[-1] for k in node_dict.keys()}
            if len(check) == 1 and check == {"Z"}:
                return count




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
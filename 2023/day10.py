from typing import List, Set, Dict, Tuple

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        # if not other: return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

    def right(self):
        return Coord(self.x+1, self.y)
    
    def left(self):
        return Coord(self.x-1, self.y)
    
    def up(self):
        return Coord(self.x, self.y-1)
    
    def down(self):
        return Coord(self.x, self.y+1)
    
    def neighbors(self) -> Dict:
        return {"u": self.up(), "d": self.down(), "l": self.left(), "r": self.right()}

class Pipe:
    def __init__(self, inp: str, loc: Coord) -> None:
        self.loc = loc
        self.data = inp
        if self.data == "J":
            self.last = self.loc.up()
            self.next = self.loc.left()
        elif self.data == "|":
            self.next = self.loc.up()
            self.last = self.loc.down()
        elif self.data == "F":
            self.next = self.loc.down()
            self.last = self.loc.right()
        elif self.data == '-':
            self.last = self.loc.left()
            self.next = self.loc.right()
        elif self.data == "L":
            self.last = self.loc.up()
            self.next = self.loc.right()
        elif self.data == "7":
            self.next = self.loc.left()
            self.last = self.loc.down()
        else:
            self.next = Coord(-1,-1)
            self.last = Coord(-1,-1)
        self.neighbors = [self.next, self.last]
        
    
    def __repr__(self) -> str:
        return f"{self.loc.x, self.loc.y}: {self.data}"

def part1(data: Dict[Coord,Pipe], test:bool = False) -> int:
    s = [x for x in data.values() if x.data == "S"][0]
    connections = [x for x in data.values() if s.loc in x.neighbors]
    s.next, s.last = connections[0], connections[1]
    s.neighbors = connections
    s.data = "L"
    if test: s.data = "F"
    one, two = s.next.loc, s.last.loc
    count = 1
    visited = {s.loc}
    while one != two:
        new_one = 0
        for x in data[one].neighbors:
            if x not in visited:
                new_one = x
        assert new_one, f"next ONE not found at {one}, see {data[one].neighbors}"
        new_two = 0
        for x in data[two].neighbors:
            if x not in visited:
                new_two = x
        assert new_two, f"next TWO not found at {two}, see {data[two].neighbors}" 
        visited.add(one)
        visited.add(two)
        one = new_one
        two = new_two
        count += 1
    return count, visited

history = set()
stack: List[Tuple[Coord, int]] = [] # don't need to track # of steps, but may need to track state while squeezing
squeeze = { # always look "right" relatively speaking
    "|" : { # this part will basically function like a state machine?
        4 : ["|", "F", "L"],
        2 : ["|", "7", "J"],
        3 : [4], # stops movement in either L or R, but could turn either way
        1 : [2]
        }, # J|F-L7
    "F" : {
        4 : [1], # stops movement up, but could turn right sometimes
        2 : ["|", "7", "J"],
        3 : ["J", "L", "-"],
        1 : [2] # stops movement right, but could turn either way
        }, # J|F-L7
    "L" : {
        4 : [1], # stops movement up, but can turn either way
        2 : ["|", "7", "J"],
        3 : [4], # stops movement left, but can turn right
        1 : ["-", "7", "F"]
        }, # J|F-L7
    "J" : {
        4 : ["|", "F", "L"],
        2 : [3], # stops movement down but can turn one way
        3 : [4], # stops movement left but can turn either way
        1 : ["-", "7", "F"]
        }, # J|F-L7
    "7" : {
        4 : ["|", "F", "L"],
        2 : [3], # stops movement down but can turn either way
        3 : ["J", "L", "-"],
        1 : [2] # stops movement right but can turn one way
        }, # J|F-L7
    "-" : {
        4 : [1], # stops movement up, but can turn either way
        2 : [3], # stops movement up, but can turn either way
        3 : ["J", "L", "-"],
        1 : ["-", "7", "F"]
        }
}

def part2(data: Dict[Coord,Pipe], visited: Set[Coord], test: bool = False) -> int:
    """ Latest though: can I make a mapping function with "squeeze between" functionality?
        If I have that, then I can go around the edge of the map, and find all "." and map from each one,
        "squeezing" in to find what else I can reach in the middle. Then the answer would be
        length(total) - (visited | history).
    """

    def next_moves(loc: Coord, state: int) -> None:
        """ doesn't return anything, just adds to the stack
        """
        if test: print(f"moved into next_moves, with {loc}, state: {state}")
        d = loc.neighbors()
        for n in d.keys(): # u, d, l, r
            if d[n] in data.keys():
                # at this point, if we have a state established, we should not be adding all neighbors to stack
                if data[d[n]].data == ".":
                    if n not in history:
                        stack.append((d[n], 0))
                        print(f"just added {stack[-1]} to stack")
                else:
                    if not state:
                        # determine the state if this is the first time we've hit
                        if n == "u": state = 4
                        elif n == "d": state = 2
                        elif n == "l": state = 3
                        elif n == "r": state = 1
                    for s in find_state(d[n], state):
                        if n not in history:
                            stack.append((d[n], s))
                            print(f"just added {stack[-1]} to stack")
    
    def find_state(c: Coord, state: int) -> List[int]:
        """ determines what potential states can be next returned as a list
        up: 4, down: 2, left: 3, right: 1
        """
        comp_list = squeeze[data[c].data]
        if state == 4:
            comp = c.right()
        elif state == 3:
            comp = c.up()
        elif state == 2:
            comp = c.left()
        elif state == 1:
            comp = c.down()
        else:
            print(f"find_state called with invalid state input {state}")
            return []
        d = data[comp].data
        if d == ".":
            if d not in history:
                stack.append((comp, 0))
                print(f"just added {stack[-1]} to stack")
            return [state]
        if d in comp_list:
            return [state]
        else:
            return comp_list


    for k in data.keys():
        if k not in visited:
            data[k].data = "."
    max_x = max(z.x for z in data.keys())
    max_y = max(z.y for z in data.keys())
    top = {z for z in data.keys() if z.y == 0 and data[z].data == "."}
    if test: print(f"top: {top}")
    bottom = {z for z in data.keys() if z.y == max_y and data[z].data == "."}
    if test: print(f"bottom: {bottom}")
    left = {z for z in data.keys() if z.x == 0 and data[z].data == "."}
    if test: print(f"left: {left}")
    right = {z for z in data.keys() if z.x == max_x and data[z].data == "."}
    if test: print(f"right: {right}")
    edges = top | bottom | left | right
    if test: print(f"edges: {edges}")
    for z in list(edges):
        if z not in history:
            if test: print(f"An item in edges is being processed: {z}")
            history.add(z)
            next_moves(z, 0)
            while stack:
                co, state = stack.pop(0)
                if co in history:
                    continue
                history.add(co)
                next_moves(co, state)


    return len(data) - len(visited | history)




if __name__ == "__main__":
    # import os, timeit
    from pathlib import Path
    test = True
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    RAW_DATA = INPUT_FILE.read_text().strip().split()
    DATA = {}
    for row in range(len(RAW_DATA)):
        for column in range(len(RAW_DATA[row])):
            DATA[Coord(column, row)] = (Pipe(RAW_DATA[row][column], Coord(column, row)))
    print(f"total size: {len(DATA)}")
    p1, visited = part1(DATA)
    print(f"Part 1: {p1}") #6724 is too low; off by one b/c forgot I start
    print(f"Part 2: {part2(DATA, visited, test)}") # not 1516, too high; somehow visited is wrong
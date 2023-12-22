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
    
    def neighbors(self):
        return [self.up(), self.down(), self.left(), self.right()]
    
    def neighbors_d(self) -> Dict:
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
    s: Pipe = [x for x in data.values() if x.data == "S"][0]
    connections: List[Pipe] = [x for x in data.values() if s.loc in x.neighbors]
    s.next, s.last = connections[0], connections[1]
    s.neighbors = connections
    # define s.data
    con_locs = [x.loc for x in connections]
    if s.loc.up() in con_locs:
        if s.loc.down() in con_locs:
            s.data = "|"
        elif s.loc.right() in con_locs:
            s.data = "L"
        elif s.loc.left() in con_locs:
            s.data = "J"
    elif s.loc.down() in con_locs:
        if s.loc.right() in con_locs:
            s.data = "F"
        elif s.loc.left() in con_locs:
            s.data = "7"
    elif s.loc.right() in con_locs:
        if s.loc.left() in con_locs:
            s.data = "-"
    assert s.data != "S", "WARNING! S.data not properly set"
    one, two = s.next.loc, s.last.loc # one is next, last, two is last, next
    count = 1
    visited = {s.loc}
    while one != two:
        new_one = 0
        for x in data[one].neighbors:
            if x not in visited:
                data[one].next = data[x]
                new_one = x
            else:
                data[one].last = data[x]
        assert new_one, f"next ONE not found at {one}, see {data[one].neighbors}"
        new_two = 0
        for x in data[two].neighbors:
            if x not in visited:
                data[two].last = data[x]
                new_two = x
            else:
                data[two].next = data[x]
        assert new_two, f"next TWO not found at {two}, see {data[two].neighbors}" 
        visited.add(one)
        visited.add(two)
        one = new_one
        two = new_two
        count += 1
    visited.add(one)
    for x in data[one].neighbors:
        if data[one] == data[x].next:
            data[one].last = data[x]
        else:
            data[one].next = data[x]
    # test that we properly loop
    loop_count = 0
    loop_start = s
    next_one = s.next
    while next_one != loop_start:
        next_one = next_one.next
        loop_count += 1
        if loop_count > 100000:
            print("Error! Infinite loop!")
    return count, visited

history: Set[Coord] = set()
stack: List[Coord] = [] # don't need to track # of steps
around: List = []

dot_dir = {
    "u" : ["J"],# "|", "7"],
    "d" : ["F"],# "|", "L"],
    "l" : ["7"],# "-", "F"],
    "r" : ["L"]#, "-", "J"]
    }

next_state = {
    4:1,
    3:4,
    2:3,
    1:2
}

def part2(data: Dict[Coord,Pipe], visited: Set[Coord], test: bool = False) -> int:
    """ Latest though: can I make a mapping function with "squeeze between" functionality?
        If I have that, then I can go around the edge of the map, and find all "." and map from each one,
        "squeezing" in to find what else I can reach in the middle. Then the answer would be
        length(total) - (visited | history).
    """

    #used output() to bug test when test input gave right answer and real input didn't
    def output() -> None:
        if test:
            count = 10
        else:
            count = 140
        for k in data.keys(): # thankfully the keys are sorted properly
            # if in history but not visited, make O, else I
            d = data[k].data
            count -= 1
            if k in visited:
                print(d, end="")
            elif k in history:
                print("O", end="")
            else:
                print("I", end="")
            if count == 0:
                print()
                if test: count = 10
                else: count = 140

    def perimeter(p: Pipe, dir: int) -> None:
        """ walks along the perimeter of the pipes, adding all "."s to the stack
        """
        curr_pipe = p
        assert dir > 0, f"dir is {dir}"
        # safe to assume that I will move at least one more step in direction already heading
        if dir == 1:
            if curr_pipe.next.loc == curr_pipe.loc.right():
                next_pipe = curr_pipe.next
            else:
                # completely reverse the direction of the loop
                for v in data.values():
                    if v.data != ".":
                        v.next, v.last = v.last, v.next
                next_pipe = curr_pipe.next
                assert next_pipe.loc == curr_pipe.loc.right(), "Neither next nor last is to the right."
        elif dir == 2:
            if curr_pipe.next.loc == curr_pipe.loc.down():
                next_pipe = curr_pipe.next
            else:
                # completely reverse the direction of the loop
                for v in data.values():
                    if v.data != ".":
                        v.next, v.last = v.last, v.next
                next_pipe = curr_pipe.next
                assert next_pipe.loc == curr_pipe.loc.down(), "Neither next nor last is down."
        elif dir == 3:
            if curr_pipe.next.loc == curr_pipe.loc.left():
                next_pipe = curr_pipe.next
            else:
                # completely reverse the direction of the loop
                for v in data.values():
                    if v.data != ".":
                        v.next, v.last = v.last, v.next
                next_pipe = curr_pipe.next
                assert next_pipe.loc == curr_pipe.loc.left(), "Neither next nor last is to the left."
        elif dir == 4:
            if curr_pipe.next.loc == curr_pipe.loc.up():
                next_pipe = curr_pipe.next
            else:
                # completely reverse the direction of the loop
                for v in data.values():
                    if v.data != ".":
                        v.next, v.last = v.last, v.next
                next_pipe = curr_pipe.next
                assert next_pipe.loc == curr_pipe.loc.up(), "Neither next nor last is up."
        assert type(next_pipe) == Pipe, "ERROR! next_pipe not a pipe"
        turned = True
        temp_history: Set[Coord] = set()
        while next_pipe != p:
            if dir == 1:
                comp = curr_pipe.loc.down()
            elif dir == 2:
                comp = curr_pipe.loc.left()
            elif dir == 3:
                comp = curr_pipe.loc.up()
            elif dir == 4:
                comp = curr_pipe.loc.right()
            else:
                assert False, f"invalid dir: {dir}"
            if comp in data.keys() and data[comp].data == ".":
                if comp not in temp_history:
                    stack.append(comp)
                    temp_history.add(comp)
            # now I need to change dir if this is a corner - and only change dir
            d = curr_pipe.data
            if d in ["7", "L", "J", "F"] and not turned:
                if d == "7":
                    if dir == 4:
                        dir = 3
                    elif dir == 1:
                        dir = 2
                    else:
                        assert False, f"d is {d} and dir is {dir}"
                elif d == "L":
                    if dir == 2:
                        dir = 1
                    elif dir == 3:
                        dir = 4
                    else:
                        assert False, f"d is {d} and dir is {dir}"
                elif d == "J":
                    if dir == 2:
                        dir = 3
                    elif dir == 1:
                        dir = 4
                    else:
                        assert False, f"d is {d} and dir is {dir}"
                elif d == "F":
                    if dir == 4:
                        dir = 1
                    elif dir == 3:
                        dir = 2
                    else:
                        assert False, f"d is {d} and dir is {dir}"
                turned = True
            else:
                curr_pipe = next_pipe
                next_pipe = curr_pipe.next
                turned = False
        around.append("")

    def next_moves(loc: Coord) -> None:
        """ doesn't return anything, just adds to the stack
        """
        d = loc.neighbors_d()
        for n in d.keys(): # u, d, l, r
            if d[n] in data.keys():
                n_data = data[d[n]].data # neighbor data
                h_data = data[loc].data # here data
                # simplest outcome
                if h_data == "." and n_data == ".":
                    if d[n] not in history: 
                        stack.append(d[n])
                if h_data == "." and n_data != "." and not around:
                    # figure out proper state
                    new_state = 0
                    if n == "u" and n_data in dot_dir[n]: new_state = 4
                    elif n == "d" and n_data in dot_dir[n]: new_state = 2
                    elif n == "l" and n_data in dot_dir[n]: new_state = 3
                    elif n == "r" and n_data in dot_dir[n]: new_state = 1
                    if new_state:
                        perimeter(data[d[n]], new_state)

    # main code of p2
    for k in data.keys():
        if k not in visited:
            data[k].data = "."
    max_x = max(z.x for z in data.keys())
    max_y = max(z.y for z in data.keys())
    top = {z for z in data.keys() if z.y == 0 and data[z].data == "."}
    bottom = {z for z in data.keys() if z.y == max_y and data[z].data == "."}
    left = {z for z in data.keys() if z.x == 0 and data[z].data == "."}
    right = {z for z in data.keys() if z.x == max_x and data[z].data == "."}
    edges = top | bottom | left | right
    for z in list(edges):
        if z not in history:
            history.add(z)
            next_moves(z)
            while stack:
                co = stack.pop(0)
                if co in history:
                    continue
                history.add(co)
                next_moves(co)
    # output()
    return len(data) - len(visited | history)

if __name__ == "__main__":
    # import os, timeit
    from pathlib import Path
    test = False
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    RAW_DATA = INPUT_FILE.read_text().strip().split()
    DATA = {}
    for row in range(len(RAW_DATA)):
        for column in range(len(RAW_DATA[row])):
            DATA[Coord(column, row)] = (Pipe(RAW_DATA[row][column], Coord(column, row)))
    p1, visited = part1(DATA, test)
    print(f"Part 1: {p1}") #6724 is too low; off by one b/c forgot I start
    print(f"Part 2: {part2(DATA, visited, test)}") # not 1516, too high; my solution was way off; 580 also too high; 387 also too high
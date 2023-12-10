from typing import List, Set, Dict

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{(self.x, self.y)}"

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __mul__(self, other: int):
        return Coord(self.x * other, self.y * other)
    
    def full_neighbors(self):
        return [self + Coord(0, 1), self + Coord(0, -1), self + Coord(1, 0), self + Coord(-1, 0), self + Coord(1, 1), self + Coord(1, -1), self + Coord(-1, -1), self + Coord(-1, 1)]

    def neighbors(self):
        return [self + Coord(0, 1), self + Coord(0, -1), self + Coord(1, 0), self + Coord(-1, 0)]

    def __eq__(self, other):
        try:
            return self.x == other.x and self.y == other.y
        except:
            print(other)
            return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))
    
    def __lt__(self, other):
        if self.y < other.y:
            return True
        if self.y == other.y:
            if self.x < other.x:
                return True
        return False
    
    def __gt__(self, other):
        if self.y > other.y:
            return True
        if self.y == other.y:
            if self.x > other.x:
                return True
        return False

class Elf:
    def __init__(self, inp) -> None:
        self.health = 200
        self.attack = 3
        self.loc = inp

class Goblin:
    def __init__(self, inp) -> None:
        self.health = 200
        self.attack = 3
        self.loc = inp


def part1(walls: Set[Coord], elves: Set[Elf], goblins: Set[Goblin], test: bool = False) -> int:
    """ solves part 1
    """
    def next_moves(loc: Coord, count: int, stack: List, history: Set, start: Coord):
        """ no returns, just adds to stack and history"""
        for n in loc.neighbors():
            if n not in walls and n not in history and n not in [x.loc for x in elves | goblins]:
                if not count:
                    start = n
                stack.append((count + 1, n, start))
                history.add(n)
    
    def find_path(start: Coord, end: Set[Coord], stack: List, history: Set):
        # remember that you need to check for each path that is tied for shortest
        # this still doesn't do quite what I want it to - I need it to return just the next step
        next_moves(start, 0, stack, history, Coord(-1,-1))
        # if test: print(end)
        possibles = []
        while True:
            # if test: print(history)
            least = 9999
            count, loc, first = stack.pop(0)
            # if test: print(count, loc, first)
            if loc in end:
                # if test: print("we're at a goal!")
                possibles.append((first, loc))
                least = min(least, count)
                if len(end) == 1:
                    return possibles[0][0]
            next_moves(loc, count, stack, history, first)
            if count > least or not len(stack):
                if not len(possibles): return start
                # if test: print(f"possibles: {possibles}")
                closest = min(x[1] for x in possibles)
                return sorted(x[0] for x in possibles if x[1] == closest)[0]
    
    # reading order means prioritize ULRD
    rounds = 0
    # each unit moves, then attacks
    # remember : update the location of a thing as soon as it has moved - assuming yes for now
    while True:
        # because creatures move in reading order, need to order moves based on combined set
        creatures: List[Coord] = sorted([x.loc for x in elves | goblins])
        if test: print(f"creatures: {creatures}")
        elf_locs: List[Coord] = [x.loc for x in elves]
        goblin_locs: List[Coord] = [x.loc for x in goblins]
        if not elf_locs or not goblin_locs:
            break
        for x in creatures:
            if test: print(x)
            # move phase : requires implementation of mapping
            # check if the creature NEEDS to move or CAN move
            stuck = True # assume stuck
            engaged = False # assume not engaged
            if x in elf_locs:
                elf = True
                goblin = False
                c = [y for y in elves if y.loc == x][0]
            else:
                goblin = True
                elf = False
                c = [y for y in goblins if y.loc == x][0]
            enemies = []
            for n in x.neighbors():
                if (goblin and n in elf_locs) or (elf and n in goblin_locs):
                    stuck = False
                    engaged = True
                    enemies.append(n)
                    continue
                if n not in walls and n not in elf_locs and n not in goblin_locs:
                    stuck = False
            if engaged:
                if test: print("won't move, engaged")
            if stuck:
                if test: print("won't move, stuck")
                continue
            if elf and not engaged:
                targets = set()
                for y in goblin_locs:
                    for n in y.neighbors():
                        if n not in walls:
                            targets.add(n)
                if not len(targets): continue
                next_pos = find_path(x, targets, [], set())
                if next_pos in targets:
                    engaged = True
                    enemies = [n for n in next_pos.neighbors() if n in goblin_locs]
                if test: print(f"next: {next_pos}")
                # find elf in set, update its loc, then update elf_locs
                if next_pos != x:
                    c.loc = next_pos
                    if test: print(f"old pos: {x} new pos: {c.loc}")
            if goblin and not engaged:
                targets = set()
                for y in elf_locs:
                    for n in y.neighbors():
                        if n not in walls:
                            targets.add(n)
                if not len(targets): continue
                next_pos = find_path(x, targets, [], set())
                if next_pos in targets:
                    engaged = True
                    enemies = [n for n in next_pos.neighbors() if n in goblin_locs]
                if test: print(f"next: {next_pos}")
                # update goblin set then goblin_locs
                if next_pos != x:
                    c.loc = next_pos
            # attack phase : requires checking health of all adjacent opponents
            if engaged:
                # get adjacent enemies health and coords
                if elf:
                    targets = [y for y in goblins if y.loc in enemies]
                else:
                    targets = [y for y in elves if y.loc in enemies]
                assert len(targets) > 0, "no targets found for engaged enemy!"
                if len(targets) == 1:
                    targets[0].health -= c.attack
                    # continue
                healths = {y:y.health for y in targets}
                health_target = min(v for v in healths.values())
                # find the lowest health dude
                targets = [y for y in goblins if y in healths.keys() and y.health == health_target]
                targets.sort(key=lambda z: z.loc)
                if len(targets) == 1:
                    targets[0].health -= c.attack
                else:
                    targets[0].health -= c.attack
                    # code to find which one is reading order first
        if test and rounds == 2: break
        # after each creature has acted, increase the round counter
        rounds += 1
        if test: print(f"round {rounds} over")
    return rounds # round * total health of remaining units





def part2(nums: List[int]) -> int:
    return




if __name__ == "__main__":
    # import os, timeit
    from pathlib import Path
    test = True
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    RAW_DATA = INPUT_FILE.read_text().strip().split("\n")
    walls = set()
    goblins = set()
    elves = set()
    for row in range(len(RAW_DATA)): # y
        for column in range(len(RAW_DATA[row])): # x
            c = RAW_DATA[row][column]
            if c == "#":
                walls.add(Coord(column, row))
            elif c == "G":
                goblins.add(Goblin(Coord(column, row)))
            elif c == "E":
                elves.add(Elf(Coord(column, row)))
    print(f"Part 1: {part1(walls, elves, goblins, test)}")
    # print(f"Part 2: {part2(DATA)}")
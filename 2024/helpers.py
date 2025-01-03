from typing import Tuple, List

def import_files(day) -> Tuple[str, str]:
    TEST_FILE = day.with_suffix(".testinput").read_text()
    INPUT_FILE = day.with_suffix(".input").read_text()
    return TEST_FILE, INPUT_FILE

class Chunk:
    def __init__(self, id: int, s: int, l: int):
        self.start: int = s
        self.id: int = id
        self.leng: int = l

    def fill(self, spaces: List, t=False) -> List:
        for i in range(len(spaces)):
            s = spaces[i]
            if self.start < s.start:
                return
            if s.leng < self.leng:
                continue
            else:
                self.start = s.start
                s.leng -= self.leng
                s.start += self.leng
                if not s.leng:
                    spaces.pop(i)
                return
    
    def value(self):
        return sum((self.start + r) * self.id for r in range(self.leng))
    
    def __repr__(self):
        return f"{self.id}" * self.leng
    
    def __hash__(self):
        return hash((self.id, self.leng))
    
    def __lt__(self, other):
        return self.start < other.start

    def __gt__(self, other):
        return self.start > other.start

class Space:
    def __init__(self, s: int, l: int):
        self.start: int = s
        self.leng: int = l

    def fill(self, chunks: List[Chunk], t=False) -> List[Chunk]:
        r = []
        while self.leng:
            top = chunks.pop()
            if self.start > top.start:
                r.append(top)
                break
            if top.leng and top.leng <= self.leng:
                top.start = self.start
                self.leng -= top.leng
                self.start += top.leng
                r.append(top)
            elif top.leng: #top.leng > self.leng
                chunks.append(Chunk(top.id, top.start, top.leng - self.leng))
                top.start = self.start
                top.leng = self.leng
                self.leng = 0
                r.append(top)
            else:
                self.leng = 0
                r.append(top)
        return r

    def __lt__(self, other):
        return self.start < other.start

    def __repr__(self):
        return f"start: {self.start}, len: {self.leng}"
    
    def __gt__(self, other):
        return self.start > other.start

class Coord:
    def __init__(self, x, y, char = "."):
        self.x = x
        self.y = y
        self.char = char

    def __repr__(self):
        return f"{(self.x, self.y, self.char)}"

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y, other.char)
    
    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y)

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
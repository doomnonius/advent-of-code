from typing import Tuple

def import_files(day) -> Tuple[str, str]:
    TEST_FILE = day.with_suffix(".testinput").read_text()
    INPUT_FILE = day.with_suffix(".input").read_text()
    return TEST_FILE, INPUT_FILE

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
from itertools import permutations

inp = "#.#.###.#.#....#..##.#.........#..#..#..#.#..#.....#.##.##.##.##.##..#...#...##.#...#.#####...###.#.#.#..#####.###.#.#.####.#####.#.#.#.##.#.##...####.#.##.##....###..#.#..#..#..###...##....#.#...##.#.#...####.....#.#######..##.##.#..#.###.#..###.#.#..##.....###.#.#.##.#......#####..###..##.#.##..###.##.###..###..#.###...#.#...#..#.##.#.#..#.#....###.#.#..##.#.##.##.#####..###...#.###.###...##..#..##.##.#.##..####.#.###.###.....####.##..#######....#.##....###.#..#..##.#.####.....###..##.#.#..#..#...#.####..######..#####.##...#.#....#....#.#.#####.##.#.#####..##.#...#..##..##.#.##.##.####..##.##..####..#..####.########.#..#.##.#.######....##...#.##.##.####......#.##.##"
h = 26
w = 26

def common(L):
    """ Finds if two numbers have a common factor. Returns True if they do not.
    """
    n = 0

    for i in range(2, min(L)+1):
        if L[0]%i==L[1]%i==0:
            n += 1
    
    if n > 0:
        return False
    else:
        return True

angles_list = list(filter(lambda x: x[0] == 1 or (x[0]<x[1] and common(x)), list(permutations(range(1,26), 2)))) #permutations returns a list of lists

def count(S, w, h):
    """Takes a string of asteroid belt data and finds the spot that can see the most asteroids, and how many asteroids it can see.
    """
    # first I need to split the string into the rows
    
    while x := 0 < len(S):
        if S[x] == ".":
            # do the counting thing
            # move right

            # move down

            # move left

            # move up

        x += 1


def los(S):
    """Takes a string of asteroid belt data and returns the spot that can see the most asteroids, and how many asteroids it can see.
    """
    
    def count(x, y, L):
        """ Takes an x,y coordinate and returns how many asteroids are visible from that location.
        """
        # move out in each direction
        x0 = x
        y0 = y
        total = 0

        def angles(x0, y0, quadrant, L):
            """ Takes the list and returns all possible angles for a particular quadrant in a list. Doesn't account for the axes.
            Quadrants are TR, TL, BR, BL.
            """
            L = []
            x = 25
            y = 25
            if quadrant == "TR":
                x_mod = 1
                y_mod = 1
                x_diff = 26 - x
                y_diff = 26 - y
                top = 26
            elif quadrant == "TL":
                x_mod = -1
                y_mod = 1
                x_diff = x
                y_diff = 26 - y
                top = 26
            elif quadrant == "BR":
                x_mod = 1
                y_mod = -1
                x_diff = 26 - x
                y_diff = y
                top = 0
            elif quadrant == "BL":
                x_mod = -1
                y_mod = -1
                x_diff = x
                y_diff = y
                top = 0
            else:
                raise ValueError

            for y in range(min(y0+y_mod,top),max(y0+y_mod,top)):
                while x > x0:
                    if [x, y] not in L: L.append([x, y])
                    x -= 1
                x = 25


            return L
    
    grid = []
    answers = []
    i = 0
    while i < 26:
        grid.append(S[0:25])
        try: S = S[26:]
        except: S = []
    x = 0
    y = 0
    for j in grid:
        for k in j:
            if k == "#":
                answers.append((x, y), count(x,y, grid))
            x += 1
        y += 1
        x = 0
    
    
    answers.sort(key=lambda x: x[1], reverse=True)
    return answers
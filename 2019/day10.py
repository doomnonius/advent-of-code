from itertools import permutations
# inp = ".#..#.....#####....#...##"
# h = 5
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

a = list(filter(lambda x: (x[0] == 1 or (x[0]<x[1] and common(x))) or (x[1] == 1 or (x[1]<x[0] and common(x))), list(permutations(range(1,h), 2)))) #permutations returns a list of lists
a.append((1,1))
# print(a)

def count(S, h):
    """Takes a string of asteroid belt data and finds the spot that can see the most asteroids, and how many asteroids it can see.
    """
    
    def math_part(point, quadrant, c, z = 0):
        """ Takes a point and a quadrant and figures things out for that quadrant.
        Quadrants are: RU, RD, LD, LU
        """

        if quadrant[1] == "U":
            m = -1
        else: m = 1

        if quadrant[0] == "L":
            n = -1
        else: n = 1
        
        y1, x1 = point[0], point[1]

        # print([y, x])
        # print(z)
        # print(a)
        i, j = a[z][0], a[z][1]
        # print(i, ",", j)
        # print(quadrant)
        while True:
            if 0 <= x1 + j*n < w and 0 <= y1 + m*i < h:
                # print(x1+j*n<w)
                # print([quadrant, c, y1+i*m, x1+j*n])
                if complete[y1 + (m*i)][x1 + (j*n)] == "#":
                    c += 1
                    if c == 200: answer = (x1 + (j*n))*100 + y1 + (m*i)
                    elif c < 200: answer = 0
                    if z < len(a)-1: z += 1
                    else: break
                    i, j = a[z][0], a[z][1]
                    # print(i, ",", j)
                else:
                    i += a[z][0]
                    j += a[z][1]
            else:
                if z < len(a)-1: z += 1
                else: break
                i, j = a[z][0], a[z][1]
                # print(i, ",", j)
        # a.pop(0)
        return(c, answer)
    
    # first I need to split the string into the rows
    total = len(S)
    # print(total)
    w = total/h
    # print(w)
    complete = []
    x = 0
    pointer = 0
    while x < h:
        # print(complete, x)
        complete.append([])
        while pointer < w:
            complete[x].append(S[0])
            S = S[1:]
            # print(S)
            pointer += 1
        pointer = 0
        x += 1
    # print(complete)
    # x, y, c = 0, 0, 0
    c = 0
    # results = []

    # the point is known

    # while y < h:
    #     while x < w:
    #         if complete[y][x] == "#":
    a.sort(key = lambda x: x[0]/x[1], reverse=True)
    a.insert(0, (1,0))
    # print(a)
    c, answer = math_part((17,13), "RU", c)
    a.pop(0)

    a.sort(key = lambda x: x[0]/x[1])
    a.insert(0, (0,1))
    c, answer = math_part((17,13), "RD", c)
    a.pop(0)
    
    a.sort(key = lambda x: x[0]/x[1], reverse=True)
    a.insert(0, (1,0)) #sorted so that 1,0 is first
    c, answer = math_part((17,13), "LD", c)
    a.pop(0)

    a.sort(key = lambda x: x[0]/x[1])
    a.insert(0, (0,1)) # sorted so 0,1 is first
    c, answer = math_part((17,13), "LU", c)
                # add count to results table
        #         results.append(c)
        #         if c == 269:
        #             print("Point:", y, ",", x)
        #         c = 0
        #     x += 1 # this increments the check for clear spaces
        # x = 0
        # y += 1
    
    # results.sort(key=lambda x: x[1])
    return c, answer

print(count(inp, h))
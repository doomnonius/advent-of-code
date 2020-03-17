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
    
    def math_part(point, quadrant, boo, c, z = 0):
        """ Takes a point, a quadrant and a boolean and figures things out for that quadrant.
        Quadrants are: RU, RD, LD, LU
        """

        if boo == True:
            a.insert(0, (1,0))
        else:
            a.insert(0, (0,1))

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
            if x1 + j*n < w and y1 + m*i < h:
                print(x1+j*n<w)
                print([quadrant, c, y+i*m, x+j*n])
                if complete[y1 + (m*i)][x1 + (j*n)] == "#":
                    c += 1
                    if c == 200:
                        print(x1*100 + y)
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
        a.pop(0)
        return(c)
        
    
    # first I need to split the string into the rows
    total = len(S)
    # print(total)
    w = total/h
    print(w)
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
    x, y, c = 0, 0, 0
    results = []
    while y < h:
        while x < w:
            if complete[y][x] == "#":
                c = math_part((y,x), "RU", True, c)
                c = math_part((y,x), "RD", False, c)
                c = math_part((y,x), "LD", True, c)
                c = math_part((y,x), "LU", True, c)
                # add count to results table
                results.append(c)
                c = 0
            x += 1 # this increments the check for clear spaces
        x = 0
        y += 1
    
    # results.sort(key=lambda x: x[1])
    return max(results)


# def los(S):
#     """Takes a string of asteroid belt data and returns the spot that can see the most asteroids, and how many asteroids it can see.
#     """
    
#     def count(x, y, L):
#         """ Takes an x,y coordinate and returns how many asteroids are visible from that location.
#         """
#         # move out in each direction
#         x0 = x
#         y0 = y
#         total = 0

#         def angles(x0, y0, quadrant, L):
#             """ Takes the list and returns all possible angles for a particular quadrant in a list. Doesn't account for the axes.
#             Quadrants are TR, TL, BR, BL.
#             """
#             L = []
#             x = 25
#             y = 25
#             if quadrant == "TR":
#                 x_mod = 1
#                 y_mod = 1
#                 x_diff = 26 - x
#                 y_diff = 26 - y
#                 top = 26
#             elif quadrant == "TL":
#                 x_mod = -1
#                 y_mod = 1
#                 x_diff = x
#                 y_diff = 26 - y
#                 top = 26
#             elif quadrant == "BR":
#                 x_mod = 1
#                 y_mod = -1
#                 x_diff = 26 - x
#                 y_diff = y
#                 top = 0
#             elif quadrant == "BL":
#                 x_mod = -1
#                 y_mod = -1
#                 x_diff = x
#                 y_diff = y
#                 top = 0
#             else:
#                 raise ValueError

#             for y in range(min(y0+y_mod,top),max(y0+y_mod,top)):
#                 while x > x0:
#                     if [x, y] not in L: L.append([x, y])
#                     x -= 1
#                 x = 25


#             return L
    
#     grid = []
#     answers = []
#     i = 0
#     while i < 26:
#         grid.append(S[0:25])
#         try: S = S[26:]
#         except: S = []
#     x = 0
#     y = 0
#     for j in grid:
#         for k in j:
#             if k == "#":
#                 answers.append((x, y), count(x,y, grid))
#             x += 1
#         y += 1
#         x = 0
    
    
#     answers.sort(key=lambda x: x[1], reverse=True)
#     return answers


print(count(inp, h))
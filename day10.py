from itertools import permutations
inp = ".#..#.....#####....#...##"
h = 5
# inp = "#.#.###.#.#....#..##.#.........#..#..#..#.#..#.....#.##.##.##.##.##..#...#...##.#...#.#####...###.#.#.#..#####.###.#.#.####.#####.#.#.#.##.#.##...####.#.##.##....###..#.#..#..#..###...##....#.#...##.#.#...####.....#.#######..##.##.#..#.###.#..###.#.#..##.....###.#.#.##.#......#####..###..##.#.##..###.##.###..###..#.###...#.#...#..#.##.#.#..#.#....###.#.#..##.#.##.##.#####..###...#.###.###...##..#..##.##.#.##..####.#.###.###.....####.##..#######....#.##....###.#..#..##.#.####.....###..##.#.#..#..#...#.####..######..#####.##...#.#....#....#.#.#####.##.#.#####..##.#...#..##..##.#.##.##.####..##.##..####..#..####.########.#..#.##.#.######....##...#.##.##.####......#.##.##"
# h = 26
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
print(a)

def count(S, h):
    """Takes a string of asteroid belt data and finds the spot that can see the most asteroids, and how many asteroids it can see.
    """
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
    print(complete)
    x, y, z, c = 0, 0, 0, 0
    results = []
    while y < h:
        while x < w:
            if complete[y][x] == "#":
                print([y, x])
                # do the counting thing
                # note: checking (0, 1) and (1, 1) separately
                # print(z)
                i, j = a[z][0], a[z][1]
                a.append((1,1))
                a.append((0,1))
                # right and down from the point
                while True:
                    if x + i < w and y + j < h:
                        if complete[x+i][y+j] == "#":
                            c += 1
                            print(["rd1", c, x+i, y+j])
                            if z < len(a)-1: z += 1
                            else: break
                            i, j = a[z][0], a[z][1]
                        else:
                            i *= 2
                            j *= 2
                    else:
                        if z < len(a)-1: z += 1
                        else: break
                        i, j = a[z][0], a[z][1]
                z = 0
                a.pop()
                a.pop()
                j, i = a[z][0], a[z][1]
                while True:
                    if x + i < w and y + j < h:
                        if complete[x+i][y+j] == "#":
                            c += 1
                            print(["rd2", c, x+i, y+j])
                            if z < len(a)-1: z += 1
                            else: break
                            j, i = a[z][0], a[z][1]
                        else:
                            i *= 2
                            j *= 2
                    else:
                        if z < len(a)-1: z += 1
                        else: break
                        j, i = a[z][0], a[z][1]
                z = 0
                i, j = a[z][0], a[z][1]
                a.append((1,1))
                # left and down from the point
                while True:
                    if x - i >= 0 and y + j < h:
                        if complete[x-i][y+j] == "#":
                            c += 1
                            print(["ld1", c, x-i, y+j])
                            if z < len(a)-1: z += 1
                            else: break
                            i, j = a[z][0], a[z][1]
                        else:
                            i *= 2
                            j *= 2
                    else:
                        if z < len(a)-1: z += 1
                        else: break
                        i, j = a[z][0], a[z][1]
                z = 0
                a.pop()
                j, i = a[z][0], a[z][1]
                a.append((0,1))
                while True:
                    if x - i >= 0 and y + j < h:
                        if complete[x-i][y+j] == "#":
                            c += 1
                            print(["ld2", c, x-i, y+j])
                            if z < len(a)-1: z += 1
                            else: break
                            j, i = a[z][0], a[z][1]
                        else:
                            i *= 2
                            j *= 2
                    else:
                        if z < len(a)-1: z += 1
                        else: break
                        j, i = a[z][0], a[z][1]
                z = 0
                a.pop()
                i, j = a[z][0], a[z][1]
                a.append((1,1))
                a.append((0,1))
                # left and up from the point
                while True:
                    if x - i >= 0 and y - j >= 0:
                        if complete[x-i][y-j] == "#":
                            c += 1
                            print(["lu1", c, x-i, y-j])
                            if z < len(a)-1: z += 1
                            else: break
                            i, j = a[z][0], a[z][1]
                        else:
                            i *= 2
                            j *= 2
                    else:
                        if z < len(a)-1: z += 1
                        else: break
                        i, j = a[z][0], a[z][1]
                z = 0
                a.pop()
                a.pop()
                j, i = a[z][0], a[z][1]
                while True:
                    if x - i >= 0 and y - j >= 0:
                        if complete[x-i][y-j] == "#":
                            c += 1
                            print(["lu2", c, x-i, y-j])
                            if z < len(a)-1: z += 1
                            else: break
                            j, i = a[z][0], a[z][1]
                        else:
                            i *= 2
                            j *= 2
                    else:
                        if z < len(a)-1: z += 1
                        else: break
                        j, i = a[z][0], a[z][1]
                z = 0
                a.append((1,1))
                i, j = a[z][0], a[z][1]
                # right and up from the point
                while True:
                    if x + i < w and y - j >= 0:
                        if complete[x+i][y-j] == "#":
                            c += 1
                            print(["ru1", c, x+i, y-j])
                            if z < len(a)-1: z += 1
                            else: break
                            i, j = a[z][0], a[z][1]
                        else:
                            i *= 2
                            j *= 2
                    else:
                        if z < len(a)-1: z += 1
                        else: break
                        i, j = a[z][0], a[z][1]
                z = 0
                a.pop()
                j, i = a[z][0], a[z][1]
                a.append((0,1))
                while True:
                    if x + i < w and y - j >= 0:
                        if complete[x+i][y-j] == "#":
                            c += 1
                            print(["ru2", c, x+i, y-j])
                            if z < len(a)-1: z += 1
                            else: break
                            j, i = a[z][0], a[z][1]
                        else:
                            i *= 2
                            j *= 2
                    else:
                        if z < len(a)-1: z += 1
                        else: break
                        j, i = a[z][0], a[z][1]
                # add count to results table
                a.pop()
                results.append([c, (y, x)])
                c = 0
                z = 0
            x += 1 # this increments the check for clear spaces
        x = 0
        y += 1
    
    # results.sort(key=lambda x: x[1])
    return results


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
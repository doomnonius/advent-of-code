inp = "#.#.###.#.#....#..##.#.........#..#..#..#.#..#.....#.##.##.##.##.##..#...#...##.#...#.#####...###.#.#.#..#####.###.#.#.####.#####.#.#.#.##.#.##...####.#.##.##....###..#.#..#..#..###...##....#.#...##.#.#...####.....#.#######..##.##.#..#.###.#..###.#.#..##.....###.#.#.##.#......#####..###..##.#.##..###.##.###..###..#.###...#.#...#..#.##.#.#..#.#....###.#.#..##.#.##.##.#####..###...#.###.###...##..#..##.##.#.##..####.#.###.###.....####.##..#######....#.##....###.#..#..##.#.####.....###..##.#.#..#..#...#.####..######..#####.##...#.#....#....#.#.#####.##.#.#####..##.#...#..##..##.#.##.##.####..##.##..####..#..####.########.#..#.##.#.######....##...#.##.##.####......#.##.##"
h = 26
w = 26

def los(S):
    """Takes a string of asteroid belt data and returns the spot that can see the most asteroids, and how many asteroids it can see.
    """
    
    def count(x, y, L):
        """ Takes an x,y coordinate and returns how many asteroids are visible from that location.
        """
        # move out in each direction
        x0 = x
        y0 = y
        while x < 26:
            x += 1
            if L[y][x] == :
                return
    
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
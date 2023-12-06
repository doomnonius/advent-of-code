from typing import List
from datetime import datetime

def charge_boat(time: int) -> int:
    for i in range(time):
        yield i * (time - i)

def charged(time:int, held:int):
    return held * (time-held)

def part1(times: List[int], dists: List[int]) -> int:
    r = 1
    for t,d in zip(times,dists):
        solves = 0
        b = False
        for x in charge_boat(t):
            if x > d:
                solves += 1
                b = True
            else:
                if b == True:
                    r *= solves
                    break
    return r

def part2(time: int, dist: int, skip: int) -> int:
    low = 0
    for i in range(0, time, skip):
        if not low and charged(time, i) > dist:
            print("approx low found!")
            for j in range(i-skip-1,i):
                if charged(time, j) > dist:
                    low = j
                    print("low found!")
                    break
        elif low and charged(time, i) < dist:
            for j in range(i-skip-1,i):
                if charged(time, j) < dist:
                    return j - low
                
if __name__ == "__main__":
    import os, timeit
    times = [51, 69, 98, 78]
    distances = [377, 1171, 1224, 1505]
    # times = [7, 15, 30]
    # distances = [9, 40, 200]
    print(f"Part 1: {part1(times, distances)}") # not 22572000, too high; dumb error
    start = datetime.now()
    print(f"Part 2: {part2(51699878, 377117112241505, 1000)}")
    print(f"time: {datetime.now()-start}")
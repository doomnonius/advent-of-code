from typing import List

def part1(nums: List[str], p2: bool = False) -> int:
    retVal = len(nums[0]) * 2 + (len(nums)-2) * 2
    y = 1
    if p2: highScore = 0
    for row in nums[1:-1]:
        x = 1
        while x < len(row) - 1:
            vis = False
            curr_h = nums[y][x]
            # look right
            if p2: seen_r = 0
            check_x = x + 1
            while check_x < len(row):
                vis = False
                if p2: seen_r += 1
                if nums[y][check_x] >= curr_h:
                    break
                check_x += 1
                vis = True
            if not p2 and vis:
                retVal += 1
                x += 1
                continue
            # look left
            if p2: seen_l = 0
            check_x = x - 1
            while check_x >= 0:
                vis = False
                if p2: seen_l += 1
                if nums[y][check_x] >= curr_h:
                    break
                check_x -= 1
                vis = True
            if not p2 and vis:
                retVal += 1
                x += 1
                continue
            # look up
            if p2: seen_u = 0
            check_y = y - 1
            while check_y >= 0:
                vis = False
                if p2: seen_u += 1
                if nums[check_y][x] >= curr_h:
                    break
                check_y -= 1
                vis = True
            if not p2 and vis:
                retVal += 1
                x += 1
                continue
            # look down
            if p2: seen_d = 0
            check_y = y + 1
            while check_y < len(nums):
                vis = False
                if p2: seen_d += 1
                if nums[check_y][x] >= curr_h:
                    break
                check_y += 1
                vis = True
            if not p2 and vis:
                retVal += 1
                x += 1
                continue
            if p2: highScore = max(highScore, (seen_d * seen_l * seen_r * seen_u))
            x += 1
        y += 1
    if p2: return highScore
    return retVal

if __name__ == "__main__":
    import os, timeit
    from pathlib import Path
    INPUT_FILE = Path(__file__).with_suffix(".input")
    DATA = INPUT_FILE.read_text().strip().split()
    DATA = [x for x in DATA] # example code
    print(f"Part 1: {part1(DATA)}")
    print(f"Part 2: {part1(DATA, True)}")
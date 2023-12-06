from typing import List, Set, Dict, Tuple
from datetime import datetime

class Map:
    def __init__(self, data:str):
        data = data.split("\n")
        self.ranges = []
        for line in data[1:]:
            self.ranges.append([int(x) for x in line.split()])
    
    def mapping(self, x:int) -> int:
        for r in self.ranges:
            dest, source, range = r
            if source <= x < source+range:
                return x + (dest - source)
        return x

def part1(seeds: Set[int], maps: List[Map], test:bool=False) -> int:
    locs = []
    for s in seeds:
        for m in maps:
            s = m.mapping(s)
        locs.append(s)
    return min(locs)

def narrow_range(starts: List[int], offsets: List[int], maps: List[Map], skip:int) -> Tuple[List[int], List[int], List[Dict]]:
    """ sample every 1,000,000 and narrow scope to 3 lowest scored dictionaries, sampling based off every 1000 from that smaller range, finally by 1s
        this solution was inspired by the idea of a binary sort
    """
    dicts = []
    for i in range(len(starts)):
        locs = dict()
        s = set(range(starts[i],starts[i]+offsets[i],skip))
        for i in s:
            locs[i] = part1({i}, maps)
        dicts.append(locs)
    dicts.sort(key=lambda x: min([v for v in x.values()])); print(f"size {len(dicts)} [37]")
    top = len(dicts) // 3
    if top < 1: top = 1
    dicts = dicts[0:top]
    new_starts: List[int] = []
    new_offsets: List[int] = []
    for d in dicts:
        # find the minimum value; find the numbers before and after the seed that leads to it, and run again at skip of 1000, then at 1
        k = sorted(d.keys())
        mid = min([v for v in d.values()])
        reversed = {v:k for k,v in d.items()}
        mid = reversed[mid]
        l = k.index(mid)
        if 0 < l < (len(k)-1):
            new_starts.append(k[l-1])
            new_offsets.append(k[l+1]-k[l-1])
        elif l == 0:
            new_starts.append(k[l])
            new_offsets.append(k[l+1]-k[l])
        else:
            new_starts.append(k[l-1])
            new_offsets.append(k[l]+1-k[l-1])
    return new_starts, new_offsets, dicts

def part2(seeds: List[int], maps: List[Map], skip:int) -> int:
    dicts: List[Dict] = []
    starts = seeds[0::2]
    offsets = seeds[1::2]
    while True:
        starts, offsets, dicts = narrow_range(starts, offsets, maps, skip)
        skip//=1000
        if len(dicts) == 1:
            break
    s = set(range(starts[0],starts[0]+offsets[0]))
    return part1(s, maps)


if __name__ == "__main__":
    import os, timeit
    from pathlib import Path
    test = False
    if test: INPUT_FILE = Path(__file__).with_suffix(".testinput")
    else: INPUT_FILE = Path(__file__).with_suffix(".input")
    DATA = INPUT_FILE.read_text().strip()
    DATA = DATA.split("\n\n")
    seeds = [int(x) for x in DATA[0].split(":")[1].split()]
    maps = [Map(x) for x in DATA[1:]]
    print(f"Part 1: {part1(seeds, maps, test)}")
    start = datetime.now()
    print(f"Part 2: {part2(seeds, maps, 1000000)}")
    print(f"run time: {datetime.now()-start}")
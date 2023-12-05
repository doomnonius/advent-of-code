from typing import List, Set, Dict, Tuple
from datetime import datetime

class Map:
    def __init__(self, data:str):
        data = data.split("\n")
        self.ranges = []
        for line in data[1:]:
            self.ranges.append([int(x) for x in line.split()])
        # print(self.ranges)
    
    def mapping(self, x:int) -> int:
        for r in self.ranges:
            dest, source, range = r
            if source <= x < source+range:
                return x + (dest - source)
        return x

def part1(seeds: Set[int], maps: List[Map], test:bool=False) -> int:
    locs = []
    for s in seeds:
        # print(f"seeds: {len(seeds)}")
        start = datetime.now()
        for m in maps:
            s = m.mapping(s)
        locs.append(s)
        end = datetime.now()
        # print(f"seed mapped in time {end-start}! with {len(seeds)} this will take about {(end-start)*len(seeds)}")
    if test: print(locs)
    return min(locs)

def process_data(seeds: List[int]) -> Set[int]:
    r = set()
    s = 0
    while s < len(seeds): #for s in seeds[0::2]:
        start = datetime.now()
        for offset in range(seeds[s+1]):
            r.add(seeds[s] + offset)
        s += 2
        end = datetime.now()
        av = (end-start/seeds[s-1])
        # print(f"{seeds[s-1]} seeds took {end-start} time to expand out, an average of {av} per seed. with {sum[seeds[1::2]]} total seeds, that would take {av*sum[seeds[1::2]]} seconds")
    print(r)
    return r

def part2(seeds: List[int], maps: List[Map], skip:int) -> int:
    # idea for tomorrow: reverse engineer (in retrospect also seems too computationally intense) OR sample every 1,000,000 and narrow scope?
    starts = seeds[0::2]
    offsets = seeds[1::2]
    dicts: List[Dict] = []
    for i in range(len(starts)):
        locs = dict()
        s = set(range(starts[i],starts[i]+offsets[i],skip))
        for i in s:
            locs[i] = part1({i}, maps)
        dicts.append(locs)
        # for k in keys:
        #     print(f"k:{k}, v:{locs[k]}")
    dicts.sort(key=lambda x: min([v for v in x.values()]))
    ranges:List[Tuple] = []
    for d in dicts[0:3]:
        # find the minimum value; find the numbers before and after the seed that leads to it, and run again at skip of 1000, then at 1
        k = sorted(d.keys())
        mid = min([v for v in d.values()])
        reversed = {v:k for k,v in d.items()}
        mid = reversed[mid]
        l = k.index(mid)
        if 0 < l < (len(k)-1):
            ranges.append((k[l-1],k[l+1]))
        elif l == 0:
            ranges.append((k[l], k[l+1]))
        else:
            ranges.append((k[l-1], k[l]+1))
    dicts: List[Dict] = []
    for r in ranges:
        locs = dict()
        s = set(range(r[0],r[1],1000))
        for i in s:
            locs[i] = part1({i}, maps)
        dicts.append(locs)
    dicts.sort(key=lambda x: min([v for v in x.values()]))
    d = dicts[0]
    k = sorted(d.keys())
    mid = min([v for v in d.values()])
    reversed = {v:k for k,v in d.items()}
    mid = reversed[mid]
    l = k.index(mid)
    if 0 < l < (len(k)-1):
        narrowed = (k[l-1],k[l+1])
    elif l == 0:
        narrowed = (k[l], k[l+1])
    else:
        narrowed = (k[l-1], k[l]+1)
    s = set(range(narrowed[0],narrowed[1]))
    return part1(s, maps)

    # select the three ranges with the lowest numbers to do the process again at 1000
    # print(min([v for v in locs.values()]))
    # return min(locs)




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
    # seeds = process_data([int(x) for x in DATA[0].split(":")[1].split()])
    start = datetime.now()
    print(f"Part 2: {part2(seeds, maps, 100000)}")
    print(f"run time: {datetime.now()-start}")
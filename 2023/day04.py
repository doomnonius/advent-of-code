from typing import List, Dict, Tuple

def process(data:str) -> Dict[int, Tuple[List[int], List[int]]]:
    r = dict()
    rows = data.split("\n")
    for card in rows:
        card_id, card_nums = card.split(":")
        card_id = int(card_id.split()[1])
        card_targets, card_hits = card_nums.split("|")
        card_targets = [int(x) for x in card_targets.split()]
        card_hits = [int(x) for x in card_hits.split()]
        r[card_id] = (card_targets, card_hits)
    return r

def part1(cards: Dict[int, Tuple[List[int], List[int]]]) -> int:
    t = 0
    for nums in cards.values():
        cv = 0
        for n in nums[1]:
            if n in nums[0]:
                if cv == 0:
                    cv = 1
                else:
                    cv *= 2
        t += cv
    return t

def part2(cards: Dict[int, Tuple[List[int], List[int]]]) -> int:
    card_counts = {k:1 for k in cards.keys()}
    for card, nums in cards.items():
        wins = 0
        for n in nums[1]:
            if n in nums[0]:
                wins += 1
        offset = 0
        while wins > 0:
            wins -= 1
            offset += 1
            if card+offset in card_counts.keys():
                card_counts[card+offset] += card_counts[card]
    return sum([x for x in card_counts.values()])




if __name__ == "__main__":
    import os, timeit
    from pathlib import Path
    INPUT_FILE = Path(__file__).with_suffix(".input")
    DATA = INPUT_FILE.read_text().strip()
    DATA = process(DATA) # example code
    print(f"Part 1: {part1(DATA)}")
    print(f"Part 2: {part2(DATA)}")
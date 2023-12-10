"""Day 7 of Advent Of Code.
pb 1: 251927063
pb 2: 255632664
"""
from collections import Counter
from typing import List, Tuple
import sys

# add the base.py to the path
sys.path.append("../advent_of_code")
from base import BaseAdventOfCode


class Day7(BaseAdventOfCode):
    """Class for solving day 7."""

    def solve_first_pb(self):
        cards: List[Tuple(str, int)] = []
        for line in self.entry:
            hand, bid = line.split(" ")
            cards.append((hand, bid))

        sorted_cards: List[Tuple[str, int]] = sorted(
            cards,
            key=lambda hand: self._find_type(hand[0])
        )

        result: int = 0
        for index, (hand, bid) in enumerate(sorted_cards):
            result += int(bid) * (index + 1)
        return result

    def solve_second_pb(self):
        cards: List[Tuple(str, int)] = []
        for line in self.entry:
            hand, bid = line.split(" ")
            cards.append((hand, bid))

        sorted_cards: List[Tuple[str, int]] = sorted(
            cards,
            key=lambda hand: self._find_type(hand[0], True)
        )

        result: int = 0
        for index, (hand, bid) in enumerate(sorted_cards):
            result += int(bid) * (index + 1)
        return result

    def _find_type(self, hand: str, part_2: bool = False) -> int:
        """Based on the hand return the hand type.

        First, replace letter by a unicode representation (for sorting purposes).
        
        Returns:
            int: that corresponds to the hand type (check patterns).
        """
        norma = hand
        hand = hand.replace('T',chr(ord('9')+1))
        hand = hand.replace('J',chr(ord('2')-1) if part_2 else chr(ord('9')+2))
        hand = hand.replace('Q',chr(ord('9')+3))
        hand = hand.replace('K',chr(ord('9')+4))
        hand = hand.replace('A',chr(ord('9')+5))
        c = Counter(hand)

        if part_2:
            target: str = list(c.keys())[0]
            for key in c:
                if key == "1":
                    continue
                if c[key] > c[target] or target == "1":
                    target = key
            if "1" in c and target != "1":
                c[target] += c["1"]
                del c["1"]

        combination: List[int] = sorted(list(c.values()))

        if combination == [5]:
            return 7, hand
        if combination == [1,4]:
            return 6, hand
        if combination == [2,3]:
            return 5, hand
        if combination == [1, 1, 3]:
            return 4, hand
        if combination == [1, 2, 2]:
            return 3, hand
        if combination == [1, 1, 1, 2]:
            return 2, hand
        return 1, hand



day7 = Day7("day7/day7.txt")
day7.solve()

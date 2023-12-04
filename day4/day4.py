"""Day 4 of Advent Of Code.
pb 1: 20107
pb 2: 
"""
from typing import List, Tuple
import sys

# add the base.py to the path
sys.path.append("../advent_of_code")

from base import BaseAdventOfCode

class Day4(BaseAdventOfCode):
    """Class for solving day 4."""

    def solve_first_pb(self):
        count: int = 0
        for line in self.entry:
            local_count: int = 0
            win_num, my_num = self._parse_line(line)
            local_count, _ = self._count(winning=win_num, numbers=my_num, local_count=local_count)
            count += local_count
        return count

    def solve_second_pb(self):
        # contains the number of copy cards
        retry: List[str]= [0 for _ in self.entry]
        count: int = 0
        for index, line in enumerate(self.entry):
            local_count: int = 0
            win_num, my_num = self._parse_line(line)
            _, local_count = self._count(winning=win_num, numbers=my_num, local_count=local_count)

            for local_index, elt in enumerate(range(index, local_count + 1)):
                retry[local_index] += elt
            count += local_count
        #     print(retry)
        # print(sum(retry))
        return count

    def _count(self, winning: List[str], numbers: List[str], local_count: int) -> Tuple[int, int]:
        """Count the number of winning number we have.
        
        Args:
            winning (List[str]): the list containing the winning number.
            numbers (List[str]): the list containing my number.

        Returns:
            Tuple[int]: the sum (point) and the count of matching number.
        """
        elt_count: int = 0
        for elt in winning:
            if elt == "":
                continue
            if elt in numbers and local_count != 0:
                local_count *= 2
                elt_count += 1
            elif elt in numbers and local_count ==0:
                local_count = 1
                elt_count += 1
        return local_count, elt_count

    def _parse_line(self, line: str) -> Tuple[List[str], List[str]]:
        """Parse the line and format values.
        
        Args:
            line (str): the current line.
        
        Returns:
            Tuple[List[str], List[str]]: Contains the winning numbers (first element)
                and the number I have (second element).
        """
        _, numbers = line.split(":")
        winning_num, my_num = numbers.split("|")
        formatted_winning_num = winning_num[1:].split(" ")
        formatted_my_num = my_num[1:].split(" ")
        return formatted_winning_num, formatted_my_num

day4 = Day4("day4/day4.txt")
day4.solve()

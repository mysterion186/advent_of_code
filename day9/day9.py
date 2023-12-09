"""Day 9 of Advent Of Code.
pb 1: 1882395907
pb 2: 1005
"""
import re
from typing import List, Union, Set
import sys

# add the base.py to the path
sys.path.append("../advent_of_code")
from base import BaseAdventOfCode


class Day9(BaseAdventOfCode):
    """Class for solving day 9."""

    def txt_parser(self, filepath: str) -> List[int]:
        re_pattern: str = r"-?\d+"
        formatted_line: List[int] = []
        lines: List[str] = super().txt_parser(filepath)
        for line in lines:
            x = re.findall(pattern=re_pattern, string=line)
            if not x:
                continue
            formatted_line.append([int(value) for value in x])
        return formatted_line

    def solve_first_pb(self):
        result: int = 0
        for line in self.entry:
            result += self._find_prediction(line)
        return result

    def solve_second_pb(self):
        self._reverse_line()
        result: int = self.solve_first_pb()
        return result

    def _find_prediction(self, line: Union[int, List[int]]) -> int:
        """Based on a line, the predicted value. It will be a recursive function.
        
        Args:
            line (Union[int, List[int]]): the working line history.
        
        Returns:
            int: the prediction value for the line.
        """
        underline: List[int] = []
        for first, second in zip(line[:-1], line[1:]):
            underline.append(second - first)
        if self._end_line(underline):
            return line[-1]
        return line[-1] + self._find_prediction(underline)

    def _end_line(self, line: Union[List[int], int]) -> bool:
        """Check that all element of the line are 0 or not."""
        if isinstance(line, int):
            return True
        setted: Set[int] = set(line)
        return len(list(setted)) == 1 and list(setted)[0] == 0

    def _reverse_line(self) -> None:
        """reverse the list."""
        temporary_entry: List[int] = []
        for line in self.entry:
            temporary_entry.append(line[::-1])
        self.entry = temporary_entry


day9 = Day9("day9/day9.txt")
day9.solve()

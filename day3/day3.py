"""Day 3 of Advent Of Code.
pb 1: 538046
pb 2: 81709807
"""
import re
from typing import Optional, List
import sys

# add the base.py to the path
sys.path.append("../advent_of_code")

from base import BaseAdventOfCode

class Day3(BaseAdventOfCode):
    """Class for solving day 3."""

    def solve_first_pb(self) -> int:
        line_sum: List[int] = []
        for count, line in enumerate(self.entry):
            if count == 0:
                local_result: List[int] = self._kernel(line, next_line= self.entry[count + 1])
            elif count == len(self.entry) - 1:
                local_result: List[int] = self._kernel(line, previous_line=self.entry[count - 1])
            else:
                local_result: List[int] = self._kernel(
                    line,
                    previous_line=self.entry[count - 1],
                    next_line=self.entry[count + 1]
                )
            line_sum.append(sum(local_result))
        return sum(line_sum)

    def solve_second_pb(self) -> int:
        line_sum: List[int] = []
        for count, line in enumerate(self.entry):
            if count == 0:
                temp_gear:List[List[int]] = self._kernel_second(line, next_line=self.entry[count + 1])
            elif count == len(self.entry) - 1:
                temp_gear:List[List[int]] = self._kernel_second(line, previous_line=self.entry[count - 1])
            else:
                temp_gear:List[List[int]] = self._kernel_second(
                    line,
                    previous_line=self.entry[count - 1],
                    next_line=self.entry[count + 1]
                )
            for gear1, gear2 in temp_gear:
                line_sum.append(gear1 * gear2)
        return sum(line_sum)

    def _kernel(
        self,
        working_line: List[str],
        previous_line: Optional[List[str]] = None,
        next_line: Optional[List[str]] = None
    ):
        """Find in the given line the number next to a symbol.
        
        Args:
            working_line (List[str]): the current line we're working with.
            previous_line (Optional[List[str]]): 
                the previous line of the working line (if it exists).
            next_line (Optional[List[str]]): the next of the working line (if it exists).
        
        Returns:
            List[int]: that contains all the number in the working line that are part
                a 'part number'.
        """
        local_part_number: List[int] = []
        re_pattern = r"\d+"
        # don't catch '.' or any digit
        re_pattern_look = r"[^\.\d]"
        research = re.finditer(pattern=re_pattern, string=working_line)
        for match in research:
            start: int = match.start()
            end: int = match.end()
            working_number = match.group()
            # constrain index position
            c_start = start - 1 if start -1 >= 0 else start
            c_end = end + 1 if end + 1 <= len(working_line) - 1 else end

            # check right and left of the number for a symbole
            result = re.findall(pattern=re_pattern_look, string=working_line[c_start:c_end])
            if result:
                local_part_number.append(int(working_number))
            if previous_line:
                result = re.findall(pattern=re_pattern_look, string=previous_line[c_start:c_end])
                if result:
                    local_part_number.append(int(working_number))
            if next_line:
                result = re.findall(pattern=re_pattern_look, string=next_line[c_start:c_end])
                if result:
                    local_part_number.append(int(working_number))
        return local_part_number

    def _kernel_second(
        self,
        working_line: List[str],
        previous_line: Optional[List[str]] = None,
        next_line: Optional[List[str]] = None
    ):
        """Find two number that are next to a '*'.
        
        This method will look alike the previous one. Because it's basically the same
        working flow. Except, I need to find the whole number and not only look for the 
        closest value.

        Args:
            working_line (List[str]): the current line we're working with.
            previous_line (Optional[List[str]]): 
                the previous line of the working line (if it exists).
            next_line (Optional[List[str]]): the next of the working line (if it exists).
        
        Returns:
            List[int]: contains the ratio gear for the working line.
        """
        local_ratio_gear: List[int] = []
        re_pattern = r"[*]"
        re_pattern_digit = r"\d+"

        research = re.finditer(pattern=re_pattern, string=working_line)
        for match in research:
            start: int = match.start()
            end: int = match.end()
            temp_local: List[int] = []

            # search for number before and after the '*'
            result = re.finditer(pattern=re_pattern_digit, string=working_line)
            for num in result:
                num_start: int = num.start() - 1
                num_end: int = num.end()
                if num_start <= end and num_end >= start:
                    temp_local.append(int(num.group()))
                    # print(f"current : num: {num.group()}, start: {num.start()}, end: {num.end()}")

            # search for number on previous line
            if previous_line:
                result = re.finditer(pattern=re_pattern_digit, string=previous_line)
                for num in result:
                    num_start: int = num.start() - 1
                    num_end: int = num.end()
                    if num_start <= end and num_end >= start:
                        temp_local.append(int(num.group()))
                        # print(f"prev : num: {num.group()}, start: {num.start()}, end: {num.end()}")
            # search for number on next line
            if next_line:
                result = re.finditer(pattern=re_pattern_digit, string=next_line)
                for num in result:
                    num_start: int = num.start() - 1
                    num_end: int = num.end()
                    if num_start <= end and num_end >= start:
                        temp_local.append(int(num.group()))
                        # print(f"next : num: {num.group()}, start: {num.start()}, end: {num.end()}")
            if len(temp_local) == 2:
                local_ratio_gear.append(temp_local)
        return local_ratio_gear





day3 = Day3("day3/day3.txt")
day3.solve()

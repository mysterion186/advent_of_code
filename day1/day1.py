"""Day 1 of Advent Of Code.
pb 1: 55123
pb 2: 55260
"""
import re
import sys

# add the base.py to the path
sys.path.append("../advent_of_code")

from base import BaseAdventOfCode

class Day1(BaseAdventOfCode):
    """Class for solving day 1."""
    MAPPING_LETTER_DIGIT = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
    }

    def solve_first_pb(self) -> int:
        regex_pattern = r"[1-9]" # one or more occurence of digit
        result = 0
        for line in self.entry:
            x = re.findall(pattern=regex_pattern, string=line)
            if len(x) > 1:
                result += int(x[0] + x[-1]) # sum first and last digit
            else:
                result += int(x[0] * 2)
        return result

    def solve_second_pb(self) -> int:
        result = 0
        regex_pattern = r"[1-9]"
        letter_key = self.MAPPING_LETTER_DIGIT.keys()
        for letter in letter_key:
            regex_pattern += f"|{letter}"
        # (?=([1-9]|one|two|three|four|five|six|seven|eight|nine))
        regex_pattern = "(?=(" + regex_pattern + "))"
        for line in self.entry:
            # result += self.extract_number_from_string(line)
            x = re.findall(pattern=regex_pattern, string=line)
            if len(x) == 1:
                only_digit = self._format_number(x[0]) * 2
                result += int(only_digit)
            else:
                first_digit = self._format_number(x[0])
                last_digit = self._format_number(x[-1])
                result += int(first_digit + last_digit)
        return result

    def _format_number(self, value: str) -> str:
        """Based on the given number, output a correct value:
            return the correct value in case of letter digit
            return the value if value is a digit.
        """
        if value.isdigit() :
            return value
        return str(self.MAPPING_LETTER_DIGIT[value])

day1 = Day1("day1/day1.txt")
day1.solve()

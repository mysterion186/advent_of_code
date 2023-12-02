"""Day 2 of Advent Of Code.
pb 1: 2207
pb 2: 62241
"""
import re
from typing import Dict, List
import sys

# add the base.py to the path
sys.path.append("../advent_of_code")

from base import BaseAdventOfCode

class Day2(BaseAdventOfCode):
    """Class for solving day 2."""

    def solve_first_pb(self):
        correct_id = []
        for count, line in enumerate(self.entry):
            failed = False
            parsed_line: List[Dict[str, int]] = self._parse_line(line)
            for sub_set in parsed_line:
                if sub_set["red"] > 12 or sub_set["blue"] > 14 or sub_set["green"] > 13:
                    failed = True
            if failed:
                continue
            correct_id.append(count + 1)
        return sum(correct_id)

    def solve_second_pb(self):
        power = 0
        for line in self.entry:
            parsed_line: List[Dict[str, int]] = self._parse_line(line)
            min_red: int = parsed_line[0]["red"]
            min_blue: int = parsed_line[0]["blue"]
            min_green: int = parsed_line[0]["green"]
            for sub_set in parsed_line:
                if sub_set["red"] > min_red:
                    min_red = sub_set["red"]
                if sub_set["blue"] > min_blue:
                    min_blue = sub_set["blue"]
                if sub_set["green"] > min_green:
                    min_green = sub_set["green"]
            power += min_red * min_green * min_blue
        return power

    def _parse_line(self, line:str) -> List[Dict[str, int]]:
        """Parse a line and return a formatted list with the following dict:
            Dict[str, int]: {
                red: tolal_red_cubes,
                green: total_green_cubes,
                blue: total_blue_cubes
            }
        """
        final_count = []
        regex_pattern = r"\d+ [a-z]+"
        _, second_part = line.split(":")
        games = second_part.split(";")
        # loop over sub set
        for elt in games:
            result_dict = {
                "red": 0,
                "green": 0,
                "blue": 0
            }
            sub_sets = elt.split(",")
            # loop over each cubes
            for sub_set in sub_sets:
                local_num = re.findall(pattern=regex_pattern, string=sub_set)
                for result in local_num:
                    value, color = result.split()
                    result_dict[color] += int(value)
            final_count.append(result_dict)
        return final_count


day2 = Day2("day2/day2.txt")
day2.solve()

"""Day 7 of Advent Of Code.
pb 1: 21409
pb 2: 21165830176709
"""
import math
import re
from typing import List, Dict, Tuple
import sys

# add the base.py to the path
sys.path.append("../advent_of_code")
from base import BaseAdventOfCode


class Day8(BaseAdventOfCode):
    """Class for solving day 8."""

    def txt_parser(self, filepath: str):
        re_pattern: str = r"[A-Z]{3}"
        lines = super().txt_parser(filepath)
        self.indication: List[str] = list(lines[0])
        self.nodes: Dict[str, Tuple[str]] = {}

        for line in lines[2:]:
            if line == "":
                continue
            key, other = line.split(" = ")
            x = re.findall(pattern=re_pattern, string=other)
            if not x:
                continue
            self.nodes[key] = (x[0], x[1])

    def solve_first_pb(self):
        keep_going: bool = True
        current_node: str = self.nodes["AAA"][self._mapper(self.indication[0])]
        step: int = 1
        while keep_going:
            current_indication: str = self.indication[step % len(self.indication)]
            current_node = self.nodes[current_node][self._mapper(current_indication)]

            if current_node == "ZZZ":
                keep_going = False
            step += 1
        return step

    def solve_second_pb(self):
        # find node that ends with Z
        re_pattern: str = r"[A-Z]{2}A" # 2 random character + ends with Z
        nodes_keys: str = " ".join(list(self.nodes.keys()))

        x: List[str] = re.findall(pattern=re_pattern, string=nodes_keys)

        steps = [0] * len(x)
        for index, node in enumerate(x):
            current_node: str = node
            while current_node[-1] != "Z":
                current_indication: str = self.indication[steps[index] % len(self.indication)]
                current_node = self.nodes[current_node][self._mapper(current_indication)]
                steps[index] += 1
        return math.lcm(*steps)

    def _mapper(self, char:str) -> int:
        """Helper for mapping direction to integer.
        
        Args:
            char (str): the direction (either R or L).
        
        Returns:
            int: 0 for L, 1 for R.
        """
        if char not in ("L", "R"):
            raise ValueError("char can only be 'R' or 'L'")
        return 0 if char=="L" else 1

day8 = Day8("day8/day8.txt")
day8.solve()

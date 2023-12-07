"""Day 6 of Advent Of Code.
pb 1: 2374848
pb 2: 39132886
"""
import math
from typing import Tuple, Optional, List
import sys

# add the base.py to the path
sys.path.append("../advent_of_code")
from base import BaseAdventOfCode


class Day6(BaseAdventOfCode):
    """Class for solving day 6.
        velocity = distance/run_time
    <=> distance = velocity * run_time  
    <=> distance = waiting_time * (total_time - waiting_time)
    <=> -waiting_time^2 + waiting_time * total_time - distance = 0
    """

    def txt_parser(self, filepath: str):
        line: List[str] = super().txt_parser(filepath)
        self.time: List[int] = [int(elt) for elt in line[0].split(':')[1].split(" ") if elt.isdigit()]
        self.distance: List[int] = [int(elt) for elt in line[1].split(':')[1].split(" ") if elt.isdigit()]

    def solve_first_pb(self):
        result: int = 1
        for index, elt in enumerate(self.time):
            r1, r2 = self.quadratic_solver(-1, elt, - self.distance[index])
            result *= r2 - r1 + 1
        return result

    def solve_second_pb(self):
        self.time: str = "".join([str(elt) for elt in self.time])
        self.distance: str = "".join([str(elt) for elt in self.distance])
        r1, r2 = self.quadratic_solver(-1,
                                       int(self.time), - int(self.distance))
        return r2 - r1 + 1

    def quadratic_solver(self, a: float, b: float, c: float) -> Optional[Tuple[int, int]]:
        """Solve a quadratic inequation.
        The output will be the range where the quadratic function is positive.
        aX^2 + bX + c = 0

        In case r1, r2 are integer, we need to make +- 1 (because they are zeros...)
        Args:
            a (float): quadratic function first coefficient.
            b (float): quadratic function second coefficient.
            c (float): quadratic function last coefficient.

        Returns:
            Tuple[int, int]: the range where the function is above zero.
        """
        delta: int = b**2 - (4 * a * c)
        if delta <= 0:
            return None
        x1: float = abs((-b + math.sqrt(delta))) / 2
        x2: float = abs((-b - math.sqrt(delta))) / 2

        r1: float = min(x1, x2)
        r2: float = max(x1, x2)

        r1 = r1 + 1 if r1.is_integer() else r1
        r2 = r2 - 1 if r2.is_integer() else r2
        return math.ceil(r1), math.floor(r2)


day6 = Day6("day6/day6.txt")
day6.solve()

"""Base class for solving advent od code pb."""

class BaseAdventOfCode:
    """Base class for handling advent of code related problem."""

    def __init__(self, filepath:str) -> None:
        """Create attribut that contains the file."""
        self.entry = self.txt_parser(filepath=filepath)

    def txt_parser(self,filepath:str):
        """Method for parsing the given input.
        
        Args:
            filepath (str): path the input file.

        Returns:
            List: each element will be a line of the input file.
        """
        with open(filepath, "r", encoding='utf-8') as f:
            a = f.readlines()
            lines = [line.strip() for line in a]
            return lines

    def solve_first_pb(self):
        """Method for solving the first problem.
        Should return an integer (only format accepted by advent of code).
        """
        raise NotImplementedError("Method not implemented yet.")

    def solve_second_pb(self):
        """Method for solving the second problem.
        Should return an integer (only format accepted by advent of code).
        """
        raise NotImplementedError("Method not implemented yet.")

    def solve(self):
        """Display the result for each problem."""
        print(f"Solution for the first problem : {self.solve_first_pb()}")
        print(f"Solution for the second problem : {self.solve_second_pb()}")

from functools import cache

from aoc2023 import Solution


class Day12Solution(Solution):
    factor: int

    def solve(self, pipes, numbers):
        @cache
        def solve_helper(string, runs):
            m = sum(runs)
            if (
                m < string.count("#")
                or m > len(string) - string.count(".")
                or m + len(runs) - 1 > len(string)
            ):
                return 0
            if not string or not runs:
                return 1
            m = 0
            if (
                    "." not in string[0:runs[0]] and
                    not string[runs[0]:].startswith("#")):
                m += solve_helper(
                    string[runs[0] + 1:].strip("."), runs[1:]
                )
            if not string.startswith("#"):
                m += solve_helper(string[1:], runs)
            return m

        return solve_helper(pipes.strip("."), numbers)

    def result(self):
        result = 0
        for line in self.data:
            part1, part2 = line.split()
            numbers = tuple(int(x) for x in part2.split(",")) * self.factor
            pipes = "?".join((part1,) * self.factor)
            result += self.solve(pipes, numbers)
        return result


class Part1Solution(Day12Solution):
    factor = 1


class Part2Solution(Day12Solution):
    factor = 5

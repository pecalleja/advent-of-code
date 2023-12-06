import re

from aoc2023 import Solution

NUMBER_RE = re.compile(r"\d+")


class Day6Solution(Solution):
    def result(self):
        raise NotImplementedError

    def parse_input(self):
        time_line = self.data[0]
        distance_line = self.data[1]
        return zip(
            (int(x) for x in NUMBER_RE.findall(time_line)),
            (int(x) for x in NUMBER_RE.findall(distance_line)),
        )


class Part1Solution(Day6Solution):
    def result(self):
        result = 1
        for time, distance in self.parse_input():
            count = 0
            for option in range(1, time):
                travel_time = time - option
                travel_distance = travel_time * option
                if travel_distance > distance:
                    count += 1
            result *= count
        return result


class Part2Solution(Day6Solution):
    def result(self):
        return None

from functools import reduce

from aoc2023 import Solution


class Day15Solution(Solution):
    def __init__(self, data, *args, **kwargs):
        self.data = [x.strip() for x in data.split(",") if x.strip()]

    def result(self):
        raise NotImplementedError

    def hash(self, string):
        return reduce(lambda acc, c: 17 * (acc + ord(c)) % 256, string, 0)


class Part1Solution(Day15Solution):
    def result(self):
        return sum(map(self.hash, self.data))


class Part2Solution(Day15Solution):
    def result(self):
        return None

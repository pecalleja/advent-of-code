import re
import string
from collections import defaultdict
from math import prod

from aoc2023 import Solution


NUMBER_RE = re.compile(r"\d+")
SYMBOL_RE = re.compile(r"[^\s\d.]")


class Day3Solution(Solution):
    symbols = string.punctuation.replace(".", "")

    def result(self):
        raise NotImplementedError

    def parse(self):
        for y, line in enumerate(self.data):
            for match_number in NUMBER_RE.finditer(line):
                number = int(match_number.group(0))
                x0, x1 = match_number.span()
                for yy in range(max(y - 1, 0), min(y + 2, len(self.data))):
                    for match_symbol in SYMBOL_RE.finditer(
                        self.data[yy], x0 - 1, x1 + 1
                    ):
                        yield match_symbol.start(), yy, number


class Part1Solution(Day3Solution):
    def result(self):
        return sum(number for _, _, number in self.parse())


class Part2Solution(Day3Solution):
    def result(self):
        gears = defaultdict(list)
        for x, y, number in self.parse():
            gears[x, y].append(number)
        return sum(
            prod(numbers) for numbers in gears.values() if len(numbers) == 2
        )

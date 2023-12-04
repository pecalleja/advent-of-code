import re
import string
from collections import defaultdict
from math import prod

from aoc2023 import Solution


NUMBER_RE = re.compile(r"\d+")  # match a number
SYMBOL_RE = re.compile(
    r"[^\s\d.]"
)  # noqa Match a single character not present in the list


class Day3Solution(Solution):
    symbols = string.punctuation.replace(".", "")

    def result(self):
        raise NotImplementedError

    def parse(self):
        for n, line in enumerate(self.data):
            for match_number in NUMBER_RE.finditer(line):
                number = int(match_number.group(0))
                number_start, number_end = match_number.span()
                for n_context in range(
                    max(n - 1, 0), min(n + 2, len(self.data))
                ):
                    for match_symbol in SYMBOL_RE.finditer(
                        self.data[n_context], number_start - 1, number_end + 1
                    ):
                        yield match_symbol.start(), n_context, number


class Part1Solution(Day3Solution):
    def result(self):
        return sum(number for _, _, number in self.parse())


class Part2Solution(Day3Solution):
    def result(self):
        gears = defaultdict(list)
        for x, y, number in self.parse():
            gears[f"{x}_{y}"].append(number)
        return sum(
            prod(numbers) for numbers in gears.values() if len(numbers) == 2
        )

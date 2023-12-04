import os
import re
import string
from collections import defaultdict
from math import prod


NUMBER_RE = re.compile(r"\d+")
SYMBOL_RE = re.compile(r"[^\s\d.]")


class Solution:
    symbols = string.punctuation.replace(".", "")
    neighbors = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    def __init__(self, data):
        self.data = data

    def result(self):
        indexes = []
        for i in self.data:
            for j in i:
                if self.data[i][j] in self.symbols:
                    indexes.append((i, j))

    def parse(self):
        for y, line in enumerate(self.data):
            for match in NUMBER_RE.finditer(line):
                number = int(match.group(0))
                x0, x1 = match.span()
                for yy in range(max(y - 1, 0), min(y + 2, len(self.data))):
                    for match in SYMBOL_RE.finditer(
                        self.data[yy], x0 - 1, x1 + 1
                    ):
                        yield match.start(), yy, number

    def part1(self):
        return sum(number for _, _, number in self.parse())

    def part2(self):
        gears = defaultdict(list)
        for x, y, number in self.parse():
            gears[x, y].append(number)
        return sum(
            prod(numbers) for numbers in gears.values() if len(numbers) == 2
        )


if __name__ == "__main__":
    this_dir = os.path.dirname(__file__)
    full_path = os.path.join(this_dir, "input.txt")
    with open(full_path) as file_input:
        data = file_input.readlines()
        s = Solution(data)
        result = s.part1()
        print(f"The result for part1 input.txt is: {result}")
        result = s.part2()
        print(f"The result for part2 input.txt is: {result}")
